
import random

class User:
    def __init__(self, name, age, address, id_number):
        self.name = name
        self.age = age
        self.address = address
        self.id_number = id_number
        self.is_verified = False

class KYC_Bot:
    def __init__(self):
        self.users = []

    def add_user(self, name, age, address, id_number):
        user = User(name, age, address, id_number)
        self.users.append(user)

    def verify_user(self, id_number):
        for user in self.users:
            if user.id_number == id_number:
                user.is_verified = True
                return True
        return False

    def generate_id(self):
        return random.randint(100000, 999999)

bot = KYC_Bot()

while True:
    print("Welcome to the KYC Bot!")
    print("1. Add User")
    print("2. Verify User")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        address = input("Enter your address: ")
        id_number = bot.generate_id()
        bot.add_user(name, age, address, id_number)
        print("User added. Your ID number is:", id_number)

    elif choice == 2:
        id_number = int(input("Enter your ID number: "))
        if bot.verify_user(id_number):
            print("User verified. You can now access premium features.")
        else:
            print("User not found. Please try again.")

    elif choice == 3:
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
