from flask import Flask, render_template, redirect, url_for, request, session
import pathlib
import random
from string import ascii_lowercase
# imports tomli for older versions of Python if tomllib fails
try:
    import tomllib 
except ModuleNotFoundError:
    import tomli as tomllib 

# 52 questions total

app = Flask(__name__)
app.secret_key = 'LOTR'

NUM_QUESTIONS_PER_QUIZ = 8
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"


# function to load and randomize questions
def prepare_questions(path, num_questions):
    # load questions from TOML file
    with open(path, 'rb') as f:
        data = tomllib.load(f)
        questions = data["questions"] 
    
    # check if questions are loaded correctly
    print("Loaded questions:", questions)

    # randomly sample questions if available
    return random.sample(questions, k=min(num_questions, len(questions)))


@app.route('/')
def index():
    print("index page accessed")
    return redirect(url_for('landing'))


@app.route('/landing')
def landing():
    print("landing page accessed")
    return render_template('landingpage.html')


# initialize quiz, selects questions, redirects to first question
@app.route('/quiz', methods=['POST'])
def start_quiz():
    questions = prepare_questions(QUESTIONS_PATH, num_questions=NUM_QUESTIONS_PER_QUIZ)

    # check if questions are loaded
    if not questions:
        return "No questions found!", 500
    
    # store questions and initialize session variables
    session['questions'] = questions  # save selected questions in session
    session['current_question'] = 0   # track index of current question
    session['num_correct'] = 0        # initialize count of correct answers
    return redirect(url_for('questions', question_num=1))


@app.route('/question/<int:question_num>', methods=['GET', 'POST'])
def questions(question_num):
    questions = session.get('questions')

    # check if questions exist in the session and if current question index is valid
    if questions is None or session['current_question'] >= len(questions):
        return redirect(url_for('results'))

    # handle form submission for answers
    if request.method == 'POST':
        selected_answer = request.form.get('answer')
        correct_answer = questions[session['current_question']]['answer']
        # increment correct answers count
        if selected_answer == correct_answer:
            session['num_correct'] += 1

        # move to next question
        session['current_question'] += 1
        if session['current_question'] < len(questions):
            return redirect(url_for('questions', question_num=session['current_question'] + 1))
        else:
            return redirect(url_for('results'))

    # prepare current question data for rendering
    question_data = questions[session['current_question']]
    question_text = question_data['question']
    alternatives = [question_data['answer']] + question_data['alternatives']
    random.shuffle(alternatives)

    # pass correct answer along with question data
    correct_answer = question_data['answer']
    
    # calculate total questions
    total_questions = len(questions)

    return render_template('questions.html', question=question_text, alternatives=alternatives, question_num=session['current_question'] + 1, total_questions = total_questions, question_data=question_data)

# display results
@app.route('/results')
def results():
    num_correct = session.get('num_correct', 0)  
    return render_template('results.html', score=num_correct)   

if __name__ == "__main__":
    app.run(debug=True, port=5001)

