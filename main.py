from textual.app import ComposeResult, on
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Input, Static, RichLog
from textual.app import App
from datetime import datetime


class TaskManager(App):
    """A simple task manager TUI application."""

    CSS = """
    Screen {
        layout: vertical;
        background: $surface;
    }

    #header {
        dock: top;
        height: 3;
        background: $boost;
        color: $text;
        border: solid $primary;
        text-align: center;
        content-align: center middle;
    }

    #tasks-container {
        height: 1fr;
        border: solid $primary;
        background: $panel;
    }

    #input-container {
        dock: bottom;
        height: auto;
        background: $boost;
        border: solid $primary;
    }

    #add-row {
        layout: horizontal;
        height: auto;
    }

    #delete-row {
        layout: horizontal;
        height: auto;
    }

    Input {
        margin: 1 1;
        width: 1fr;
    }

    Button {
        margin: 1 0;
    }

    RichLog {
        margin: 1 2;
    }
    """

    def __init__(self):
        super().__init__()
        self.tasks = []

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Static("✓ Task Manager", id="header")

        with Vertical(id="tasks-container"):
            yield RichLog(id="task-log", markup=True)

        with Vertical(id="input-container"):
            with Horizontal(id="add-row"):
                yield Input(
                    placeholder="Enter a new task...",
                    id="task-input",
                )
                yield Button("Add", id="add-btn", variant="primary")

            with Horizontal(id="delete-row"):
                yield Input(
                    placeholder="Task number to delete...",
                    id="delete-input",
                )
                yield Button("Delete", id="delete-btn", variant="warning")
                yield Button("Export", id="export-btn", variant="success")
                yield Button("Clear All", id="clear-btn", variant="error")

    def on_mount(self) -> None:
        """Called when the app is mounted."""
        self.query_one("#task-input", Input).focus()

    @on(Button.Pressed, "#add-btn")
    def add_task(self) -> None:
        """Add a new task."""
        input_widget = self.query_one("#task-input", Input)
        task_text = input_widget.value.strip()

        if task_text:
            self.tasks.append(task_text)
            self.update_task_list()
            input_widget.value = ""
            input_widget.focus()

    @on(Button.Pressed, "#clear-btn")
    def clear_all(self) -> None:
        """Clear all tasks."""
        self.tasks.clear()
        self.update_task_list()

    @on(Button.Pressed, "#delete-btn")
    def delete_task(self) -> None:
        """Delete a specific task by number."""
        delete_input = self.query_one("#delete-input", Input)
        try:
            task_num = int(delete_input.value.strip())
            if 1 <= task_num <= len(self.tasks):
                self.tasks.pop(task_num - 1)
                self.update_task_list()
                delete_input.value = ""
            else:
                self.notify(f"Task number must be between 1 and {len(self.tasks)}", severity="error")
        except ValueError:
            self.notify("Please enter a valid number", severity="error")
        delete_input.focus()

    @on(Input.Submitted, "#delete-input")
    def on_delete_submitted(self) -> None:
        """Handle Enter key in delete input."""
        self.delete_task()

    @on(Button.Pressed, "#export-btn")
    def export_tasks(self) -> None:
        """Export tasks to a text file."""
        if not self.tasks:
            self.notify("No tasks to export", severity="warning")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"tasks_{timestamp}.txt"

        try:
            with open(filename, "w") as f:
                f.write("=== TASK LIST ===\n")
                f.write(f"Exported: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                for idx, task in enumerate(self.tasks, 1):
                    f.write(f"{idx}. {task}\n")

            self.notify(f"Tasks exported to {filename}", severity="information")
        except IOError as e:
            self.notify(f"Error exporting tasks: {e}", severity="error")

    @on(Input.Submitted, "#task-input")
    def on_input_submitted(self) -> None:
        """Handle Enter key in input."""
        self.add_task()

    def update_task_list(self) -> None:
        """Update the displayed task list."""
        task_log = self.query_one("#task-log", RichLog)
        task_log.clear()

        if not self.tasks:
            task_log.write("[dim]No tasks yet. Add one to get started![/dim]")
        else:
            for idx, task in enumerate(self.tasks, 1):
                task_log.write(f"[cyan]{idx}.[/cyan] {task}")


if __name__ == "__main__":
    app = TaskManager()
    app.run()

