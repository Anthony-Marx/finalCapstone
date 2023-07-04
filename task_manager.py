# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#TO DO/ASK ABOUT
# - r: Errors reading txt file
# - vm: selecting tasks, mark as comp, edit task
# - gr: adding some of the correct content

#Keep user and password in pairs
#test if user is in list when adding task
#if today's date is larger than due date then its overdue
#date.today() for todays date

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

def reg_user():
    # - Request input of a new username
    new_username = input("New Username: ")

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")



    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("Passwords Match")
        username_password[new_username] = new_password

        with open("user.txt", "r+") as out_file:

            lines = out_file.readlines()

            lines_split = lines[0].strip().split(';')

            print(lines_split)





            if new_username == lines_split[0]:
                print("Error: Username already in use, please enter a different username. ")

            else:

                print("New user added")

                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")

                    out_file.write("\n".join(user_data))


    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")

    out_file.close()

def add_task():
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()

    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list = []

    task_list.append(new_task)

    with open("tasks.txt", "a+") as task_file:

        task_list_to_write = []

        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
            task_string = str(task_list_to_write)
            task_file.write(task_string + '\n')
    print("Task successfully added.")

    task_file.close()




def view_all():

    with open('tasks.txt', 'r') as all_tasks:

        show_tasks = all_tasks.readlines()

    for t in show_tasks:

        all_tasks_split = t.strip().split(";")

        disp_str = f"Task: \t\t {all_tasks_split[1]}\n"
        disp_str += f"Assigned to: \t {all_tasks_split[0]}\n"
        disp_str += f"Date Assigned: \t {all_tasks_split[4]}\n"
        disp_str += f"Due Date: \t {all_tasks_split[3]}\n"
        disp_str += f"Task Description: \n {all_tasks_split[2]}\n"
        print(disp_str)

    all_tasks.close()


def view_mine():

    with open('tasks.txt', 'r') as user_tasks:

        show_tasks = user_tasks.readlines()

        index_list = []

    for i, t in enumerate(show_tasks):

        user_tasks_split = t.strip().split(";")

        if user_tasks_split[0] == curr_user:
            disp_str = f"Task {i+1}: \t\t {user_tasks_split[1]}\n"
            disp_str += f"Assigned to: \t {user_tasks_split[0]}\n"
            disp_str += f"Date Assigned: \t {user_tasks_split[4]}\n"
            disp_str += f"Due Date: \t {user_tasks_split[3]}\n"
            disp_str += f"Task Description: \n {user_tasks_split[2]}\n"
            print(disp_str)

            index_list.append(i)

    user_input = input("Which task would you like to select? Input -1 to return to main menu.")

    for i in index_list:
        if i == user_input:

                disp_str = f"Task {i}: \t\t {user_tasks_split[1]}\n"
                disp_str += f"Assigned to: \t {user_tasks_split[0]}\n"
                disp_str += f"Date Assigned: \t {user_tasks_split[4]}\n"
                disp_str += f"Due Date: \t {user_tasks_split[3]}\n"
                disp_str += f"Task Description: \n {user_tasks_split[2]}\n"
                print(disp_str)

        elif user_input == '-1':
            break

        user_tasks.close()


def mark():
    with open('tasks.txt', 'r') as user_tasks:

        show_tasks = user_tasks.readlines()

    for i, t in enumerate(show_tasks):

        user_tasks_split = t.strip().split(";")

        if i == t:

            user_tasks_split[5] == 'Yes'




def generate_reports():

    with open('task_overview.txt', 'w+') as task_overview:

        with open('tasks.txt', 'r') as tasks_for_gr:

            all_tasks = tasks_for_gr.readlines()

            total_gen = len(all_tasks)

            str_total_gen = str(total_gen)

            task_overview.write("Tasks generated/tracked: " + str_total_gen + '\n')

            #str_tasks = str(all_tasks)



            num_comp_tasks = []

            for t in all_tasks:

                completed_tasks = t.strip().split(";")[-1]


                if completed_tasks == 'Yes':
                    num_comp_tasks.append('t')
                    num_comp_tasks_count = len(num_comp_tasks)
                    num_comp = str(num_comp_tasks_count)
                    task_overview.write(num_comp)





    with open('user_overview.txt', 'w+') as user_overview:

        with open('tasks.txt', 'r') as tasks_for_gr_user:

            with open('user.txt', 'r') as user_for_gr:

                all_users = user_for_gr.readlines()

                all_tasks = tasks_for_gr_user.readlines()

                total_reg = len(all_users)

                str_total_reg = str(total_reg)

                user_overview.write("Users Registered: " + str_total_reg + '\n')

                total_gen = len(all_tasks)

                str_total_gen = str(total_gen)

                user_overview.write("Tasks generated/tracked: " + str_total_gen + '\n')

                for t in all_tasks:

                    tasks_split = t.strip().split(";")

                    if tasks_split[0] == curr_user:

                        user_only = len(all_tasks)

                        str_user_only = str(user_only)

                        user_overview.write("Tasks assigned to user: " + str_user_only + '\n')

                        user_only_percentage = user_only / total_gen * 100

                        str_user_only_percentage = str(user_only_percentage)

                        user_overview.write("Percentage tasks assigned to user: " + str_user_only_percentage + '\n')















#edit task?
# Create tasks.txt if it doesn't exist
#if not os.path.exists("tasks.txt"):
#     with open("tasks.txt", "w") as default_file:
#         pass
#
# with open("tasks.txt", 'r') as task_file:
#     task_data = task_file.read().split("\n")
#     task_data = [t for t in task_data if t != ""]
#
#
# task_list = []
# for t_str in task_data:
#     curr_t = {}
#
#     # Split by semicolon and manually add each component
#     task_components = t_str.split(";")
#     curr_t['username'] = task_components[0]
#     curr_t['title'] = task_components[1]
#     curr_t['description'] = task_components[2]
#     curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
#     curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
#     curr_t['completed'] = True if task_components[5] == "Yes" else False
#
#     task_list.append(curr_t)



#====Login Section====
'''This code reads usernames and password from the user.txt file to
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.readlines()

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()


    if menu == 'r':
        '''Add a new user to the user.txt file'''

        reg_user()

    elif menu == 'a':

        add_task()

    elif menu == 'va':

        view_all()

    elif menu == 'vm':

        view_mine()



        with open('tasks.txt', 'r+') as tasks_file:





            q1 = input("Would you like to mark the task as complete? (Y/N:")

            if q1 == "Y":
                mark()




    elif menu == 'gr':
         generate_reports()






    
    elif menu == 'ds' and curr_user == 'admin':

        with open('tasks.txt', 'r') as tasks_file:

            with open('user.txt', 'r') as user_file:

                tasks = tasks_file.readlines()

                num_users = len(username_password.keys())
                num_tasks = len(tasks)

                print("-----------------------------------")
                print(f"Number of users: \t\t {num_users}")
                print(f"Number of tasks: \t\t {num_tasks}")
                print("-----------------------------------")



    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")