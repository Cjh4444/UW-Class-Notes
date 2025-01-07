import os
import re

# Directory containing the files
directory = '/Users/camdencambre/UW Class Notes/notes'

# Initialize an empty list to store uncompleted tasks from all files
all_uncompleted_tasks = []

# Process each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.md') and not filename.startswith('template'):
        filepath = os.path.join(directory, filename)
        
        with open(filepath, 'r') as file:
            content = file.read()

        # Extract the Todo section
        todo_section = re.search(r'## Todo:(.*?)(##|$)', content, re.DOTALL)

        if todo_section:
            # Get the content of the Todo section
            todo_content = todo_section.group(1)

            # Find all tasks without an 'x' in the brackets
            tasks = re.findall(r'- \[ \] (.+)', todo_content)

            # Add the uncompleted tasks to the list
            all_uncompleted_tasks.extend([(filename, task) for task in tasks])

# Print all uncompleted tasks with their filenames

print("HAVE DUE DATES (likely soon)")
for filename, task in all_uncompleted_tasks:
    if "due" in task.lower(): print(f'{filename}: {task}')

print("MISC")
for filename, task in all_uncompleted_tasks:
    if "due" not in task.lower(): print(f'{filename}: {task}')