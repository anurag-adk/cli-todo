# imports
import sys
from typing import List, Dict, Any, Optional

class TodoApp:
    # define constructor to initialize the app
    def __init__(self):
        self.file_path = "todo_data.json"
        self.tasks: List[Dict[str, Any]] = []
        self.next_id = 1
        self.load_tasks()
        self.args = sys.argv[1:]

    # load tasks from the JSON file 
    def load_tasks(self) -> None:
        pass

    # save tasks to the JSON file
    def save_tasks(self) -> None:
        pass

    def list_tasks(self) -> None:
        pass

    def find_task_by_id(self, task_id: int) -> Optional[Dict[str, Any]]:
        pass
    
    def add_task(self, description: str) -> None:
        pass

    # mark a task as completed by its ID
    def complete_task(self, task_id: int) -> None:
        pass

    # remove a task by its ID
    def remove_task(self, task_id: int) -> None:
        pass

    # display the cli commands 
    def show_help(self) -> None:
        pass


    # run the cli app
    def run(self) -> None:
        print(f"CLI app is up and running")
