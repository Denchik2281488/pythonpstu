import json
import uuid

def load_tasks():
    """
    Функция загрузки бюджета из JSON-файла.

    Возвращает словарь, где ключом является идентификатор задачи, а значением - словарь с информацией о задаче.
    """

    try:
        with open("budget.json", "r") as f:
           tasks = json.load(f)
    except FileNotFoundError:
        tasks = {}

    return tasks


def save_tasks(tasks):
    """
    Функция сохранения бюджета в JSON-файл.
    """

    with open("budget.json", "w") as f:
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
    Функция добавления новой покупки.

    Запрашивает у пользователя описание покупки и котегорию.
    """

    description = get_input("Описание транзакции: ")
    category = get_input("Категория транзакции: ")
    while(True):
        try:
            summ = float(get_input("Сумма: "))
            break
        except ValueError:
            print("Введите число!")
    lee =  len(tasks)
    tasks[str(uuid.uuid4())] = {
        "description": description,
        "category": category,
        "summ": summ
    }



def list_tasks(tasks):
    """
    Функция вывода бюджета.
    """
    complete ="" 
    for transaction_id, task in tasks.items():
        print(f"{transaction_id:>40}  | {task['description']:<40} | {task['category']:<20} | {task['summ']:<20}")


def list_tasks_category(tasks):
    """
    Функция вывода списка задач.
    """
    summ =0
    category = get_input("Введите название категории: ")
    if (category != ""):
        for transaction_id, task in tasks.items():
            if (task['category'].lower() == category.lower()):
                summ += float(tasks[transaction_id]['summ'])
        print(f"{category}  {summ}")







def main():
    tasks = load_tasks()

    while True:
        command = get_input("Введите команду:")

        if command == "add":
            add_task(tasks)
        elif command == "list":
            list_tasks(tasks)
        elif command == "category":
            list_tasks_category(tasks)
        elif command == "exit":
            break

    save_tasks(tasks)
    

if __name__ == "__main__":
    main()