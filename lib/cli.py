from lib.db.models import Project, User, Issue
from lib.database import session, engine

def pause():
    input("Press Enter to continue...")

def create_user():
    name = input("Enter user name: ").strip()
    email = input("Enter user email: ").strip()
    if not name or not email:
        print("Name and email are required.")
        return
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print(f"User '{name}' created.")

def view_all_users():
    users = session.query(User).order_by(User.id).all()
    if not users:
        print("No users found.")
        return
    for user in users:
        print(f"{user.id}: {user.name} ({user.email})")

def create_new_project():
    name = input("Project name: ").strip()
    description = input("Project description: ").strip()
    if not name:
        print("Project name is required.")
        return
    project = Project(name=name, description=description)
    session.add(project)
    session.commit()
    print(f"Project '{name}' created.")

def view_all_projects():
    projects = session.query(Project).order_by(Project.id).all()
    if not projects:
        print("No projects found.")
        return
    for project in projects:
        desc = project.description or ""
        print(f"{project.id}: {project.name} - {desc}")

def create_new_issue():
    title = input("Issue title: ").strip()
    description = input("Issue description: ").strip()
    if not title:
        print("Title is required.")
        return

    projects = session.query(Project).order_by(Project.id).all()
    if not projects:
        print("No projects found. Create a project first.")
        return
    print("Choose project:")
    for p in projects:
        print(f"{p.id}: {p.name}")
    try:
        project_id = int(input("Project ID: ").strip())
    except ValueError:
        print("Invalid project ID.")
        return
    project = session.get(Project, project_id)
    if not project:
        print("Project not found.")
        return

    users = session.query(User).order_by(User.id).all()
    if not users:
        print("No users found. Create a user first.")
        return
    print("Assign to user:")
    for user in users:
        print(f"{user.id}: {user.name} ({user.email})")
    try:
        user_id = int(input("User ID: ").strip())
    except ValueError:
        print("Invalid user ID.")
        return
    user = session.get(User, user_id)
    if not user:
        print("User not found.")
        return

    issue = Issue(title=title, description=description, project_id=project.id, user_id=user.id)
    session.add(issue)
    session.commit()
    print(f"Issue '{title}' created and assigned to {user.name}.")

def view_all_issues():
    issues = (
        session.query(Issue)
        .order_by(Issue.id)
        .all()
    )
    if not issues:
        print("No issues found.")
        return

    header = f"{'ID':<4} | {'Title':<30} | {'Status':<12} | {'Project':<20} | {'Assignee':<20}"
    print(header)
    print("-" * len(header))
    for issue in issues:
        project_name = issue.project.name if issue.project else "Unassigned"
        user_name = issue.user.name if issue.user else "Unassigned"
        print(f"{issue.id:<4} | {issue.title[:30]:<30} | {issue.status:<12} | {project_name[:20]:<20} | {user_name[:20]:<20}")

def main_menu():
    while True:
        print("\nBug Tracker")
        print("1. Create a new project")
        print("2. View all projects")
        print("3. Create a new issue")
        print("4. View all issues")
        print("5. Create a new user")
        print("6. View all users")
        print("7. Exit")

        choice = input("Choose 1-7: ").strip()

        if choice == "1":
            create_new_project()
            pause()
        elif choice == "2":
            view_all_projects()
            pause()
        elif choice == "3":
            create_new_issue()
            pause()
        elif choice == "4":
            view_all_issues()
            pause()
        elif choice == "5":
            create_user()
            pause()
        elif choice == "6":
            view_all_users()
            pause()
        elif choice == "7":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    # Useful if you want to confirm which DB file is used:
    # print(f"DB file: {engine.url.database}")
    main_menu()
