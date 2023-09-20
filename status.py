from PyInquirer import prompt
import csv

def show_status():

    file = open("users.csv", "r")
    users_list = []
    data_users = list(csv.reader(file))
    for users in data_users:
        users_list.append(users[0])

    for user in users_list:
        debt_dict = {}
        with open('expense_registry.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                if (len(row) > 3 and row[2] != user):
                    involved_list = eval(row[3])
                    for involved_user in involved_list:
                        if (involved_user == user):
                            if row[2] in debt_dict:
                                debt_dict[row[2]] += float(row[0]) // len(involved_list)
                            else:
                                debt_dict[row[2]] = float(row[0]) // len(involved_list)
        
        if debt_dict != {}:
            for key in debt_dict:
                print(user + " owes " + str(debt_dict[key]) + " to " + key)
        else:
            print(user + " owes nothing")
        f.close()
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    return True