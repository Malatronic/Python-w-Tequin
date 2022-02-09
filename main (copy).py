"""
Day Calculator
-Malachi lang and Tequin Lake
Date: 0/2/2022
MVP:
  https://docs.python.org/3/library/datetime.html#examples-of-usage-date
  https://docs.python.org/3/tutorial/errors.html
"""
#-----------Imports-----------
import datetime

#-----------FUNCTIONS-----------

# Converts string to int and restarts if it isn't a number
def to_int(string_number):
  try: # If no error convert to int and return
    int_number = int(string_number)
    return int_number
  except ValueError: # If ValueError tell user and restart
    print("Ayo use number. \n")
    get_day()

# Says a sentance with the weekday, and starts over
def say_day(weekday):
  print("The day is a", weekday, "\n")
  get_day()

#-----------MAIN-----------
# Repeatable function to keep repeating
def get_day():
  # Get user inputs and check and convert to int
  day = to_int(input("Day: "))
  month = to_int(input("Month: "))
  year = to_int(input("Year: "))

  # Gets the weekday
  weekday = (datetime.date(year, month, day).weekday())

  # Checks what day of the week it is
  if weekday == 0:
    say_day("Monday")
  if weekday == 1:
    say_day("Tuesday")
  if weekday == 2:
    say_day("Wednsday")
  if weekday == 3:
    say_day("Thursday")
  if weekday == 4:
    say_day("Friday")
  if weekday == 5:
    say_day("Saturday")
  if weekday == 6:
    say_day("Sunday")

get_day()
