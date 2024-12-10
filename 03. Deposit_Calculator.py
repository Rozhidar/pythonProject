sum_deposited = float(input())
term_for_deposit_in_months = int(input())
annual_percentage_rate = float(input())

annual_percentage_rate_in_percents = annual_percentage_rate / 100

accrued_interest = sum_deposited * annual_percentage_rate_in_percents

interest_for_one_month = accrued_interest / 12

total_amount = sum_deposited + term_for_deposit_in_months * interest_for_one_month

print(total_amount)
