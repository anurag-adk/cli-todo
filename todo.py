# imports
import sys
import json
from typing import List, Dict, Any, Optional

class TodoApp:
    # define constructor to initialize the app
    def __init__(self):
        self.file_name = "todo_data.json"
        self.tasks: List[Dict[str, Any]] = []
        self.task_id = 1
        self.load_tasks()
        self.args = sys.argv[1:]

    def load_tasks(self) -> None:
        pass

    # write tasks into JSON file
    def save_tasks(self) -> None:
        try:
            with open(self.file_name, "a") as file:
                json.dump(self.tasks, file, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def list_tasks(self) -> None:
        pass

    def find_task_by_id(self, task_id: int) -> Optional[Dict[str, Any]]:
        pass
    
    # arg: description is the task description
    def add_task(self, description: str) -> None:
        # no need to validate description since we have handled it at run time

        # if not description.strip():
        #     print("Error 400: Task description cannot be empty")
        #     return
        
        task = {
            'id': self.task_id,
            'description': description.strip(),
            'completed': False
        }
        
        self.tasks.append(task)
        self.task_id += 1
        self.save_tasks()
        
        print(f"Task added: \"{task['description']}\"")

    def complete_task(self, task_id: int) -> None:
        pass

    def remove_task(self, task_id: int) -> None:
        pass

    # display the cli commands 
    def show_help(self) -> None:
        pass

    # run the cli app
    def run(self) -> None:
        print("cli app is running ...") 
        command = self.args[0].lower()

        if command == "add":
            if len(self.args) < 2:
                print("Error 400: Task description cannot be empty")
                print("Usage: python main.py add <task description>")
            else:
                task_description = " ".join(self.args[1:])
                self.add_task(task_description)
            
