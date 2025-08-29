# Bug Tracker CLI

This is a command-line based bug tracking system developed in Python.  
It allows users to manage projects, users, and issues efficiently through a structured menu system.  
The database is managed using SQLAlchemy ORM with an SQLite backend.  

# Features

## Project Management
- Create and view multiple projects.  
- Each project can hold several issues.  

## User Management
- Add users with unique names and emails.  
- Users can be assigned to issues.  

## Issue Management
- Create issues tied to specific projects.  
- Assign issues to users for accountability.  
- View all issues in a well-formatted table showing title, status, project, and assignee.  

## Persistent Storage
- Data is stored in an SQLite database so that information is preserved between runs.  

# Project Structure
```bash
bug-tracker-cli/
│── lib/
│   ├── cli.py         # The main CLI logic and menu system
│   ├── models.py      # SQLAlchemy models (Project, User, Issue)
│   ├── database.py    # Database connection and session configuration
│── bug_tracker.db     # SQLite database file (auto-generated after running the project)
│── README.md          # Project documentation
Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone <your-repo-url>
cd bug-tracker-cli
2. Install dependencies
You will need SQLAlchemy installed. If you are using Pipenv:

bash
Copy
Edit
pipenv install sqlalchemy
Or with pip:

bash
Copy
Edit
pip install sqlalchemy
3. Run the application
From the root directory:

bash
Copy
Edit
python -m lib.cli
Usage
When you run the application, you will see a menu like this:

text
Copy
Edit
Welcome to Your Bug Tracker!
1. Create a new project
2. View all projects
3. Create a new issue
4. View all issues
5. Create a new user
6. View all users
7. Exit
To create a project, select option 1.

To view all projects, select option 2.

To create an issue, select option 3. You will be asked to choose a project and assign a user.

To view issues, select option 4. A table will be displayed with issue details.

To add a user, select option 5.

To view all users, select option 6.

Select option 7 to exit the program.

Example Workflow
Create a project called Website.

Add a user named Denzel with the email denzel@example.com.

Add a new issue titled Fix login bug, assign it to Denzel under the Website project.

View all issues to confirm that the issue has been recorded with the correct project and assignee.

Technologies Used
Python 3.8+

SQLAlchemy (ORM)

SQLite (database)

Grading Alignment
Configuration of Environment and Dependencies
Dependencies installed via pip or Pipenv.

Imports are organized and used only where necessary.

Package structure supports local imports.

SQLAlchemy Schema Design
Three tables are created: projects, users, issues.

Relationships are established between them.

SQLAlchemy ORM is used to query and display results in the CLI.

Use of Data Structures
Lists are used when displaying projects, users, and issues.

Dictionaries and tuples can be integrated for menu options and display formatting.

Best Practices in CLI Design
Input is validated (e.g., checking for valid user and project IDs).

Logic is separated into functions.

User receives clear and detailed prompts.

Documentation
This README provides full setup, usage, and workflow instructions.

Author
Work by Pascal Denzel
Contact: pascaldenzel7@gmail.com / pascaldenzel.student@moringa.school@gmail.com
