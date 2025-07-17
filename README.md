# 📝 CLI Todo App

## 📌 Project Overview

A clean, lightweight command-line interface (CLI) Todo application built with Python following Clean Code principles.

## 🚀 Features

- Add new tasks
- List all tasks with status
- Mark tasks as complete
- Remove tasks
- Persistent storage using JSON file
- Robust error handling

## 🔧 Requirements

- Python 3.6 or higher
- No external dependencies required

## ⚙️ Setup and Installation

1. Clone this repository:

```bash
git clone https://github.com/anurag-adk/cli-todo.git
cd cli-todo
```

2. Run using Python:

```bash
python main.py <command> [arguments]
```

### 🎯 Commands

| Command              | Description           | Example                                    |
| -------------------- | --------------------- | ------------------------------------------ |
| `add <task_details>` | Add a new task        | `python main.py add "Complete Assignment"` |
| `list`               | Display all tasks     | `python main.py list`                      |
| `complete <task_id>` | Mark task as complete | `python main.py complete 1`                |
| `remove <task_id>`   | Remove a task         | `python main.py remove 2`                  |
| `help`               | Show help message     | `python main.py help`                      |

## 💡 Example Usage

### Adding Tasks

```bash
$ python main.py add "Complete LSPP Assignment"
Task added: "Complete LSPP Assignment"

$ python main.py add "Drink 2lt of water"
Task added: "Drink 2lt of water"

$ python main.py add "Read a book"
Task added: "Read a book"
```

### Listing Tasks

```bash
$ python main.py list

------------------------------
TODO LIST
------------------------------

Your tasks:
  1. [x] Complete LSPP Assignment
  2. [○] Drink 2lt of water
  3. [○] Read a book
```

### Completing Tasks

```bash
$ python main.py complete 3
Task completed: "Read a book"
```

### Removing Tasks

```bash
$ python main.py remove 3
Task removed: "Read a book"
```

### Error Handling

```bash
$ python main.py complete
Error 400: Task ID is required
Usage: python main.py complete <task id>

$ python main.py complete abc
Error 400: Task ID must be a positive number

$ python main.py complete 9999
Error 400: Task with ID 9999 not found
```

## 📂 File Structure

<pre>📁 cli-todo/
├── main.py
├── todo.py
├── todo_data.json
└── README.md
</pre>

## 🧹 Clean Code Principles Applied

### 1. Single Responsibility Principle (SRP)

- **`TodoApp`**: Manages todo operations
- **`validate_task_id()`**: Handles task ID validation
- **`find_task_by_id()`**: Locates tasks by ID
- **`load_tasks()`** / **`save_tasks()`**: Handle file I/O

### 2. Don't Repeat Yourself (DRY)

- Extracted `validate_task_id()` to eliminate duplicate validation logic
- Centralized error handling in `find_task_by_id()`
- Reusable methods for common operations

### 3. Meaningful Names

```python
def validate_task_id() -> Optional[int]:     # Clear purpose
def find_task_by_id(task_id: int):           # Descriptive function name
self.next_id                                 # Self-documenting variable
```

### 4. Small, Focused Functions

Each function has a single, clear responsibility:

- `add_task()`: Only adds tasks
- `complete_task()`: Only marks tasks complete
- `validate_task_id()`: Only validates IDs

### 5. Error Handling

- User-friendly error messages
- Input validation with helpful feedback
- Consistent error format (`Error 400: ...`)

### 6. Consistent Formatting

- Consistent indentation (4 spaces)
- Clear method organization
- Type hints for better code documentation
- Meaningful comments where needed

## 🙏 Thank You

_A Special Thank You To Our Mentors and Facilitators at Leapfrog especially Dilip Gautam dai_
