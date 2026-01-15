# hello_world.py
# This program prints user details and today's date

# Importing datetime module to get today's date
import datetime

# Taking user input
name = input("Enter your name: ")
role = input("Enter your internship role: ")

# Getting today's date
today_date = datetime.date.today()

# Printing the output
print("\n----- Internship Details -----")
print("Name:", name)
print("Internship Role:", role)
print("Today's Date:", today_date)
print("------------------------------")
