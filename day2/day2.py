print("Welcome to the tip calculator.\n")

totalbill = int(input("What was the total bill?\n"))
numberofpeople = int(input("How many people split the bill?\n"))
percentagetip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))

def individual_total(tb, nop, pt):
    tipdecimal = pt / 100
    individualbill = tb / nop
    individualtip = individualbill * tipdecimal
    individualtotal = individualbill + individualtip
    print(f"Each person should pay: {individualtotal}")


individual_total(totalbill, numberofpeople, percentagetip)