def my_tasks(task_list):
    if task_list is None or task_list==[]:
        raise Exception('Task list cannot be None or empty')
    if not [task for task in task_list if '#TODO' in task]:
        raise Exception('No #TODO tasks found')
    else:
        return task_list
