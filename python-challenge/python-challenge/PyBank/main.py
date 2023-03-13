import csv

file_to_load = "PyBank/Resources/budget_data.csv"

total_months = 0
total_profit = 0
previous_month = 0
total_change = 0
greatest_increase = ["",0]
greatest_decrease = ["",999999999999999999]

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)

    for row in reader:
        total_months += 1
        profit = int(row[1])
        month = row[0]
        total_profit += profit
        if total_months > 1:
            change = profit - previous_month
            total_change += change
            if change > greatest_increase[1]:
                greatest_increase[0] = month
                greatest_increase[1] = change
            if change < greatest_decrease[1]:
                greatest_decrease[0] = month
                greatest_decrease[1] = change   
        previous_month = profit


print(f"Total Months: {total_months}")
print(f"Total Profit: ${total_profit}")
print(f"Total change: ${total_change}")
avg_change = total_change / (total_months -1)
print(f"Total average change: ${avg_change}")
print(f"Total Increase in profit: {greatest_increase[0]}(${greatest_increase[1]})")
print(f"Total Decrease in profit: {greatest_decrease[0]}(${greatest_decrease[1]})")
