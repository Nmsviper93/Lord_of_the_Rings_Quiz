# Lord of the Rings Quiz App

The Lord of the Rings Quiz App is a Flask-based web application that allows users to take a randomized multiple choice quiz. Various results will lead to different end points, with lower results offering suggestions for relevant resources. On the results page there is also a link to lead back to the landing page.


## Table of Contents

### Features

### Installation

### Usage

<!-- ### Testing -->

### Technologies Used

### Contributing

### License

-------------------------------

## Features

-**Landing Page:** Welcomes users and provides an entry point to begin the quiz.

-**Questions Page:** Displays a randomized selection of 8 questions, one a time, each with 4 answers to choose from.

-**Results Page:** Displays quiz results, with lower scores being offered suggestions of resources to learn more about Lord of the Rings. This page also includes a route back to the landing page.

-------------------------------

## Installation

To run the Lord of the Rings Quiz App locally, follow these steps:

1. **Clone the repository:**

bash
git clone https://github.com/yourusername/Lord_of_the_Rings_Quiz.git
cd Lord_of_the_Rings_Quiz


2. **Setup virtual environment:**

bash
python -m venv venv
source venv/bin/activate   ## On Windows use `venv\Scripts\activate`

<!-- 3. **Install dependencies:**

bash
pip install -r requirements.txt -->


4. **Run the Flask application:**

bash
python quiz.py


**Access the application:**

Open a web browser and go to http://localhost:5001 to view the app.

-------------------------------

### Usage

- **Landing Page:** Upon accessing the application, users are greeted with a welcoming landing page introducing the app and providing a button to begin the quiz.

- **Questions Page:** Users are presented with a randomized question and given 4 answers to choose from.

- **Results Page:** Displays user's score with a corresponding message based on that score. Lower scores include suggestions for resources to learn more about Lord of the Rings. This page also includes a route back to the landing page.

-------------------------------

<!-- ## Testing

To run the tests for the Lord of the Rings Quiz App, execute the following command:

bash
python -m unittest test_quiz.py -->


-------------------------------

## Technologies Used

-Python: Programming language used for backend development.

-Flask: Web framework used for building the web application.

-HTML/CSS: Frontend design and styling of web pages.

-------------------------------

## Contributing

This is currently the MVP, but contributions to the Lord of the Rings Quiz App are welcome! If you find any issues or have suggestions for improvement, please submit an issue or pull request. For major changes, please open an issue first to discuss what you would like to change.

-------------------------------

## License

MIT License