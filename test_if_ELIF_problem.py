# You need to make a program to take a year as input and output "Leap year" if it’s a leap year,
# and "Not a leap year", if it’s not.

# 1) If the year is evenly divisible by 4, go to step 2. Otherwise, the year is NOT leap year.
# 2) If the year is evenly divisible by 100, go to step 3. Otherwise, the year is a leap year.
# 3) If the year is evenly divisible by 400, the year is a leap year. Otherwise, it is not a leap year.

# Sample Input
# 2000

# Sample Output
# Leap year

# Use the modulo operator % to check if the year is evenly divisible by a number.


year = int(input())
if year % 4 != 0:
    print("Not a leap year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 == 0:
    print("Leap year")
elif year % 400 != 0:
    print("Not a leap year")

