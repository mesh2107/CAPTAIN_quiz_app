# CAPTAINS - Quiz Application

CAPTAINS is a full-stack quiz application built with Python (Flask), SQLite, HTML, CSS, and JavaScript. It allows users to select quiz topics and the number of questions to answer, providing a fun and interactive way to test their knowledge.

---

## Features

- User-friendly UI with responsive design.
- Select quiz topic and number of questions.
- Instant scoring and results display.
- Questions stored in SQLite database.
- Easily extensible with CSV imports for new quiz data.

---

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python with Flask framework
- **Database:** SQLite

---

## Getting Started

### Prerequisites

- Python 3.x installed
- `pip` package manager

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/CAPTAIN_quiz_app.git
   cd CAPTAIN_quiz_app
   
2. Create and activate a virtual environment (optional but recommended):
   python -m venv venv
  # Windows
  venv\Scripts\activate
  # Mac/Linux
  source venv/bin/activate

3.Install required packages:
  pip install -r requirements.txt

4.Initialize the database:
  python create_db.py

5.Run the Flask app:
  python app.py

6.Open your browser and go to:
  http://127.0.0.1:5000



#Usage:
Select a quiz topic from the dropdown.
Choose the number of questions.
Start the quiz and answer the questions.
View your score at the end.

#Adding New Quiz Data
You can add new quiz questions by providing CSV files with the following columns:
  id, topic, question, option1, option2, option3, option4, answer
Use the load_questions.py script to import new questions into the database.

#Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you want to change.

#License
This project is licensed under the MIT License.

