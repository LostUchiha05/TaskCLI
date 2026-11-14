<h1>🚀 Command Line Task Tracker</h1>
A simple, lightweight Command Line Interface (CLI) task manager built in Python using argparse and JSON for local data persistence.

<h2>📁 Project Structure</h2>h2>
taskTracker.py: Handles core backend logic (adding, deleting, updating, and filtering tasks, plus file I/O).   
todoCli.py: Handles the user interface via argparse, routing commands and arguments to the backend tracker.   
Something.json: Local database file where tasks are stored (automatically generated).

<h2>🛠️ Features </h2>
Add Tasks: Create new tasks with custom descriptions and progress statuses.   
todoCli.py

Delete Tasks: Remove tasks by ID with automatic ID re-indexing.   
taskTracker.py

Update Tasks: Modify existing task descriptions or progress states optionally.   
todoCli.py

List & Filter Tasks: View all tasks or filter them by ID and progress status.   
todoCli.py

<h2>⚙️ Installation & Setup</h2>
Clone the repository:
<b>Bash</b>
git clone https://github.com/your-username/task-tracker-cli.git
cd task-tracker-cli
Ensure you have Python 3 installed. No external dependencies or virtual environments are required.

<h3>📖 Usage Guide</h3>
Run the CLI using python todoCli.py followed by a subcommand:   
todoCli.py

1. Add a Task
Bash
python todoCli.py add "Finish my Python project" --Progress "Mark-in-progress"

3. List All Tasks
Bash
python todoCli.py list

5. Filter Tasks by ID or Progress
Bash
python todoCli.py list --id 1
python todoCli.py list --Progress "Mark-in-progress"

7. Update a Task
(You can update the description, the progress, or both)   
todoCli.py

Bash
python todoCli.py update 1 -D "Finish and test Python project" -P "Mark-in-done"

5. Delete a Task
Bash
python todoCli.py del 1

<h3>💡 Future Improvements</h3>
<ul>
<li>Add a clear command to wipe all tasks.</li>
<li>Implement task priorities (High, Medium, Low).</li>
<li>Add timestamps for completion tracking.</li>
</ul>

https://roadmap.sh/projects/task-tracker
<img src="Screenshot 2026-11-14 175247.jpg">
<img src="Screenshot 2026-11-14 175437.jpg">
