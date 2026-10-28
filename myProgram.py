
# Simple Python Tax Calculator

income = float(input("Enter your annual income: $"))
tax_rate = float(input("Enter the tax rate (%): "))

tax = income * tax_rate / 100
after_tax_income = income - tax

print(f"Estimated tax: ${tax:,.2f}")
print(f"Income after tax: ${after_tax_income:,.2f}")
