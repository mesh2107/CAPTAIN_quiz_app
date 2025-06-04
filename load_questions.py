
import csv
import sqlite3

def load_questions_from_csv(csv_file, db_file='quiz.db'):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        count = 0
        for row in reader:
            cursor.execute('''
                INSERT INTO questions (question, option1, option2, option3, option4, answer, topic)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                row['question'],
                row['option a'],
                row['option b'],
                row['option c'],
                row['option d'],
                row['correct'],
                row['topic']
            ))
            count += 1

    conn.commit()
    conn.close()
    print(f'{count} questions loaded successfully.')

if __name__ == '__main__':
    load_questions_from_csv('questions.csv')
