# #___Given Input of DOB in format of DD-MM-YYYY : it will return in format of MM-YYYY-DD. ELSE it will return INVALID:
from datetime import datetime

def date_of_birth(date):
    try:
        DOB = datetime.strptime(date,"%d-%m-%Y")
        print("Your date is",DOB)

        print("-----------After converting in MM-YYYY-DD format----")
        print(DOB.strftime("%m-%Y-%d"))

    except ValueError:
        print("Invalid")
print("Eg:- Today is my birthday 31-12-1999 (FORMAT)")
date = input("Enter the DATE OF BIRTH....")
date_of_birth(date)
