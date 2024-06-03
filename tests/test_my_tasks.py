import pytest
from lib.my_tasks import * 

def test_my_tasks_with_none_value():
    with pytest.raises(Exception) as e:
        my_tasks(None)
    message = str(e.value)
    assert message == ('Task list cannot be None or empty')

def test_my_tasks_with_empty_list():
    with pytest.raises(Exception) as e:
        my_tasks([])
    message = str(e.value)
    assert message == ('Task list cannot be None or empty')

def test_my_tasks_task_to_do_one_task():
    task_list = ["#TODO washing"]
    assert my_tasks(task_list)== ["#TODO washing"]

def test_my_tasks_with_two_to_do_two_tasks():
    task_list = ["#TODO washing", "walking #TODO"]
    assert my_tasks(task_list) == ["#TODO washing", "walking #TODO"]

def test_my_tasks_with_no_to_do_tasks():
    with pytest.raises(Exception) as e:
        my_tasks(["feed the cat", "make dinner", "go to sleep early"])
    message = str(e.value)
    assert message == ('No #TODO tasks found')

def test_my_tasks_with_to_do_and_not_to_do_tasks():
    task_list = (["#TODO washing","make dinner","walking #TODO"])
    assert my_tasks(task_list) == ["#TODO washing","walking #TODO"]





