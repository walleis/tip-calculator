print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\nR$"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))
billwithtip = (tip / 100 * bill + bill) / people
finalresult = round(billwithtip, 2)
print(f"Each person will pay R${finalresult}.")
