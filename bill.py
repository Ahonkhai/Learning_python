print("welcome to the tip calculator")


bill = float(input("what was the total bill? $"))
tip  = float(input("How much tip would you like to give? 10%, 12%, or 15% \n")) / 100
people = int(input("How many people spilt the bill? "))

total_sum = bill * ( 1 + tip)
equal_sum = total_sum / people

equal_sum = round(equal_sum, 2)
print(f"Each person pays:${equal_sum} ")



