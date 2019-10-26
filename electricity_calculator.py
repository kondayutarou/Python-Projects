# python 3
# An electricity calculator for adding, editing, saving, displaying electricity information at user's request
import shelve
import os

print("\nElectricity data is read.")
if os.path.exists("electricity_data.bak") and os.path.exists("electricity_data.dir") and os.path.exists(
        "electricity_data.dat"):
    shelf = shelve.open("electricity_data")
    # electricity = (year, month): [kW, yen]
    electricity = shelf["electricity"]
else:
    shelf = shelve.open("electricity_data")
    electricity = {}
    shelf["electricity"] = electricity


def month_name(date):
    if date == 1 or date == "1":
        return "Jan."
    elif date == 2 or date == "2":
        return "Feb."
    elif date == 3 or date == "3":
        return "Mar."
    elif date == 4 or date == "4":
        return "Apr."
    elif date == 5 or date == "5":
        return "May"
    elif date == 6 or date == "6":
        return "Jun."
    elif date == 7 or date == "7":
        return "Jul."
    elif date == 8 or date == "8":
        return "Aug."
    elif date == 9 or date == "9":
        return "Sep."
    elif date == 10 or date == "10":
        return "Oct."
    elif date == 11 or date == "11":
        return "Nov."
    elif date == 12 or date == "12":
        return "Dec."
    else:
        return date


def input_integer_determiner():
    # Ensure input string is an integer. Otherwise, prompts the user for another input.
    while True:
        string = input("> ")
        if string.isdecimal():
            return int(string)
        else:
            print("Invalid input. Try again.")


def input_year_determiner():
    # Ensure input string is a valid year. Otherwise, prompts the user for another input.
    while True:
        string = input("> ")
        if string.isdecimal():
            if 2019 <= int(string) <= 2025:
                return int(string)
            else:
                print("Invalid input. Try again.")
        else:
            print("Invalid input. Try again.")


def input_month_determiner():
    # Ensure input string is a valid year. Otherwise, prompts the user for another input.
    while True:
        string = input("> ")
        if string.isdecimal():
            if 1 <= int(string) <= 12:
                return int(string)
            else:
                print("Invalid input. Try again.")
        else:
            print("Invalid input. Try again.")


def date_search(year, month, dictionary):
    if (year, month) in dictionary.keys():
        print("Warning. The input date already exists.\n")


def total_electricity(dictionary):
    # For displaying both electricity consumption and the bill
    for date, electricity_data in dictionary.items():
        year, month = date
        dictionary.setdefault(date, 0)
        print(f"On {month_name(month)} {year}:")
        print(f"""Total electricity: {electricity_data[0]} kW
Total bill: {electricity_data[1]} Yen
""")


def electricity_per_kw(dictionary):
    # For creating a new dictionary consisting of a date and a cost per kW
    for date, electricity_data in dictionary.items():
        average = electricity_data[1] / electricity_data[0]
        year, month = date
        print(f"On {month_name(month)} {year}:")
        print(f"""Average electricity cost: {round(average, ndigits=2)} Yen/kW
        """)


def save():
    print("Electricity data is saved.")
    shelf["electricity"] = electricity


def append_info(dictionary):
    print("Add information on electricity usage and bill.")
    print("Input year:")
    year = input_integer_determiner()
    print("Input month:")
    month = input_integer_determiner()
    # Check if the input date actually exists in dictionary.
    date_search(year, month, dictionary)
    print("Input electricity usage (kW):")
    usage = input_integer_determiner()
    print("Input electricity bill (Yen):")
    bill = input_integer_determiner()
    print(f"""
Do you want to add the following information?
    "You used {usage} kW for {bill} yen on {month_name(month)} {year}."
If yes, input "y", otherwise, input any other string.
""")
    confirmation = input("> ")
    if confirmation.lower() == "y":
        dictionary[(year, month)] = [usage, bill]
        print("Change reflected.")


def edit_info(dictionary):
    print("Navigate to a piece of information you want to change.")
    print("Input year:")
    year = input_year_determiner()
    print("Input month:")
    month = input_month_determiner()
    # For checking whether the input date already exists in dictionary.
    if (year, month) in dictionary.keys():
        # Retrieve and display the relevant value from the dictionary.
        print("Electricity usage and bill for the specified date:")
        print(f"{dictionary[(year, month)][0]} kW for {dictionary[(year, month)][1]} yen.\n")
        # Prompt a user to input electricity usage and bill for the date.
        print("Input new electricity usage")
        usage = input_integer_determiner()
        print("Input new electricity bill")
        bill = input_integer_determiner()
        # Confirm the user on the change.
        print('Do you wish to make the following change? If yes, input "y", otherwise, input any other key.')
        print(f"\tYou used {usage} kW for {bill} yen.\n")
        if input("> ").lower() == "y":
            dictionary[(year, month)] = [usage, bill]
            print("Change reflected.")
    else:
        print("The specified date does not exist in the dictionary.")


while True:
    print(f"""
Type "a" to add information to electricity data.
Type "e" to edit existing information on the electricity data.
Type "s" to save the electricity data.
Type "t" to display total electricity (in kW and yen).
Type "p" to display average electricity cost per kW (in yen).
Type "q" to quit.
""")
    user_input = input("> ")
    if user_input.lower() == "q":
        shelf.close()
        break
    elif user_input.lower() == "t":
        total_electricity(electricity)
    elif user_input.lower() == "p":
        electricity_per_kw(electricity)
    elif user_input.lower() == "s":
        save()
    elif user_input.lower() == "a":
        append_info(electricity)
    elif user_input.lower() == "e":
        edit_info(electricity)
