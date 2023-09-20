from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    }

]





def new_expense(*args):
    infos = prompt(expense_questions)

    file = open("users.csv", "r")

    users_list = []
    data_users = list(csv.reader(file))
    for users in data_users:
        users_list.append(users[0])

    choose_spender = [
        {
            "type":"list",
            "name":"spender",
            "message":"New Expense - Spender: ",
            "choices": users_list
        }
    ]

    spender = prompt(choose_spender)
    infos["spender"] = spender["spender"]
    users_list.remove(infos["spender"])
    users_list_dict = []
    for user in users_list:
        users_list_dict.append({"name": user})

    choose_involved_users = [
        {
            "type":"checkbox",
            "name":"involved users",
            "message":"New Expense - Involved users: ",
            "choices": users_list_dict
        }
    ]
    involved_users = prompt(choose_involved_users)
    infos["involved users"] = involved_users["involved users"]
    with open('expense_registry.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=infos.keys())
        writer.writerow(infos)

    f.close()
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True


