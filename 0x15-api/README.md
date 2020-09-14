# Project 0x15 API

Use of APIs and Python scripts

Concepts:

    What Bash scripting should not be used for
    What is an API
    What is a REST API
    What are microservices
    What is the CSV format
    What is the JSON format
    Pythonic Package and module name style
    Pythonic Class name style
    Pythonic Variable name style
    Pythonic Function name style
    Pythonic Constant name style
    Significance of CapWords or CamelCase in Python

Content:

0-gather_data_from_an_API.py is a python script that using the REST API for a given employee ID, returns information about his/her TODO list progress.

1-export_to_CSV.py is a python script that does task 0 but export data in the CSV format 

2-export_to_JSON.py is a python script that does task 0 but export data in the JSON format 

3-dictionary_of_list_of_dictionaries.py is a python script that does task 0 but export data in the JSON format as example.
Example:

    Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
