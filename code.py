class Account:
    '''
    create an account with an account owner and an account balance.
    default balance is '0'
    '''
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    
    '''
    show owner and balance
    '''
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount Balance: ${self.balance}"
        
    '''
    add deposit amount to balance and print deposited amount
    '''
    def deposit(self,dep_amnt):
        self.balance += dep_amnt
        print(f"You successfully deposited ${dep_amnt}")
    
    '''
    subtract withdrawal amount and print withdrawal amount and balance after withdrawal.
    do not allow withdrawal if account balance is less than withdrawal amount
    '''
    def withdraw(self,wth_amnt):
        if self.balance >= wth_amnt:
            self.balance -= wth_amnt
            print(f"You successfully withdrew ${wth_amnt}")
            print(f"Your Balance is now ${self.balance}")
        
        else:
            print("Sorry, you have insufficient funds.") 
            return f"Your Balance is ${self.balance}"
            
    
    # Try it out...
myaccount = Account('Gordo', 100)
print(myaccount)
myaccount.deposit(1000)
myaccount.withdraw(1000)
myaccount.withdraw(120)
