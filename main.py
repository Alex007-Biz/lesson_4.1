class Task():
    def __init__(self, description, deadline, status):
        self.description = description
        self.deadline = deadline
        self.status = status
        self.tasks = []

    def add_task(self, description, deadline):
        new_task = Task(description, deadline, self.status)
        self.tasks.append(new_task)

    def mark_task_as_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = True
                break

    def print_current_tasks(self):
        print("Current tasks:")
        for task in self.tasks:
            print(f"Описание: {task.description}, Дата выполнения: {task.deadline}, Статус: {'Выполнено' if task.status else 'Не выполнено'}")


task1 = Task("Задача1", "2024-04-01", False)

task1.add_task("Выполнить проект №1", "15.10.2024")
task1.add_task("Buy groceries", "20.10.2024")
task1.add_task("Задача на 30 минут", "25.05.2024")
task1.print_current_tasks()

task1.mark_task_as_done("Buy groceries")
task1.print_current_tasks()


