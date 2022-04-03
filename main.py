from os import getcwd, path


def menu():
    print('Just type some text to add new task. '
          'Type "show", "clear" to show or clear all tasks accordingly. '
          'Start your command with "del" to delete some tasks')


def prep_list_for_deleting(content_list):

    intersect_list = []
    content_set = set(content_list)

    for todo in todo_list:
        todo_set = set(todo.split())
        if content_set & todo_set == set():
            continue
        else:
            intersect_list.append(todo)

    dict_for_deleting = {ind: item for ind, item in enumerate(sorted(set(intersect_list)), 1)}

    if len(dict_for_deleting) < 1:
        print('No tasks found to delete')
        menu()
    else:
        print_deleting_tasks(dict_for_deleting)


def print_deleting_tasks(dct):

    for key, value in dct.items():
        print(f'{key} - {value}')

    cmd = input('Type comma-separated tasks to delete' + '\n')
    indexes = [int(symb) for symb in filter(lambda x: x.isdigit() and 1 <= int(x) <= len(dct.keys()), cmd.split(','))]
    lst = []

    for index in indexes:
        lst.append(dct[index])

    del_tasks(lst)


def del_tasks(lst_del):
    for task in lst_del:
        for _ in todo_list:
            todo_list.remove(task)
            break
    show()


def add_task(str_add):
    print(f'New task - {str_add}')
    todo_list.append(str_add)


def del_all_tasks(*args):
    todo_list.clear()
    show()


def show(*args):
    if len(todo_list):
        print('Your tasks:')
        for ind, item in enumerate(todo_list, 1):
            print(f'{ind}) - {item}')
    else:
        print("There are no tasks")


def tasks():
    if path.isfile(path_to_tasks):
        with open(path_to_tasks) as f:
            tasks_list = [task.strip() for task in f.readlines()]
    else:
        tasks_list = []
        with open(path_to_tasks, 'w') as f:
            f.write('')
    return tasks_list


def record_new_tasks_to_file():
    with open(path_to_tasks, 'w') as f:
        todo_str = '\n'.join(todo_list)
        f.writelines(todo_str)


path_to_tasks = getcwd() + '/tasks.txt'

command_dict = {
    'show': show,
    'clear': del_all_tasks,
    'del': prep_list_for_deleting,
}


todo_list = tasks()

show()
menu()

while True:
    print()

    command = input('Enter your command' + '\n')
    if len(command.split()) == 0:
        continue
    else:
        indicator = command.split()[0]
        content = command.split()[1:]
        if indicator.lower() in ('show', 'clear', 'del'):
            command_dict[indicator.lower()](content)
        elif indicator.lower() == 'x':
            record_new_tasks_to_file()
            print('Bye')
            break
        else:
            add_task(command)
