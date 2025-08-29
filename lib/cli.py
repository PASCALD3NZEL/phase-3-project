# lib/cli.py
from lib.db.models import Project, User, Issue
from lib.database import session, engine

# Print the database file location (debugging)
print(f"Database file: {engine.url.database}")

# Create a new user
u = User(name="Denzel", email="denzel@example.com")
session.add(u)
session.commit()   # 👈 MUST commit

def view_all_projects():
    """Check what projects exist in the database"""
    print("\n📋 Your Projects:")
    projects = session.query(Project).all()
    
    if not projects:
        print("No projects yet! Create your first one.")
        return
    
    for project in projects:
        print(f"• {project.name} - {project.description}")

def create_new_project():
    """The first function we need!"""
    print("\n➕ Let's create your first project!")
    
    name = input("What should we call this project? ").strip()
    description = input("What's it about? ").strip()

    new_project = Project(name=name, description=description)
    session.add(new_project)
    session.commit()
    
    print(f"✅ Perfect! '{name}' is now ready for issues!")
    input("Press Enter to continue...")

def view_all_issues():
    print("\n--- All Issues ---")
    all_issues = session.query(Issue).all()
    
    if not all_issues:
        print("Hooray! The issue board is clear! 🎉")
        return
    
    print(f"{'ID':<4} | {'Title':<25} | {'Status':<12} | {'Project':<15} | {'Assignee':<15}")
    print("-" * 80)
    for issue in all_issues:
        project_name = issue.project.name[:14] if issue.project else "Unassigned"
        assignee_name = issue.user.name[:14] if issue.user else "Unassigned"  # <-- FIXED
        print(f"{issue.id:<4} | {issue.title[:24]:<25} | {issue.status:<12} | {project_name:<15} | {assignee_name:<15}")

def create_user():
    name = input("👤 Enter user name: ").strip()
    email = input("📧 Enter user email: ").strip()
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print(f"✅ User {name} created successfully!")
    input("Press Enter to continue...")

def view_all_users():
    users = session.query(User).all()
    for user in users:
        print(user)
    input("Press Enter to continue...")

def create_new_issue():
    print("\n🛠️  Let's add a new issue!")
    title = input("What's the title of the issue? ").strip()
    description = input("Describe the issue: ").strip()

    print("\nWhich project is this for?")
    all_projects = session.query(Project).all()
    if not all_projects:
        print("Oops! No projects found. You need to create a project first!")
        input("(Press Enter to go back...)")
        return
    for index, project in enumerate(all_projects, start=1):
        print(f"{index}. {project.name}")
    try:
        choice = int(input(f"Enter the project number (1-{len(all_projects)}): "))
        selected_project = all_projects[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice! Let's start over.")
        input("(Press Enter to go back...)")
        return

    print("\nWho should this be assigned to?")
    all_users = session.query(User).all()
    if not all_users:
        print("No users found. Please add users first!")
        input("(Press Enter to go back...)")
        return
    for user in all_users:
        print(f"{user.id}. {user.name} ({user.email})")
    try:
        user_id = int(input("Enter the ID of the user to assign this issue: "))
        selected_user = session.query(User).get(user_id)
        if not selected_user:
            raise ValueError
    except (ValueError, TypeError):
        print("Invalid user ID! Let's start over.")
        input("(Press Enter to go back...)")
        return

    new_issue = Issue(
        title=title,
        description=description,
        project_id=selected_project.id,
        user_id=selected_user.id
    )
    session.add(new_issue)
    session.commit()
    print(f"\n✅ Success! New issue '{title}' has been created and assigned to {selected_user.name}!")
    input("(Press Enter to continue...)")

def main_menu():
    while True:
        print("\n🐛 Welcome to Your Bug Tracker!")
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
        elif choice == "2":
            view_all_projects()
            input("Press Enter to continue...")
        elif choice == "3":
            create_new_issue()
        elif choice == "4":
            view_all_issues()
            input("Press Enter to continue...")
        elif choice == "5":
            create_user()
        elif choice == "6":
            view_all_users()
        elif choice == "7":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Please choose a valid option (1-7)")

if __name__ == "__main__":
    main_menu()