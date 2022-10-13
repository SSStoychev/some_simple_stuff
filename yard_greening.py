square_metres_for_ladscaping = float(input())
price_for_landscaping_the_whole_yard = square_metres_for_ladscaping * 7.61
discaunt = price_for_landscaping_the_whole_yard * 0.18
final_price = price_for_landscaping_the_whole_yard - discaunt

print(f"The final price is: {final_price} lv.")
print(f"The discaunt is: {discaunt} lv.")