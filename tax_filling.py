TAX_RATE = 0.20
STANDED_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

grossIncome = float(input("Enter the gross income: "))
numDependents = float(input("Enter the number of dependents: "))

taxableIncome = grossIncome - STANDED_DEDUCTION - DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE

print("this income tax is $"+ str(incomeTax))