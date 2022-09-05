tasks = []
task = {}
while True:
    task_number=input("Enter a task number,Enter Q to quit: ")
    if task_number.upper() == 'Q':
        break
    task_description=input("Enter task description: ")
    task_assignee=input("Enter task assignee: ")
    task['task_number'] = task_number
    task['task_description'] = task_description
    task['task_assignee'] = task_assignee
    # tasks.append(task.copy())
    tasks.append({'task_number': task_number, 
                  'task_description': task_description,
                  'task_assignee': task_assignee})
print(tasks)


def display_tasks(tasks):
    print(tasks)

display_tasks(tasks)