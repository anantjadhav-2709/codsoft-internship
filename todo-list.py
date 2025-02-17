class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'done': False})
        print(f"Added task: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "Done" if task['done'] else "Not Done"
                print(f"{idx}. {task['task']} [{status}]")

    def mark_as_done(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['done'] = True
            print(f"Marked task {task_number} as done.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"Deleted task: {deleted_task['task']}")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List:")
        todo_list.view_tasks()
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Done")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_number = int(input("Enter the task number to mark as done: "))
            todo_list.mark_as_done(task_number)
        elif choice == '3':
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
