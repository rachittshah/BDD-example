from behave import given, when, then
from todo import ToDo

@given('an empty task list')
def step_given_an_empty_task_list(context):
    context.todo = ToDo()

@given('a task list with the task "{task}"')
def step_given_a_task_list_with_task(context, task):
    context.todo = ToDo()
    context.todo.add_task(task)

@when('I add the task "{task}"')
def step_when_I_add_task(context, task):
    context.todo.add_task(task)

@when('I mark the task "{task}" as complete')
def step_when_I_mark_task_as_complete(context, task):
    context.todo.mark_task_complete(task)

@then('the task list should contain {count:d} task')
def step_then_task_list_should_contain_count_tasks(context, count):
    assert len(context.todo.tasks) == count, f"Expected {count} task(s), but got {len(context.todo.tasks)}"

@then('the task "{task}" should be marked as complete')
def step_then_task_should_be_marked_as_complete(context, task):
    task_found = False
    for t, completed in context.todo.tasks.items():
        if t == task:
            task_found = True
            assert completed, f"Expected task '{task}' to be marked as complete, but it was not"
            break
    assert task_found, f"Task '{task}' not found"
