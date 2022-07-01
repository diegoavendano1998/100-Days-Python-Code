print("Welcome to the bill calculator!\n")
bill = float(input("Whats the bill total? $"))
tip = int(input("What percentage of tip you like to give? %"))
people = int(input("How many people to split the tip?"))


bill_with_tip = tip / 100 * bill + bill
bill_per_person = round(bill_with_tip /people, 2)
# Otra forma de redondear
bill_per_person = "{:.2f}".format(bill_per_person)


print(f"Bill per person ${bill_per_person}")

