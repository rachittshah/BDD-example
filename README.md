
# ToDo List Application with Behave BDD

This is a simple example of a text-based ToDo List application developed using Python and tested with the Behave BDD framework.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python 3.6 or higher
- Pip (Python package manager)

### Installation

1. Clone the repository

2. Install the required dependencies: ```pip3 install behave```

### Running the tests

To run the BDD tests using Behave, navigate to the project's root directory (`todo_app`) and execute the following command:

```behave```

The test results will be displayed on the console. If everything is set up correctly, you should see all the scenarios and steps passing.

## Project Structure

The project is organized as follows:

- `todo.py`: The main application file containing the ToDo List implementation.
- `features/`: The directory containing the Behave feature files and step definitions.
  - `todo.feature`: The feature file containing the scenarios and steps for the ToDo List application.
  - `steps/`: The directory containing the step definition files.
    - `todo_steps.py`: The step definitions for the `todo.feature` file.

## Built With

- [Python](https://www.python.org/) - The programming language used.
- [Behave](https://behave.readthedocs.io/en/latest/) - The BDD framework used for testing.


