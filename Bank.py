class Bank:
    def __init__(self):
        self.__users = {}
        self.__balance_of_bank = 0
        self.__given_loan = 0
        self.__active_loan = True

    def create_account(self, name):
        if name not in self.__users:
            self.__users[name] = {'balance': 0, 'loan_amount': 0, 'transactions': []}
            return True
        else:
            return False
    
    def user_balance(self, name):
        if name in self.__users:
            print(name,'Balance:',self.__users[name]['balance']) 
        else:
            print(name,'Has No Balance')

    def user_all_transactions(self, name):
        if name in self.__users:
            print(name,self.__users[name]['transactions']) 
        else:
            print('Not Match Account')
    
    def user_deposit(self, name, amount):
        if name in self.__users:
            self.__users[name]['balance'] += amount
            self.__users[name]['transactions'].append(f"Deposited: {amount}")
            self.__balance_of_bank += amount
            print(name,'Deposite:',amount)
        else:
            print('Not Match Account')

    def user_withdraw(self, name, amount):
        if name in self.__users:
            if self.__users[name]['balance'] >= amount:
                self.__users[name]['balance'] -= amount
                self.__users[name]['transactions'].append(f"Withdrawn: {amount}")
                self.__balance_of_bank -= amount
                print(name,'Withdraw:',amount)
            else:
                print("Unable to user_withdraw amount. Bank is bankrupt.") 
        else:
            print('Not Match Account')
    
    def user_balance_transfer(self, sender, receiver, amount):
        if sender in self.__users and receiver in self.__users:
            if amount < self.__users[sender]['balance'] :
                self.__users[sender]['balance'] -= amount
                self.__users[sender]['transactions'].append(f"Transferred: {amount} to {receiver}")
                self.__users[receiver]['balance'] += amount
                self.__users[receiver]['transactions'].append(f"Received: {amount} from {sender}")
                print(sender, 'Send', amount, 'to', receiver)
            else:
                print("Unable to user_withdraw amount. Bank is bankrupt.") 
        else:
            print('Not Match Account')

    def user_take_loan(self, name):
        if name in self.__users and self.__active_loan:
            total_amount = self.__users[name]['balance']
            loan_amount = total_amount+total_amount
            if loan_amount<=self.__balance_of_bank:
                if self.__users[name]['balance']>self.__users[name]['loan_amount']:
                    self.__users[name]['loan_amount'] += loan_amount
                    self.__users[name]['balance'] =self.__users[name]['loan_amount']
                    self.__users[name]['transactions'].append(f"Get Loan: {loan_amount}")
                    # self.__users[name]['balance'] = loan_amount
                    self.__given_loan += loan_amount
                    self.__balance_of_bank -= loan_amount
                    print(name, 'will get Loan:', loan_amount)
            else:
                print(name,'No Enough Balance in Bank')
        else:
            print('Bank Decide Nobody will get Loan')

# -------------------------------------------------Admin's Methods
    def total_balance_check(self,name):
        if name in self.__users:
            if name=='admin' or name=='Admin' or name=='ADMIN':
                print('Bank\'s Balance:',self.__balance_of_bank)
            else:
                print('Access Only Admin')
        else:
                print('No Account This Name')

    def loan_amount_check(self,name):
        if name in self.__users:
            if name=='admin' or name=='Admin' or name=='ADMIN':
                print('Bank\'s Given Loan:',self.__given_loan)
            else:
                print('Access Only Admin')
        else:
                print('No Account This Name')

    def loan_shut_down(self,name):
        if name in self.__users:
            if name=='admin' or name=='Admin' or name=='ADMIN':
                self.__active_loan= False
            else:
                print('Access Only Admin')
        else:
                print('No Account This Name')

