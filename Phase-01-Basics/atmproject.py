import random
import datetime

# User ka data aur details manage karne ke liye class banayi
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # User ki information screen par dikhane ke liye method
    def show_info(self):
        print(f"Holder name: {self.name} | balance in account: {self.balance}")

# Ek sample user account create kiya
user1 = Account("Akash", 5000000)

# Login verification ke liye random 4-digit OTP generate kiya
otp = random.randint(1111, 9999)
print(f"The OTP is {otp}")

# User ko 5 mauke (attempts) dene ke liye variable
chance = 5

# OTP verification process shuru (Loop tab tak chalega jab tak chances hain)
while chance > 0:
    try:
        user_otp = int(input("Enter the otp you have received: "))

        # Agar user ka input OTP se match ho jata hai
        if user_otp == otp:
            print("This is the Valid otp")
            
            # Current time nikal kar use readable format (12-hour) mein badla
            now = datetime.datetime.now().strftime("%I:%M:%S %p")
            print(f"The login time is {now}")
            user1.show_info()
            
            # Login details ko permanent file 'account.txt' mein save kiya
            with open("account.txt", "a") as f:
                f.write(f"User: {user1.name} | Login Time: {now} | Balance: {user1.balance}\n")
            
            # Login successful hone par loop se bahar nikal gaye
            break

        # Agar OTP galat hai toh chances kam karo
        else:
            chance -= 1
            if chance > 0:
                print(f"Wrong otp! {chance} retry left.")
            else:
                print("Account Blocked! All attempts exhausted.")
                
    # Agar user number ki jagah alphabet/text daal de toh error handle kiya
    except ValueError:
        print("Invalid Input! Please enter numbers only.")
