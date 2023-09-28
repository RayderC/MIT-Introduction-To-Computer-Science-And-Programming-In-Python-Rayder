while True:
    try:
        annual_salary = float(input("Please enter your annual salary: "))
        portion_saved = float(input("Please enter the percent of your salary to save, as a decimal: "))
        total_cost = float(input("Please enter the total cost of your dream house: "))
        break

    except ValueError:
        print("Invalid input. Please enter valid number.")

portion_down_payment = 0.25  # 25% down payment
current_savings = 0  # Initial savings
r = 0.04  # Annual return on investment
months = 0  # Initialize months counter

# Calculate monthly savings and return until enough is saved for down payment
while current_savings < total_cost * portion_down_payment:
    monthly_salary = annual_salary / 12
    monthly_savings = monthly_salary * portion_saved
    current_savings += current_savings * (r / 12) + monthly_savings
    months += 1

print(f"Number of months: {months}")