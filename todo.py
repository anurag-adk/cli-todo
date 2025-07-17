# imports
import sys
import json
from typing import List, Dict, Any, Optional

class TodoApp:
    # define constructor to initialize the app
    def __init__(self):
        self.file_name = "todo_data.json"
        self.tasks: List[Dict[str, Any]] = []
        self.next_id = 1
        self.load_tasks()
        self.args = sys.argv[1:]

    # read tasks from JSON file
    def load_tasks(self) -> None:
        try:
            with open(self.file_name, 'r') as file:
                self.tasks = json.load(file)
                if self.tasks:
                    self.next_id = max(task['id'] for task in self.tasks) + 1
        except Exception as e:
            print(f"Error loading tasks: {e}")

    # write tasks into JSON file
    def save_tasks(self) -> None:
        try:
            with open(self.file_name, "w") as file:
                # we are using "w" mode instead of "a" since we are loading the file beforehand and we need to overwrite to avoid duplicates
                json.dump(self.tasks, file, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def list_tasks(self) -> None:
        print("\n" + "-" * 30)
        print("TODO LIST")
        print("-" * 30)
        
        if not self.tasks:
            print("\nNo tasks found. Add a task to get started!")
        else:
            print("\nYour tasks:")
            for task in self.tasks:
                status_icon = "✓" if task['completed'] else "○"
                print(f"{task['id']}. [{status_icon}] {task['description']}")

    def find_task_by_id(self, next_id: int) -> Optional[Dict[str, Any]]:
        pass
    
    # arg: description is the task description
    def add_task(self, description: str) -> None:
        # no need to validate description since we have handled it at run time

        # if not description.strip():
        #     print("Error 400: Task description cannot be empty")
        #     return
        
        task = {
            'id': self.next_id,
            'description': description.strip(),
            'completed': False
        }
        
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        
        print(f"Task added: \"{task['description']}\"")

    def complete_task(self, next_id: int) -> None:
        pass

    def remove_task(self, next_id: int) -> None:
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
                # print(f"{task_description}")
                self.add_task(task_description)

        elif command == "list":
            self.list_tasks()
