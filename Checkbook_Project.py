def deposit(deposit):
    if os.path.exists(user_data) == True: 
        with open(user_data, 'r') as f:
            last_data = f.readlines()[-1]
            last_data = float(last_data)
            deposit = float(deposit)
            new_bal = last_data + deposit
        with open(user_data, 'a') as f: 
            f.writelines('\n{}'.format(new_bal))
    else:
        pass

def withdraw(withdraw):
    if os.path.exists(user_data) == True: 
        with open(user_data, 'r') as f:
            last_data = f.readlines()[-1]
            last_data = float(last_data)
            withdraw = float(withdraw)
            new_bal = last_data - withdraw
        with open(user_data, 'a') as f: 
            f.writelines('\n{}'.format(new_bal))
    else:
        pass

def balance():
    if os.path.exists(user_data) == True:
        with open (user_data, 'r') as f:
            last_data = f.readlines()[-1]
            last_data = float(last_data)
    return print(last_data) #('balance: ${:0.2f}'.format(last_data))

import os


user_data = 'value.txt'
user_input = ''


while True: 
    user_input = input(
        'Please type a number for selection: 1) Deposit | 2) Withdraw | 3) Balance | 4) Exit\n'
    )

    if user_input == '1':
        deposit_input = input('Please enter dollar amount: ')
        deposit(deposit_input)
        
    elif user_input == '2':
        withdraw_input = input('Please enter dollar amount: ')
        withdraw(withdraw_input)
        
    elif user_input == '3':
        
        balance()


    elif user_input == '4': 
        break