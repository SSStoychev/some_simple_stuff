deposit_amount = float(input())
months = int(input())
year_fee = float(input())

per_year = deposit_amount * (year_fee / 100)
per_month = per_year / 12
total_sum = deposit_amount + (per_month * months)


print(total_sum)

