# To do app, user is able to add, delete, and update tasks


# main run function
def run_app():
    app_running = True
    todolist = []
    print('Welcome to the ToDo App.')

    while app_running:
        count = 0
        menu = []

        if todolist:
            for task in todolist:
                count += 1
                menu.append(str(count) + ' ' + task)

        print('1: View your list.')
        print('2: Add a task.')
        print('3: Edit a task.')
        print('4: Delete a task.')
        print('5: Clear your list.')
        print('6: Quit')
        option = input('What would you like to do?: ')
        if option == '1':
            if len(todolist) > 0:
                print(todolist)
            else:
                print('You do not have any items in your list.')
            continue
        elif option == '2':
            add_task(todolist)
            continue
        elif option == '3':
            edit_task(menu, todolist)
            continue
        elif option == '4':
            delete_task(menu, todolist)
            continue
        elif option == '5':
            clear_task(todolist)
            continue
        elif option == '6':
            confirm = input('Are you sure you wish to quit? Y or N')
            if confirm.lower() == 'y':
                app_running = False
                print('Thanks! See you again soon!')
                break
            else:
                continue
        else:
            print('You have entered an invalid response. Please try again.')
            continue


def add_task(task_list):
    tasktodo = input('Please enter a task: ')
    print('You have entered the following task: ' + tasktodo)
    confirmtodo = input('Is this the task you want to add? Y or N?')

    if confirmtodo[0].lower() == 'y':
        item = tasktodo
        task_list.append(item)
        print('Item added!')
        print(task_list)
    else:
        print('Add cancelled.')


def edit_task(menu, task_list):
    if len(task_list) > 0:
        print(menu)

        task_to_update = input('Please enter the number of the item you want to change: ')
        for index, task in enumerate(task_list):
            try:
                int(task_to_update)
            except Exception as e:
                print('You\'ve entered an invalid response. Please try again.')
                continue
            if int(task_to_update) > len(task_list):
                print('That number is invalid.')
                continue
            elif int(task_to_update) == index + 1:
                update = input('Enter your edits: ')
                print(update)
                confirm = input('Do you want to commit your changes? Y or N')
                if confirm.lower() == 'y':
                    task_list.remove(task)
                    task_list.append(update)
                    print('Changes saved successfully.')
                    print(task_list)
                    break
                elif confirm.lower() == 'n':
                    print('Changes cancelled.')
                    continue
                else:
                    print('You have entered an invalid response. Please try again.')
                    continue

    else:
        print('You do not have any items in your list.')


def delete_task(menu, task_list):
    if len(task_list) > 0:
        print(menu)

        task_to_delete = input('Please enter the number of the item you want to delete: ')
        for index, task in enumerate(task_list):
            try:
                int(task_to_delete)
            except Exception as e:
                print('You\'ve entered an invalid response. Please try again.')
                continue
            if int(task_to_delete) > len(task_list):
                print('That number is invalid.')
                continue
            elif int(task_to_delete) == index + 1:
                print(task)
                confirm = input('Is this the task you want to delete? Y or N')
                if confirm.lower() == 'y':
                    task_list.remove(task)
                    print('Changes saved successfully.')
                    print(task_list)
                    break
                elif confirm.lower() == 'n':
                    print('Changes cancelled.')
                    continue
                else:
                    print('You have entered an invalid response. Please try again.')
                    continue

    else:
        print('You do not have any items in your list.')


def clear_task(task_list):
    if len(task_list) > 0:
        confirm = input('Are you sure you want to clear your list? Y or N')
        if confirm.lower() == 'y':
            task_list.clear()
        else:
            print('Request has been cancelled.')
    else:
        print('You do not have any items in your list.')


run_app()
