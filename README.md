# Task Manager TUI

A modern, interactive terminal user interface (TUI) task manager built with Python and [Textual](https://textual.textualize.io/).

## Overview

Task Manager is a lightweight command-line application that allows you to efficiently manage your tasks directly from the terminal. With a clean, intuitive interface, you can add, delete, clear, and export tasks without leaving your terminal.

## Features

- ✅ **Add Tasks** - Create new tasks with a simple input field
- 🗑️ **Delete Tasks** - Remove individual tasks by their number
- 🧹 **Clear All** - Remove all tasks at once
- 💾 **Export Tasks** - Save your task list to a timestamped text file
- 🎨 **Beautiful UI** - Color-coded interface with intuitive layout
- ⌨️ **Keyboard Friendly** - Full keyboard navigation and Enter key support

## Requirements

- Python 3.12 or higher
- `textual` (Terminal User Interface framework)

## Installation

### Using uv (Recommended)

```bash
cd task_manager
uv sync
```

### Using pip

```bash
pip install textual
```

## Usage

### Running the Application

```bash
# Activate the virtual environment
source .venv/bin/activate

# Run the app
python main.py
```

### Interface Guide

The application is divided into three main sections:

**Header** - Displays the application title "✓ Task Manager"

**Task List** - Shows all your current tasks numbered sequentially

**Input Area** - Contains two rows of controls:

1. **Add Task Row**
   - Input field for entering new task text
   - "Add" button to submit the task
   - Press Enter to add a task

2. **Delete/Control Row**
   - Input field for task number to delete (1-indexed)
   - "Delete" button to remove the selected task
   - "Export" button to save tasks to file
   - "Clear All" button to remove all tasks

### Keyboard Shortcuts

- **Enter** in task input field → Add new task
- **Enter** in delete input field → Delete task
- **Tab** → Navigate between input fields and buttons
- **Mouse clicks** → Activate buttons and focus fields

## Examples

### Adding a Task

1. Focus on the task input field (default focus on startup)
2. Type your task: `Buy groceries`
3. Press Enter or click "Add"

### Deleting a Task

1. Click the delete input field
2. Enter the task number: `1`
3. Press Enter or click "Delete"

### Exporting Tasks

1. Click the "Export" button
2. Your tasks will be saved to `tasks_YYYYMMDD_HHMMSS.txt`

## Project Structure

```
task_manager/
├── main.py              # Main application code
├── pyproject.toml       # Project configuration
├── README.md            # This file
├── .venv/               # Virtual environment
├── .python-version      # Python version specification
├── uv.lock              # Dependency lock file
└── .git/                # Git repository
```

## Development

The application is built with the Textual framework, which provides:

- Reactive widgets (Input, Button, RichLog)
- CSS-based styling
- Event-driven architecture
- Cross-platform terminal support

### Key Components

- **TaskManager class** - Main application class extending `textual.app.App`
- **Task storage** - In-memory list (`self.tasks`)
- **Task display** - `RichLog` widget for formatted output
- **Export functionality** - Generates timestamped text files

## Notes

- Tasks are stored in memory only and will be lost when you exit the application
- Task numbers are 1-indexed (first task is #1)
- Export files are created in the current working directory
- The interface uses a responsive layout that adapts to terminal size

## License

This project is provided as-is for personal and educational use.
