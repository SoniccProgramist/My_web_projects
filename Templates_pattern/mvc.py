class TODOListModel:
    def __init__(self):
        self._tasks = []

    @property
    def tasks(self):
        return self._tasks

    def create_tasks(self, task:str):
        new_task = {"title": task, "is_completed": False}
        self.tasks.append(new_task)

    def complete_tasks(self, index:int):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["is_completed"] = True

    def remove_tasks(self, index:int):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

class TODOListView:

    def display_tasks(self, tasks:list):
        print("TODOList\n")
        if not tasks:
            print("Empty list")
        else:
            for i, task in enumerate(tasks):
                if task['is_completed']:
                    status = "[✅]"
                else:
                    status = "[ ]"
                print(f"{i+1}, {status} | {task['title']}", end="\n=======================\n")
            print("===========================")

    def display_message(self, message:str):
        print(f"Message: {message}")

class TODOListController:
    def __init__(self, model:TODOListModel, view:TODOListView):
        self.model = model
        self._view = view

    def update_view(self):
        self._view.display_tasks(self.model.tasks)

    def add_new_task(self, task_name:str):
        self.model.create_tasks(task_name)
        self._view.display_message(f"Added task")
        self.update_view()

    def complete_existing_task(self, index:int):
        self.model.complete_tasks(index-1)
        self._view.display_message(f"Completed task {index}")
        self.update_view()

    def remove_existing_task(self, index:int):
        self.model.remove_tasks(index-1)
        self._view.display_message(f"Removed task {index}")
        self.update_view()

if __name__ == "__main__":
    todo_model = TODOListModel()
    todo_view = TODOListView()
    todo_controller = TODOListController(todo_model, todo_view)
    todo_controller.update_view()
    todo_controller.add_new_task("Buy bread")
    todo_controller.add_new_task("Have rest")
    todo_controller.complete_existing_task(2)
    todo_controller.remove_existing_task(1)
