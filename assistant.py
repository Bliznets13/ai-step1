import json, os, datetime  # (набор готовых «ящиков с инструментами»: сохранение, время)

TASKS_FILE = "tasks.json"  # (имя файла, куда будем складывать задачи — как «тетрадь»)

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def show_menu():
    print("\n=== Консольный помощник ===")
    print("1) Приветствие")
    print("2) Текущее время")
    print("3) Показать задачи")
    print("4) Добавить задачу")
    print("5) Удалить задачу")
    print("0) Выход")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Ваш выбор: ").strip()
        if choice == "1":
            name = input("Как вас зовут? ")
            print(f"Привет, {name}!")
        elif choice == "2":
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Сейчас: {now}")
        elif choice == "3":
            if not tasks:
                print("Список задач пуст.")
            else:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
        elif choice == "4":
            t = input("Введите текст задачи: ").strip()
            if t:
                tasks.append(t)
                save_tasks(tasks)
                print("✅ Задача добавлена.")
        elif choice == "5":
            if not tasks:
                print("Удалять нечего.")
            else:
                idx = input("Номер задачи для удаления: ").strip()
                if idx.isdigit() and 1 <= int(idx) <= len(tasks):
                    removed = tasks.pop(int(idx)-1)
                    save_tasks(tasks)
                    print(f"🗑️ Удалено: {removed}")
                else:
                    print("Неверный номер.")
        elif choice == "0":
            print("Пока!")
            break
        else:
            print("Неизвестная команда.")

if __name__ == "__main__":
    main()
