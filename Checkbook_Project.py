Main_input = input('Please select an option:')
Deposit_input = input('How much would you like to desposit?')
Withdrawal_input = input('How much would you like to withdraw?')


#-----------------


options = ['Deposit', 'Withdraw', 'Balance', 'Exit']

user_input = ''

input_message = "Please select a valid option\n"

for index, item in enumerate(options):
    input_message = input_message + f'{index+1}) {item}\n'
input_message = input_message + 'Your choice: '

while user_input not in map(str, range(1, len(options) + 1)):
    user_input = input(input_message)

print('You picked: ' + options[int(user_input) - 1])

#--------------

user_input = ''

while True: 
    user_input = input(
        'Please type a number for selection: 1) Deposit | 2) Withdraw | 3) Balance | 4) Exit
    )

    if user_input == '1':
        Deposit_input = ''

        while True:
            try: 
                Deposit_input = float(input('Type positive dollar amount to deposit: '))
                if Deposit_input >= 0:
                    print( '${:,.2f}'.format(Deposit_input))
                    break
 
            except ValueError: 
                Deposit_input = input('That is not a valid dollar amount. Type dollar amount to deposit: ')
        
    if user_input == '2':
        Withdrawal_input = ''
        while True:
            Withdrawal_input = input('Type dollar amount to withdraw')

    if user_input == '3':


    if user_input == '4': 
        break
