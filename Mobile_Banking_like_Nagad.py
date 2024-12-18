# Mobile Banking system like Nagad
# Here I tried to create a mobile banking system like Nagad or Bkash with python. It is not totally similar to Nagad but has quite differences.
# I tried as much as possible.

all_account_numbers = []

class BankingSystem:
    def __init__(self, account_holder_name,account_number, pin_number, initial_amount=0):
        if account_number in all_account_numbers:
            print("Account Number Already Exists. Enter a unique Account Number")
        else:
            all_account_numbers.append(account_number)
            self.acc_holder_name = account_holder_name
            self.account_number = account_number
            self.pin_number = pin_number
            self.total_amount = initial_amount

            print(f"\nHi, {self.acc_holder_name}!\nYour Account has been created.\n"
                  f"Your Current Balance is {self.total_amount} tk.\n"
                  f"Your account number is {self.account_number}\n"
                  f"Your pin number is {self.pin_number}\n"
                  f"Don't share your PIN number with anyone.")
#Balance check
    def check_balance(self,pin_number):
        if int(pin_number)==self.pin_number:
            print(f"\nAccount Name: {self.acc_holder_name}")
            print(f"Your current balance: {self.total_amount} tk.")
        else:
            print("\nInvalid Pin Number")
#Deposit money
    def deposit(self, amount,pin_number):
        if int(pin_number)==self.pin_number:
            if amount > 0:
                self.total_amount += amount
                print(f"\n{amount} tk have been deposited.\n"
                      f"Your Current Balance is {self.total_amount} tk.")
            else:
                print(f"\n{amount} is not a valid amount to deposit.")
        else:
            print("\nInvalid Pin Number")
#withdraw money
    def withdraw(self, amount,pin_number):
        if int(pin_number)==self.pin_number:
            if 0 < amount <= self.total_amount:
                self.total_amount -= amount
                print(f"\n{amount} tk withdrawn successfully.\n"
                      f"Your Current Balance is {self.total_amount} tk.")
            else:
                print(f"\nInsufficient funds to withdraw {amount} tk.")
        else:
            print("\nInvalid Pin Number")
#Account information
    def account_info(self,pin_number):
        if int(pin_number)==self.pin_number:
            print(f"\nAccount holder name: {self.acc_holder_name}.\n"
                  f"Your account number is {self.account_number}\n"
                  f"Your Current Balance is {self.total_amount} tk.\n"
                  f"Your pin number is {self.pin_number}\n"
                  f"Don't share your PIN number with anyone.")

#For showing menu
def show_menu():
    account = None

    while True:
        menu = ("\n"
                "1. Create Account\n"
                "2. Deposit\n"
                "3. Withdraw\n"
                "4. Check Balance\n"
                "5. Account Details\n"
                "6. Exit")
        print(menu)

        choice = input("Enter your choice (1-5): ")
#Account creation
        if choice == "1":
            print("\n")
            name = input("Enter your name: ")
            acc_num = int(input("Enter account number: "))
            pin_number = int(input("Enter your pin number: "))
            initial_amount = int(input("Enter initial amount: "))
            account = BankingSystem(name, acc_num,pin_number, initial_amount)
#Deposit money
        elif choice == "2":
            if account is None:
                print("\nYou have no account.\n"
                      "Please create an account first.")
            else:
                amount = int(input("Enter amount to deposit: "))
                pin_number = int(input("Enter your pin number: "))
                account.deposit(amount,pin_number)
#Withdraw money
        elif choice == "3":
            if account is None:
                print("\nYou have no account.\n"
                      "Please create an account first.")
            else:
                amount = int(input("Enter amount to withdraw: "))
                pin_number = input("Enter your pin number: ")
                account.withdraw(amount,pin_number)
#Check balance
        elif choice == "4":
            if account is None:
                print("\nYou have no account.\n"
                      "Please create an account first.")
            else:
                pin_number = input("Enter your pin number: ")
                account.check_balance(pin_number)
#Show account information
        elif choice == "5":
            if account is None:
                print("\nYou have no account.\n")
                print("Please create an account first.")
            else:
                pin_number = input("Enter your pin number: ")
                account.account_info(pin_number)
#Exit program
        elif choice == "6":
            print("\nThank you for banking with us.")
            break

        else:
            print("\nInvalid choice. Please choose between 1 to 5.")



print("To open menu, Enter *167# code.")
#Checking code
while True:
    mobile_menu=input("Enter code: ")
    if mobile_menu == "*167#":
        print("Welcome to Nagad.")
        show_menu()
    else:
        print("Invalid choice. Please choose *167# code.")
