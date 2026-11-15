def remove_empty_tasks(tasks):
    """Return a new list of tasks with empty strings removed."""
    return [task for task in tasks if task != ""]


if __name__ == "__main__":
    print(remove_empty_tasks(["Study Python", "", "Practice", ""]))
    # ['Study Python', 'Practice']
