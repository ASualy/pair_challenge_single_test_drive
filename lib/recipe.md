# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string `#TODO`.

We assume this is a list of text strings, some which will contain '#TODO' and some may not contain '#TODO' Any items which need be returned should contain the string exactly as '#TODO' and not 'Todo' or '#todo' or '#TOdo' etc. The list that is defined will not contain numbers or special characters.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def my_tasks():
    """ Extract items from a list which contain the string '#TODO' Assuming that the strings in the list which need to be extracted contains '#TODO' anywhere in the string

    Parameters: (list all parameters and their types)
        task_list: a string containing words (e.g. "#TODO the washing", "#TODO walking", 'feed the cat')

    Returns: (state the return value and its type)
        a list of strings, each one a word/task which starts with '#TODO' 

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given an empty list or None raises an Exception error
It returns a empty list  "" or None value 
"""
my_tasks_empty_list(None) => ["Task list cannot be None"]

"""
Given one item in a list with '#TODO' in the string
It returns the item which contains the string '#TODO'
"""
my_tasks_task_to_do_one_task("#TODO washing") => ["#TODO washing"]

"""
Given two items in a list with '#TODO' in the string

my_tasks_with_two_to_do_two_tasks("#TODO washing", "walking #TODO") => ["#TODO washing", "walking #TODO"]

"""

"""
Given a list that doesn't contain '#TODO' in the string
It returns an empty list
"""
my_tasks_with_no_to_do_tasks("feed the cat", "make dinner", "go to sleep early") => [""]

"""
Given a list with a mix of '#TODO' tasks and ones which don't contain '#TODO'
"""
my_tasks_with_to_do_and_not_to_do_tasks("#TODO washing","make dinner","walking #TODO") => ["#TODO washing","walking #TODO"]
"""

Given a list where the task does not contain the exact string "#TO drive to mum DO123"

my_tasks_with_not_the_exact_string("#TO drive to mum DO123","make dinner","#TODO washing") ==> ["#TODO washing"]

"""

"""
Given a list where the task contains '#TODO' as '#Todo'
my_tasks_with_todo_not_in_the_correct_format("#TODO washing","#Todo walk the dog", "walking #TODO") ==> [#TODO washing", "walking #TODO"]


"""

"""
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Ensure all test function names are unique, otherwise pytest will ignore them!
