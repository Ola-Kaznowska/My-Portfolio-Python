import os
import random

# Clear the screen
os.system("cls")

# Course details for each skill level
Beginner = ["Python", "HTML", "CSS"]
Intermediate = ["SQL", "Hacking", "C#"]
Advanced = ["C++", "Java", "Machine Learning"]

# Course modules (10 modules for each course)
CourseModules = {
    "Python": [
        "1. Introduction to Python programming",
        "2. Installation and environment setup",
        "3. Variables, data types, and operators",
        "4. Conditional statements",
        "5. Loops: for and while",
        "6. Functions and modules",
        "7. Working with text files",
        "8. Debugging code",
        "9. Building a simple calculator",
        "10. Final project: text-based game"
    ],
    "HTML": [
        "1. Introduction to HTML",
        "2. Creating a basic HTML document",
        "3. Page structure: headers, paragraphs, and sections",
        "4. Images and multimedia",
        "5. Links and navigation",
        "6. Lists: ordered and unordered",
        "7. Forms and their elements",
        "8. Tables and their usage",
        "9. Semantic HTML5 tags",
        "10. Final project: business card webpage"
    ],
    "CSS": [
        "1. Basics of CSS styles",
        "2. Colors, backgrounds, and fonts",
        "3. CSS selectors and classes",
        "4. Element layout: box model",
        "5. Positioning elements",
        "6. Styling tables and forms",
        "7. Media queries and responsiveness",
        "8. CSS animations",
        "9. Flexbox and Grid",
        "10. Final project: responsive webpage"
    ],
    "SQL": [
        "1. Basics of SQL language",
        "2. Creating databases",
        "3. SELECT queries",
        "4. Filtering data",
        "5. Joining tables",
        "6. Aggregating functions",
        "7. Subqueries",
        "8. Query optimization",
        "9. Creating indexes",
        "10. Final project: database for an app"
    ],
    "Hacking": [
        "1. Introduction to ethical hacking",
        "2. Basics of computer security",
        "3. Tools for penetration testing",
        "4. Identifying security vulnerabilities",
        "5. Exploits and attack methods",
        "6. Network security and protection",
        "7. Cryptography and secure communication",
        "8. Phishing and social engineering",
        "9. Creating penetration testing reports",
        "10. Final project: simulate an attack"
    ],
    "C#": [
        "1. Introduction to C#",
        "2. Object-oriented programming",
        "3. Variables and operators in C#",
        "4. Conditional statements and loops",
        "5. Working with classes and objects",
        "6. Collections and data structures",
        "7. Event handling",
        "8. Windows applications in C#",
        "9. Testing applications",
        "10. Final project: desktop application"
    ],
    "C++": [
        "1. Introduction to C++",
        "2. Basics of object-oriented programming",
        "3. Variables, data types, and operators",
        "4. Functions in C++",
        "5. Data structures and algorithms",
        "6. Dynamic memory allocation",
        "7. Working with files",
        "8. Multithreading programming",
        "9. Code optimization",
        "10. Final project: command-line tool"
    ],
    "Java": [
        "1. Introduction to Java",
        "2. Classes and objects in Java",
        "3. Variables, data types, and operators",
        "4. Conditional statements and loops",
        "5. Collections and data structures",
        "6. Working with databases",
        "7. Design patterns in Java",
        "8. Parallel programming",
        "9. Testing applications",
        "10. Final project: web application"
    ],
    "Machine Learning": [
        "1. Introduction to Machine Learning",
        "2. Classification algorithms",
        "3. Linear and logistic regression",
        "4. Clustering and grouping algorithms",
        "5. Neural networks",
        "6. Data preprocessing",
        "7. Model training and tuning",
        "8. Model validation and testing",
        "9. Applications in data analysis",
        "10. Final project: predictive model"
    ]
}

# Ask the user for their skill level
User = int(input("What is your programming skill level? Choose 1-3: "))

if User == 1:
    print(f"\nBeginner level: Available languages: {', '.join(Beginner)}")
    for _ in range(3):  # Show 3 random languages
        language = random.choice(Beginner)
        print(f"\nChosen language: {language}")
        for module in CourseModules[language]:
            print(f"{module}")
elif User == 2:
    print(f"\nIntermediate level: Available languages: {', '.join(Intermediate)}")
    for _ in range(3):  # Show 3 random languages
        language = random.choice(Intermediate)
        print(f"\nChosen language: {language}")
        for module in CourseModules[language]:
            print(f"{module}")
elif User == 3:
    print(f"\nAdvanced level: Available languages: {', '.join(Advanced)}")
    for _ in range(3):  # Show 3 random languages
        language = random.choice(Advanced)
        print(f"\nChosen language: {language}")
        for module in CourseModules[language]:
            print(f"{module}")
else:
    print("\nInvalid level. Choose a number between 1 and 3.")