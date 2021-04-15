from datetime import date
today = date.today()
class Budget:
    """
    This is a blueprint for a budget app with all functionalities such as deposit, withdrawal and transfer. It has a default balance set to zero for an instance of a new user
    """
    balance = {
        "Food": 0,
        "Clothing": 0,
        "Entertainment" : 0
            }
    budget_category = ["Food", "Clothing", "Entertainment"]
    
    def __init__(self, category):
        self.category = category - 1      #Since the index of the balance is zero-based
        
    def transactions(self):
        isTransacting = False
        while isTransacting == False:
            print("------------" *10)
            print("This is your %s budget. What would you like to do?" % Budget.budget_category[self.category])
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer to another category")
            print("4. Check total budget balance")
            print("5. Go to Home")
            try:
                option = int(input(""))
                if option == 1:
                    self.deposit()
                    isTransacting = True
                elif option == 2:
                    self.withdraw()
                    isTransacting = True
                elif option == 3:
                    self.transfer()
                    isTransacting = True
                elif option == 4:
                    self.checkBalance()
                    isTransacting = True
                elif option == 5:
                    init()
                else:
                    print("Invalid selection")
            except (ValueError, IndexError):
                print("Invalid Selection. Please select within the range above")
                
    def deposit(self):
        print("---------" *10)
        deposited = int(input("How much would you like to deposit? \n"))
        Budget.balance[Budget.budget_category[self.category]]+= deposited
        print("%d Naira has been deposited into your %s budget " %( deposited, Budget.budget_category[self.category]))
        self.secondTransaction()
        
    def withdraw(self):
        print("---------" *10)
        withdrawn = int(input("How much would you like to withdraw? \n"))
        if withdrawn <= Budget.balance[Budget.budget_category[self.category]]:
            Budget.balance[Budget.budget_category[self.category]] -= withdrawn
            print("Take you cash. %d Naira has been deducted from your %s budget " %( withdrawn, Budget.budget_category[self.category]))
            self.secondTransaction()
        else:
            print("Insufficient Funds")
            self.secondTransaction()
    
    def transfer(self):
        print("---------" *10)
        try:
            option = self.category + 1
            transferAmt = int(input("How much would you like to transfer? \n"))
            print("To which category?")
            for index, category in enumerate(Budget.budget_category):
                print(f"{index + 1}. {category}")
            option2 = int(input(""))
            if option == option2:
                print("You cannot transfer to the same category")
                self.transfer()
            elif option != option2:
                if transferAmt <= Budget.balance[Budget.budget_category[self.category]]:
                    Budget.balance[Budget.budget_category[option2 -1]] += transferAmt
                    Budget.balance[Budget.budget_category[self.category]] -= transferAmt
                    print("%d Naira has been transferred to %s budget" %(transferAmt, Budget.budget_category[option2 -1]))
                    self.secondTransaction()
                else:
                    print("Insufficient Funds")
                    self.secondTransaction()
            else:
                print("Invalid selection.")
                self.secondTransaction()
        except (ValueError, IndexError):
            print("Invalid Selection. Please select within the range above")   
            
    def secondTransaction(self):
        try:
            option = int(input("Would you like to do anything else? 1. Yes 2. No \n"))
            if option ==1:
                self.transactions()
            elif option == 2:
                print("Have a good day")
                exit()
            else:
                print("Invalid selection. Please select between 1 -3")
        except (ValueError, IndexError):
            print("Invalid Selection. Please select within the range above")
            self.secondTransaction()
            
    def checkBalance(self):
        print("Your budget balance as at %s is : "% today)
        for key in Budget.balance:
            print(key, ":", Budget.balance[key])
        print("--------" *10)
        self.secondTransaction()
         
            
            
            
def init():
    print("--------" *10)
    print("Welcome to your SaveWithSense budget App")
    isSelecting = False
    while isSelecting==False:
        print("Select Category or press 0 to create a new category")
        def printCategories():
            for index, category in enumerate(Budget.budget_category):
                print(f"{index + 1}. {category}")
        printCategories()
        try:
            option = int(input("")) 
            if option == 0:
                new_category = input("Enter category name: \n")
                new_category = new_category.capitalize() 
                if new_category in Budget.budget_category :
                    print("This category already exists")
                    print("----------" *10)
                else:
                    Budget.budget_category.append(new_category)
                    Budget.balance[new_category] = 0
                    print(f"Your new {new_category} category has been created")
                    print("----------" *10)
            elif option != 0:
                category_selected = Budget(option)
                category_selected.transactions()
            else:
                print("Invalid Selection.")
        except (ValueError, IndexError):
            print("Invalid Selection. Please select within the range above **")
            
init()
