deposit_sum = float(input())
time_months = int(input())
percents_rerward = float(input())


reward_per_month = ((deposit_sum / 100) * percents_rerward) / 12
end_deposit_sum = deposit_sum + time_months * reward_per_month




print(end_deposit_sum)