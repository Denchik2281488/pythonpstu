import json
import uuid

def load_tasks():
    """
    Функция загрузки списка задач из JSON-файла.

    Возвращает словарь, где ключом является идентификатор задачи, а значением - словарь с информацией о задаче.
    """

    try:
        with open("tasks.json", "r") as f:
           tasks = json.load(f)
    except FileNotFoundError:
        tasks = {}

    return tasks


def save_tasks(tasks):
    """
    Функция сохранения списка задач в JSON-файл.
    """

    with open("tasks.json", "w") as f:
        json.dump(tasks, f)


def get_input(str):
    """
    Функция получения пользовательского ввода.

    Возвращает строку, введенную пользователем.
    """

    print(str)
    return input()


def add_task(tasks):
    """
    Функция добавления новой задачи.

    Запрашивает у пользователя описание задачи и категорию задачи.
    """

    description = get_input("Описание задачи: ")
    category = get_input("Категория задачи: ")
    lee =  len(tasks)
    tasks[str(uuid.uuid4())] = {
        "description": description,
        "category": category,
        "completed": False,
    }


def mark_task_as_completed(tasks):
    """
    Функция отметки задачи выполненным.

    Запрашивает у пользователя идентификатор задачи.
    """

    task_id = str(get_input("Идентификатор задачи: "))
    try:
        if (tasks[str(task_id)]["completed"] != True):
            tasks[str(task_id)]["completed"] = True
        else:
            tasks[str(task_id)]["completed"] = False
    except KeyError:
        print("Такого идентификатора нет!")


def list_tasks(tasks):
    """
    Функция вывода списка задач.
    """
    complete ="" 
    for task_id, task in tasks.items():
        if(task['completed'] == False):

            print(f"{task_id:>40}  | {task['description']:<40} | {task['category']:<20} | [ ]")
        else:
             print(f"{task_id:>40}  | {task['description']:<40} | {task['category']:<20} | [X]")

def list_tasks_category(tasks):
    """
    Функция вывода списка задач.
    """
    category = get_input("Введите название категории: ")

    for task_id, task in tasks.items():
        if (task['category'] == category):
            if(task['completed'] == False):

                print(f"{task_id:>40}  | {task['description']:<40} | {task['category']:<20} | [ ]")
            else:
                print(f"{task_id:>40}  | {task['description']:<40} | {task['category']:<20} | [X]")

def list_tasks_search(tasks):
    """
    Функция вывода списка задач.
    """
    strsearch = get_input("Поиск: ")
    for task_id, task in tasks.items():
        if(strsearch in task['description']):
            if(task['completed'] == False):

                print(f"{task_id:>40}  | {task['description']:<40} | {task['category']:<20} | [ ]")
            else:
                print(f"{task_id:>40}  | {task['description']:<40} | {task['category']:<20} | [X]")



def main():
    tasks = load_tasks()

    while True:
        command = get_input("Введите команду:")

        if command == "add":
            add_task(tasks)
        elif command == "mark":
            mark_task_as_completed(tasks)
        elif command == "list":
            list_tasks(tasks)
        elif command == "category":
            list_tasks_category(tasks)
        elif command == "search":
            list_tasks_search(tasks)
        elif command == "exit":
            break

    save_tasks(tasks)


if __name__ == "__main__":
    main()