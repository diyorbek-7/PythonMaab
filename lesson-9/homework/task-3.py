import json
import csv

# Load tasks from JSON file
def load_tasks(filename="tasks.json"):
    with open(filename, "r") as file:
        return json.load(file)

# Display tasks
def display_tasks(tasks):
    print("\nTasks:")
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

# Calculate task statistics
def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(task["completed"] for task in tasks)
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task["priority"] for task in tasks) / total_tasks if total_tasks else 0

    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {avg_priority:.2f}")

# Save tasks to JSON file
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

# Convert JSON to CSV
def convert_to_csv(tasks, filename="tasks.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
    print(f"\nTasks saved to {filename}")

# Main execution
if __name__ == "__main__":
    tasks = load_tasks()
    display_tasks(tasks)
    calculate_stats(tasks)
    save_tasks(tasks)  # Save any modifications if needed
    convert_to_csv(tasks)
