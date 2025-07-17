# imports
import sys
import json
from typing import List, Dict, Any, Optional

class TodoApp:
    # constructor to initialize the app
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
                status_icon = "x" if task['completed'] else "o"
                print(f"{task['id']}. [{status_icon}] {task['description']}")

    def add_task(self, description: str) -> None:
        # arg: description is the task description
        
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

    def complete_task(self, task_id: int) -> None:
        # arg: task_id is the id of task to mark as completed

        task = self.find_task_by_id(task_id)
        if not task: return
        task['completed'] = True
        self.save_tasks()
        
        print(f"Task completed: \"{task['description']}\"")

    def remove_task(self, task_id: int) -> None:
        # arg: task_id is the id of task to be removed

        task = self.find_task_by_id(task_id)
        if not task: return
        self.tasks.remove(task)
        self.save_tasks()
        
        print(f"Task removed: \"{task['description']}\"")

    # display the cli commands 
    def show_help(self) -> None:
        print("""
Usage: python todo.py [command] [arguments]

Commands:
  add <task>        Add a new task
  list              List all tasks
  complete <id>     Mark task as complete
  remove <id>       Remove a task
  help              Show help message

Examples:
  python main.py add "Complete LSPP Assignment"
  python main.py list
  python main.py complete 1
  python main.py remove 2
""")

    # run the cli app
    def run(self) -> None:
        # print("cli app is running ...") 
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

        elif command == "complete":
            task_id = self.validate_task_id()
            if task_id is not None:
                self.complete_task(task_id)

        elif command == "remove":
            task_id = self.validate_task_id()
            if task_id is not None:
                self.remove_task(task_id)
        
        elif command == "help":
            self.show_help()

        else:
            print(f"Error 400: Unknown command: {command}")
            print('Run "python main.py help" for available commands.')

    def find_task_by_id(self, task_id: int) -> Optional[Dict[str, Any]]:
        # arg: task_id is the id of task to find
        # return: task dictionary if found else return None

        for task in self.tasks:
            if task['id'] == task_id:
                return task
        print(f"Error 400: Task with ID {task_id} not found")
        return None
    
    def validate_task_id(self) -> Optional[int]:
        # return: task_id if valid else return None
        if len(self.args) < 2: 
            print("Error 400: Task ID is required")
            print("Usage: python main.py <command> <task id>")
            return None
        else:       
            try:
                task_id = int(self.args[1])
                if task_id <= 0:
                    print("Error 400: Task ID must be a positive number")
                    return None
                return task_id
            
            except ValueError:
                print("Error 400: Task ID must be a positive number")
                return None