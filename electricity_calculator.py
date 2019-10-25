import pprint

electricity = {"201906": [112, 3423], "201907": [105, 3259], "201908": [124, 3664], "201909": [194, 5541],
               "201910": [117, 3176]}
# date: [electricity, cost]


def total_electricity(dictionary):
    # For displaying both electricity consumption and the bill
    for date, electricity_data in dictionary.items():
        dictionary.setdefault(date, 0)
        print(f"On {date}:")
        print(f"""Total electricity: {electricity_data[0]} kW
Total bill: {electricity_data[1]} Yen
""")


def electricity_per_kw(dictionary):
    # For creating a new dictionary consisting of a date and a cost per kW
    kw_dic = {}
    for date, electricity_data in dictionary.items():
        kw_dic.setdefault(date, 0)
        kw_dic[date] = electricity_data[1] / electricity_data[0]
    return kw_dic


while True:
    print(f"""
Type "t" for displaying total electricity (in kW and yen).
Type "p" for displaying electricity cost per kW (in yen).
Type "q" for quit.
""")
    user_input = input("> ")
    if user_input.lower() == "q":
        break
    elif user_input.lower() == "t":
        print("\n")
        total_electricity(electricity)
    elif user_input.lower() == "p":
        print("    date : electricity per kW")
        pprint.pprint(electricity_per_kw(electricity))