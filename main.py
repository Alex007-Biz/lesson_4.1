
class Task():
    def __init__(self, description, deadline, status):
        self.description = description
        self.deadline = deadline
        self.status = status
        self.tasks = []

    def add_task(self, description, deadline):
       new_task = Task(description, deadline)
       self.tasks.append(new_task)

    def mark_task_as_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = True
                break

    def print_current_tasks(self):
        print("Current tasks:")
        for task in self.tasks:
            if not task.status:
                print(f"Description: {task.description}, Deadline: {task.deadline}, Status: {'Done' if task.status else 'Not Done'}")

task = Task()
    task.add_task("Complete project report", "2022-10-15")
    task.add_task("Buy groceries", "2022-10-20")
    task.add_task("Exercise for 30 minutes", "2022-10-25")
task.mark_task_as_done("Buy groceries")
task.print_current_tasks()