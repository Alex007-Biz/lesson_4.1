class Task():
    def __init__(self):
        self.tasks = []
    def add_task(self, description, deadline):
               self.tasks.append({"description": description, "deadline": deadline, "status": "не выполнено"})

    def mark_task_as_done(self, description):
        for task in self.tasks:
            if task["description"] == description:
                task["status"] = "Выполнено"
                print(f"Задача {description} не найдена")
            else:
                print(f"Задача {description} не найдена")

    def print_current_tasks(self):
        print("текущие задачи:")
        for task in self.tasks:
            if task["status"] == "не выполнено":
                print(f"{task['description']} - {task['deadline']}")


task1 = Task()
task1.add_task(description="прочитать книгу", deadline="01.06.2024")
task1.add_task(description="Пробежать марафон", deadline="05.06.2024")
task1.add_task(description="Починить машину", deadline="27.06.2024")

task1.mark_task_as_done("прочитать книгу")

task1.print_current_tasks()



