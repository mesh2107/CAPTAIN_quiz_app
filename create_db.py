import sqlite3

# Connect to database (or create it if it doesn't exist)
conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()

# Drop table if it already exists (optional during development)
cursor.execute('DROP TABLE IF EXISTS questions')

# Create new table with topic column
cursor.execute('''
    CREATE TABLE questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        option1 TEXT NOT NULL,
        option2 TEXT NOT NULL,
        option3 TEXT NOT NULL,
        option4 TEXT NOT NULL,
        answer TEXT NOT NULL,
        topic TEXT NOT NULL
    )
''')

# Optional: Insert a sample question for testing
cursor.execute('''
    INSERT INTO questions (question, option1, option2, option3, option4, answer, topic)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', (
    "What is the capital of France?",
    "Berlin",
    "Madrid",
    "Paris",
    "Lisbon",
    "Paris",
    "Geography"
))

# Commit changes and close
conn.commit()
conn.close()

print("Database created and sample question inserted.")
