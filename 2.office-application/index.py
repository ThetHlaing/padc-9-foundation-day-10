from Enginner import Enginner
from Accountant import Accoutant
from Company import Company
from Project import Project

# Create a company
company = Company()

def index():
    try:
        selected_option = input(
            f'Please select the action you want to do.\n'
            f'[1] Add New Enginner\n'
            f'[2] Add New Accountant\n'
            f'[3] Get New Project\n'
            f'[4] List all employee\n'
        )

        if(selected_option == '1'):
            engineer = Enginner(input("What's the name of the engineer? : "))
            company.hire(engineer)
            # hire this enginner into company
        elif(selected_option == '2'):
            accountant = Accoutant(input("What's the name of the accountant? :"))
            company.hire(accountant)
        elif(selected_option == '3'):
            project = Project(input("What's the project type"),'New Project')
            company.getNewProject(project)
        elif(selected_option == '4'):
            count = 1
            for employee in company.subscribers:
                print(f"{count} {employee.name}")
                count += 1

        user_choice = input("Do you want to go back to menu? : y/n \n")
        if(user_choice == 'y'):
            index()
        else:
            print("Bye Bye")
    except KeyboardInterrupt:
        print("Bye bye")


if __name__ == "__main__":
    index()