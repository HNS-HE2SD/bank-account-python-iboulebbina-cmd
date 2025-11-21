class Client:
    def __init__(self, cin, firstName, lastName, tel=""):
        self.__CIN = cin
        self.__firstName = firstName
        self.__lastName = lastName
        self.__tel = tel
        self.__accounts = [] #When we create a new account for client, we add it to this list
    def get_CIN(self):
        return self.__CIN
    def get_firstName(self): 
        return self.__firstName
    def get_lastName(self): 
        return self.__lastName
    def get_tel(self): 
        return self.__tel
    def set_tel(self, tel): 
        self.__tel = tel
    def add_account(self, account):    
        self.__accounts.append(account) #Allow a client to hold multiple accounts
    def display_accounts(self):
        if len(self.__accounts) == 0:  
            print("No accounts found")
        else:
            for acc in self.__accounts:
                account_code = acc.get_code()
                account_balance = acc.get_balance()
                print("Account",account_code,"",account_balance,"DA")

    def display(self):
        print(f"CIN: {self.__CIN}, Name: {self.__firstName} {self.__lastName}, Tel: {self.__tel}")
class Account:
    __nbAccounts = 0 #static variable counts how many accounts have been created
    def __init__(self, owner):
        Account.__nbAccounts += 1
        self.__code = Account.__nbAccounts
        self.__balance = 0.0
        self.__owner = owner
        self.__transactions = []  # Store all the actions done on the account
        owner.add_account(self)  #add the new account to client's account list
def __validate_amount(self, amount):
        if amount <= 0:
            print("Error:You must enter a number  positive")
            return False
        return True
def __record_transaction(self, type, amount, target_account=None):
        transaction = {
            'type': type,
            'amount': amount,
            'balance_after': self.__balance
        }
        if target_account:
            transaction['target_account'] = target_account.get_code()
        self.__transactions.append(transaction)
def get_code(self): 
    return self.__code
def get_balance(self): 
    return self.__balance
def get_owner(self): 
    return self.__owner
def credit(self, amount, account=None):
    valid = self.__validate_amount(amount)
    if valid == False:
        return #ُُExit the function without adding the money or recording the operation
    if account is None:
            self.__balance += amount
            self.__record_transaction('CREDIT', amount)

    else:
        if account.get_balance() >= amount:   #Check if the other account has enough money to make the transfer
            self.__balance += amount
            self.__record_transaction('TRANSFER_IN', amount, account)  #Record transfer received from another account
        else:
            print("Not enough money in the other account") 
def debit(self, amount, account = None):
    valid = self.__validate_amount(amount)
    if valid == False:
        return 
    if account is None: #Just take money from this account
        if self.__balance >= amount:
                self.__balance -= amount
                self.__record_transaction('DEBIT', amount)
        else:
            print("Insufficient balance.")
    else:
        if self.__balance >= amount:
                self.__balance -= amount
                self.__record_transaction('TRANSFER_OUT', amount, account)
                account.credit(amount)  # Credit the target account
        else:
            print("Transfer failed: Insufficient balance.")
def displayTransactions(self):
    print("Transactions for this account:", self.__code)
    if len(self.__transactions) == 0:
        print("  No operations done yet")
        return
    i = 1
    for trans in self.__transactions:
        print(" ", i, ". Type:", trans['type'], ", Amount:", trans['amount'], "DA")
        i += 1
    if 'target_account' in trans:
        print("     Sent/Received to Account:", trans['target_account'])  #"If the operation is a transfer we write the other account
        print("     Balance now:", trans['balance_after'], "DA")#After each operation we write the current balance of the account
def display(self):
        print(f"Account Code: {self.__code}")
        print(f"Owner: {self.__owner.get_firstName()} {self.__owner.get_lastName()}")
        print(f"Balance: {self.__balance} DA")
@staticmethod
def displayNbAccounts():
        print("Total accounts created:", Account.__nbAccounts)
#MyAccount inherits the properties from Account
class MyAccount(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner) 
        self._Account__balance = balance
        self.vip_message = "Welcome to your Account!"  
    def greet(self):
        print(f"{self.vip_message} Your current balance is: {self.get_balance()} DA")




