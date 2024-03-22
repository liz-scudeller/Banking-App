from datetime import datetime

now = datetime.now()
balance = 0
transaction = []


class Transaction:
    def __init__(self, option_value, value, balance_value):
        self.option_value = option_value
        self.value = value
        self.balance_value = balance_value

    def appendlist(self):
        if self.value != 0:
            trans_str = f'{now.strftime("%Y-%m-%d %H:%M:%S")} - {self.option_value} - ${self.value:.2f} - Balance ${self.balance_value:.2f}'
        else:
            trans_str = f'{now.strftime("%Y-%m-%d %H:%M:%S")} - {self.option_value} - Balance ${self.balance_value:.2f}'
        transaction.append(trans_str)

        with open('transactions.txt', 'a') as ctx:
            ctx.write(trans_str + '\n')

        print(transaction)
        print('Transaction Recorded\n')


while True:
    option = input('Type one option: \n1)Balance\n2)Withdrawal\n3)Deposit\n4)Transactions\n5)Exit\n')
    if option in {"1", "2", "3", "4", "5"}:
        if option == "1":
            print(f'You have ${balance:.2f} CAD\n')
            opt1 = Transaction('Checked Balance', 0, balance)
            opt1.appendlist()

        if option == "2":
            try:
                withdrawalValue = float(input('How much do you want to withdrawal? $'))
                if withdrawalValue > 0:
                    balance -= withdrawalValue
                    print(f'You withdrawal ${withdrawalValue:.2f} from your account\nYour new balance is ${balance:.2f}\n')
                    opt2 = Transaction('Withdrawal', withdrawalValue, balance)
                    opt2.appendlist()
                else:
                    print('The withdrawal value needs to be a number greater than zero!\n')
            except ValueError:
                print('Invalid input! Please enter a valid number.\n')

        if option == "3":
            try:
                depositValue = float(input('How much do you want to deposit? $'))
                if depositValue > 0:
                    balance += depositValue
                    print(f'You deposit ${depositValue:.2f} on your account\nYour new balance is ${balance:.2f}\n')
                    opt3 = Transaction('Deposit', depositValue, balance)
                    opt3.appendlist()
                else:
                    print('The deposit value needs to be a number greater than zero!\n')
            except ValueError:
                print('Invalid input! Please enter a valid number.\n')

        if option == "4":
            with open('transactions.txt', 'r') as file:
                print(file.read())

        if option == "5":
            break
    else:
        print('This is not a valid option!\n')


