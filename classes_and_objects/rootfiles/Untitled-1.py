import datetime
from colorama import init, Fore, Back, Style
my_name = input("Enter your name \n")
my_age = input("Enter your age \n")
my_date_of_birth = input("Enter your date of birth  Day.Month.Year\n")
my_date_of_birth_formatted = my_date_of_birth.split()
print(my_name)
print(my_age)
print(my_date_of_birth)
print(my_date_of_birth_formatted)
date_dateformat = datetime.datetime.strptime(my_date_of_birth, "%d.%m.%Y")
print(date_dateformat)
todays_date = datetime.datetime.today()
age_calculated = (todays_date-date_dateformat)
output = "Dear {my_name} Your age is : {age_calculated.days/365} years"
print(f"Dear {Fore.GREEN} {my_name} Your age is : {Fore.YELLOW} {int(age_calculated.days/365)} years")



