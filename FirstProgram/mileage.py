print("How many kilometers did you run today?")
# String from input()
kms = input()
# convert string to float then divide
miles = float(kms)/1.60934
# round to 2 decimal places
miles = round(miles, 2)
print(f"Your {kms}km ride is {miles}miles")