from flask import Flask, render_template_string, request, jsonify
import random
import pyttsx3

app = Flask(__name__)

# List of answers to various questions in English
responses = {
    "How are you?": "I am a voice assistant written in Python. I'm doing great, thank you!",
    "What is your name?": "I am a voice assistant created to answer your questions. I don't have a personal name.",
    "What do you do?": "I can help answer questions and provide information in a conversational way.",
    "Who created you?": "I was created by a team of developers working with Python programming language.",
    "Tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
    "What is Python?": "Python is a popular programming language known for its simplicity and versatility.",
    "How can I learn Python?": "You can learn Python through various online courses, books, and tutorials. Start with the basics like variables, loops, and functions.",
    "What is AI?": "AI (Artificial Intelligence) refers to the simulation of human intelligence processes by machines, especially computer systems.",
    "Tell me something interesting": "Did you know that the Eiffel Tower can grow by up to 15 cm during the summer due to thermal expansion?",
    "Who is a programmer?": "A programmer is someone who writes computer software. They write code to solve problems and create applications.",
    "What is Python programming language?": "Python is a high-level, interpreted programming language known for its simplicity and readability. It is widely used for web development, data science, machine learning, and more.",
    "What is Discord?": "Discord is a communication platform designed for creating communities. It supports voice, video, and text chat, making it popular among gamers and online communities.",
    "What is Slack?": "Slack is a messaging platform designed for teams and organizations. It allows for group communication, file sharing, and integration with various apps to enhance collaboration.",
    "What is Java?": "Java is a general-purpose, high-level programming language. It's known for its portability, as Java applications can run on any device that supports the Java Virtual Machine (JVM).",
    "What is HTML?": "HTML (HyperText Markup Language) is the standard language used to create web pages. It structures the content on the page with elements like headings, paragraphs, and links.",
    "What is CSS?": "CSS (Cascading Style Sheets) is used to style and design the layout of web pages. It controls the color, font, size, spacing, and positioning of elements on a webpage.",
    "What is JavaScript?": "JavaScript is a programming language used to create interactive effects within web browsers. It's essential for front-end development and also used in back-end with Node.js.",
    "What is GitHub?": "GitHub is a platform for hosting and sharing code. It allows developers to collaborate, track changes in code, and manage version control using Git.",
    "What is machine learning?": "Machine learning is a subset of AI where computers use algorithms to learn patterns from data, and make predictions or decisions without being explicitly programmed for specific tasks.",
    "What is deep learning?": "Deep learning is a subset of machine learning that uses artificial neural networks to model high-level abstractions in data. It's used in applications like speech recognition, image processing, and more.",
    "What is an algorithm?": "An algorithm is a step-by-step procedure or formula for solving a problem or performing a task, like sorting data or searching for information.",
    "What is a database?": "A database is an organized collection of data that can be accessed, managed, and updated. Databases are used to store and retrieve information quickly.",
    "What is SQL?": "SQL (Structured Query Language) is the standard language used to interact with databases. It allows you to perform operations like retrieving, inserting, updating, and deleting data.",
    "What is an IDE?": "An IDE (Integrated Development Environment) is a software application that provides comprehensive tools for programming, including a code editor, compiler, debugger, and other utilities.",
    "What is a variable in programming?": "A variable in programming is a container for storing data values. It has a name and can hold different types of data, such as numbers, text, or objects.",
    "What is a function in programming?": "A function is a block of code designed to perform a specific task. It can take inputs (parameters), process them, and return an output.",
    "What is recursion?": "Recursion occurs when a function calls itself in order to solve smaller instances of the same problem. It's commonly used in tasks like tree traversal and calculating factorials.",
    "What is a framework?": "A framework is a pre-built collection of tools, libraries, and conventions used to help developers create applications more efficiently. Examples include Django (for Python) and React (for JavaScript).",
    "What is Docker?": "Docker is a platform used to develop, ship, and run applications inside containers. Containers help ensure that an application runs consistently across different environments.",
    "What is Kubernetes?": "Kubernetes is an open-source system for automating the deployment, scaling, and management of containerized applications.",
    "What is HTTP?": "HTTP (HyperText Transfer Protocol) is the protocol used for transferring data over the web. It's the foundation of data communication on the internet.",
    "What is REST API?": "REST (Representational State Transfer) API is an architectural style for designing networked applications. It uses HTTP requests to perform CRUD operations on resources.",
    "What is Agile methodology?": "Agile is a project management and software development methodology that emphasizes flexibility, collaboration, and customer feedback, often used in iterative development cycles.",
    "What is Scrum?": "Scrum is an Agile framework used for managing and completing complex projects. It focuses on delivering working software in short iterations called sprints.",
    "What is CI/CD?": "CI/CD (Continuous Integration/Continuous Deployment) is a practice in software development that encourages developers to integrate their code frequently and automatically deploy it to production.",
    "What is version control?": "Version control is a system that tracks changes to code over time, allowing developers to collaborate and revert to previous versions if necessary.",
    "What is a code repository?": "A code repository is a storage location for your codebase. It can be local or hosted online, like GitHub, GitLab, or Bitbucket, and it helps track code changes.",
    "What is a pull request?": "A pull request is a way of submitting contributions to a codebase. It allows developers to review changes before they are merged into the main project."
}


HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Voice Assistant - Chat</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 500px;
            width: 100%;
        }

        input {
            width: 80%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }

        button {
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        #response {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Voice Assistant</h1>
        <input type="text" id="question" placeholder="Ask me a question...">
        <button id="ask-btn">Ask Question</button>
        
        <div id="response">
            <p id="text-response"></p>
        </div>
    </div>

    <script>
        document.getElementById('ask-btn').addEventListener('click', function() {
            var question = document.getElementById('question').value;

            fetch('/ask', {
                method: 'POST',
                body: new URLSearchParams({ 'question': question })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('text-response').textContent = data.text;
            })
            .catch(error => console.error('Error:', error));
        });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']

     # Searching for answers based on a query
    answer_text = responses.get(question, "Sorry, I don't understand that question.")

    # Generating a voice response
    engine = pyttsx3.init()

 
    engine.say(answer_text)
    engine.runAndWait()

    # We return the text of the response in JSON form
    return jsonify({
        'text': answer_text
    })

if __name__ == '__main__':
    app.run(debug=True)