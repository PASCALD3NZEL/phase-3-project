# lib/cli.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Project, User, Issue  # Make sure it's Issue if you renamed Ticket!

# --- Database Setup ---
engine = create_engine("sqlite:///bug_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()

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
        assignee_name = issue.assignee.name[:14] if issue.assignee else "Unassigned"
        print(f"{issue.id:<4} | {issue.title[:24]:<25} | {issue.status:<12} | {project_name:<15} | {assignee_name:<15}")

def create_new_issue():
    print("\n🛠️  Let's add a new issue!")
    
    # 1. Get the basic info
    title = input("What's the title of the issue? ").strip()
    description = input("Describe the issue: ").strip()

    # 2. List all projects and let the user pick one
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

    # 3. List all users and let the user pick an assignee
    print("\nWho should this be assigned to?")
    all_users = session.query(User).all()
    if not all_users:
        print("No users found. Please add users first!")
        input("(Press Enter to go back...)")
        return

    for index, user in enumerate(all_users, start=1):
        print(f"{index}. {user.name}")
    
    try:
        choice = int(input(f"Enter the user number (1-{len(all_users)}): "))
        selected_user = all_users[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice! Let's start over.")
        input("(Press Enter to go back...)")
        return

    # 4. Create and save the new Issue!
    new_issue = Issue(
        title=title,
        description=description,
        project_id=selected_project.id,
        assignee_id=selected_user.id,
        reporter_id=selected_user.id  # In a real app, use the logged-in user
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
        print("3. Create a new issue")  # Changed text
        print("4. View all issues")
        print("5. Exit")
        
        choice = input("Choose 1, 2, 3, 4, or 5: ").strip()
        
        if choice == "1":
            create_new_project()
        elif choice == "2":
            view_all_projects()
            input("Press Enter to continue...")
        elif choice == "3":
            # This now calls our brand new function!
            create_new_issue()
        elif choice == "4":
            view_all_issues()
            input("Press Enter to continue...")
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Please choose 1, 2, 3, 4, or 5")

if __name__ == "__main__":
    main_menu()