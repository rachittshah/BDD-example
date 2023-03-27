Feature: ToDo application
  As a user
  I want to be able to add tasks and mark them as complete
  So that I can keep track of my tasks

  Scenario: Add a task
    Given an empty task list
    When I add the task "Buy groceries"
    Then the task list should contain 1 task

  Scenario: Mark a task as complete
    Given a task list with the task "Buy groceries"
    When I mark the task "Buy groceries" as complete
    Then the task "Buy groceries" should be marked as complete
