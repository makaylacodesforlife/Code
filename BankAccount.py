# Coder: Makayla Mayne
# Date: October 10, 2021
# Purpose: Deposit and transfer money between accounts

# In your week4 folder, create a new file and name it workshop4.py.
# In this file, declare a class and give it the name User.
# Give the User class three instance attributes: name, pin, and password.
class User:
    def __init__(self, name: str, pin: int, password: str):
        self.name = name
        self.pin = pin
        self.password = password
    # write this driver code in the same file
    # (workshop4.py),
    # but keep it at the bottom of the file,
    # separated from the rest of your code.
    # Driver Code for Task 1

    def __str__(self):
        return f"{self.name} {self.pin} {self.password}"

    # Driver Code for Task1
    # user = User("Bob", 1234, "password ")
    # It should inherit the instance
    # attributes of name, pin, and password.

    def change_name(self, new_name: str):
        # Changes the name to a new name
        self.name = new_name

    def change_pin(self, new_pin: int):
        # Changes the pin to a new pin
        self.pin = new_pin

    def change_password(self, new_password: str):
        # Changes the password to a new password
        self.password = new_password

    # initializes the name pin and password


class BankUser(User):
    def __init__(self, name: str, pin: int, password: str):
        super().__init__(name, pin, password)
        self.balance = 0.0

    # shows the balance of your account
    def show_balance(self):
        print(f"{self.name} has a balance of: ${self.balance}")

    # withdraws money from specified account
    def withdraw(self, amount_to_withdraw: float):
        if self.balance - amount_to_withdraw < 0:
            print("Insufficient funds.")
        else:
            self.balance -= amount_to_withdraw

    # deposits money into specified account
    def deposit(self, amount_to_deposit: float):
        self.balance += amount_to_deposit

    # approves the transfer of money for an account
    def transfer_money(self, recipient: object, amount_to_transfer: float):
        pin = int(input(f"Enter {self.name}'s PIN:"))
        if pin == self.pin:
            self.balance = self.balance - amount_to_transfer
            recipient.balance = recipient.balance+amount_to_transfer
            print("Transfer authorized")
            print(f"Transferred {amount_to_transfer} to {recipient.name}")
            return True
        else:
            print("Invalid PIN. Transaction canceled.")
            return False

    # requests money. If it is authorized it will transfer the money into the account
    def request_money(self, recipient: object, amount: float):
        print(f"\nYou are requesting ${amount} from {self.name}")
        print("User authentication is required...")
        pin = int(input(f"Enter {recipient.name}'s PIN:"))
        if pin == recipient.pin:
            self.withdraw(amount)
            recipient.deposit(amount)
            print("Request authorized")
            password = input("Enter your password:")
            if password != recipient.password:
                print("Invalid password. Transaction canceled.")
                return False
            if(password == recipient.password):
                print(f"Request authorized")
                print(f"{self.name} sent ${amount}")
                return True
        else:
            print("Invalid PIN. Transaction canceled.")
            return False


"""
user = User("Bob", 1234, "password")
user.change_name("Bobby")
user.change_pin(4321)
user.change_password("newpassword")
print(user)
"""

# Driver code for task 3
"""
user = BankUser("Bob", 1234, "password")
print(user, user.balance)
"""

# Driver code for Task 4
# Uncomment the following section to check if my code works!
"""
user = BankUser("Bob", 1234, "password")
user.show_balance()
user.deposit(1000)
user.show_balance()
user.withdraw(500)
user.show_balance()
"""


# driver code for 5
# instantiate an object of the BankUser Class
user = BankUser("Alice", 4321, "password1")
user2 = BankUser("Bob", 1234, "password")

user.deposit(5000)
user.show_balance()
user2.show_balance()
print("You are transferring $500 to Bob\nAuthentication required")
user.transfer_money(user2, 500)
user.show_balance()
user2.show_balance()
user2.request_money(user2, 400.0)
user.show_balance()
user2.show_balance()
