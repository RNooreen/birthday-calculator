#!/usr/bin/env python3

### Assignment Week 7- Birthday Calculator
### Author: Ruqayya Nooreen

# Importing datetime and date module
from datetime import datetime,date


#  This function displays the title
def display_title():
  print("===================================")
  print("      Birthday Calculator!      ")
  print("===================================")


# This function does all the calculations
def calc_birthday():
  my_name= input("Enter name:")


 #This code uses exceptions to check if the user has entered valid date
  while True:
      my_date_str= input("Enter birthday (MM/DD/YY):")
      
      try:
          my_date= datetime.strptime(my_date_str, "%m/%d/%y")
          break
      except ValueError:
          print("Invalid Date. Enter (MM/DD/YY) format with valid values for each ")
      
      
  new=my_date
  today=date.today()

  if my_date>datetime.today():
    new=my_date.replace(year=my_date.year-100)

  my_weekday=new.strftime("%A")
  my_month=new.strftime("%B")
  my_year=new.strftime("%Y")
  my_dt=new.strftime("%d")
  print(f"\nBirthday: {my_weekday}, {my_month} {my_dt}, {my_year}")

  today_weekday=today.strftime("%A")
  today_month=today.strftime("%B")
  today_year=today.strftime("%Y")
  today_dt=today.strftime("%d")
  print(f"Today: {today_weekday}, {today_month} {today_dt}, {today_year}")
  

  if today<date(today.year,new.month,new.day):
    next_birthday=date(today.year,new.month,new.day)
    age=today.year-new.year-1
  else:
    next_birthday=date(today.year+1,new.month,new.day)
    age=today.year-new.year

  print(f"{my_name} is {age} years old.")

  diff=(next_birthday - today).days

  if diff==365:
    print(f"{my_name}'s birthday is today!")
  elif diff==364:
    print(f"{my_name}'s birthday was yesterday!")
  elif diff==1:
    print(f"{my_name}'s birthday is tomorrow!")
  else:
    print(f"{my_name}'s birthday is in {diff} days")
    



# This function displays the final message
def end_message():
  print("\nBye!")


# Defining the main function
def main():
  display_title()
  response= "y"
  while response.lower() == "y":
    calc_birthday()
    response = input("\nContinue(y/n): ")
  end_message()



# Calling the main function
if __name__ == "__main__":
  main()

