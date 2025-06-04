from flask import Flask, render_template, request
import sqlite3
import random


app = Flask(__name__)

def get_questions(topic=None):
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    if topic:
        c.execute("SELECT * FROM questions WHERE topic = ?", (topic,))
    else:
        c.execute("SELECT * FROM questions")
    questions = c.fetchall()
    conn.close()
    return questions


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    topic = request.args.get('topic')
    num_questions = request.args.get('num_questions', default=5, type=int)
    
    # Limit the number of questions max to avoid abuse
    if num_questions < 1:
        num_questions = 1
    elif num_questions > 20:
        num_questions = 20

    conn = sqlite3.connect('quiz.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Get all question IDs for the topic
    cursor.execute('SELECT id FROM questions WHERE topic = ?', (topic,))
    all_question_ids = [row['id'] for row in cursor.fetchall()]

    # If requested more questions than available, adjust
    if len(all_question_ids) < num_questions:
        num_questions = len(all_question_ids)

    # Randomly sample question ids
    selected_ids = random.sample(all_question_ids, num_questions)

    # Fetch full question details for selected ids
    placeholders = ','.join('?' for _ in selected_ids)
    cursor.execute(f'SELECT * FROM questions WHERE id IN ({placeholders})', selected_ids)
    questions = cursor.fetchall()

    conn.close()

    return render_template('quiz.html', questions=questions, topic=topic)


@app.route('/submit', methods=['POST'])
def submit():
    import sqlite3
    conn = sqlite3.connect('quiz.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    score = 0
    total = 0

    for key in request.form:
        if key.startswith('q_'):
            question_id = key.split('_')[1]
            user_answer = request.form[key]

            cursor.execute('SELECT answer FROM questions WHERE id = ?', (question_id,))
            row = cursor.fetchone()

            if row:
                correct_answer = row['answer']
                if user_answer.strip().lower() == correct_answer.strip().lower():
                    score += 1
                total += 1

    conn.close()

    return render_template('result.html', score=score, total=total)





if __name__ == '__main__':
    app.run(debug=True)