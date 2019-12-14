from Department import Department

from MainController import MainController       


def index():
    try:
        selected_option = input(
            f'Please select the action you want to do.\n'
            f'[1] Add New Employee\n'
            f'[2] Add New Department\n'
            f'[3] View All Employee\n'
            f'[4] View All Departments\n'
            f'[5] Increase Salary\n'
        )

        if(selected_option == '1'):
            MainController.addNewEmployee()
        elif(selected_option == '2'):
            MainController.addNewDepartment()
        elif(selected_option == '3'):
            MainController.displayAllEmployees()
        elif(selected_option == '4'):
            MainController.displayAllDepartments()
        elif(selected_option == '5'):
            MainController.increaseSalary()
        user_choice = input("Do you want to go back to menu? : y/n \n")
        if(user_choice == 'y'):
            index()
        else:
            print("Bye Bye")
    except KeyboardInterrupt:
        print("Bye bye")


index()
