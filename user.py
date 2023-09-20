from PyInquirer import prompt
import csv
from csv import DictWriter
user_questions = [
    {
        'type': 'input',
        'name': 'name',
        'message': 'What\'s your name ? ',
    }
]

def add_user():
    name = prompt(user_questions)
    with open('users.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=name.keys())
        writer.writerow(name)
    f.close()
    # This function should create a new user, asking for its name
    return