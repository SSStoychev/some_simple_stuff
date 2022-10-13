page_numbers = int(input())
pages_per_our = int(input())
days = int(input())

all_book_time = page_numbers // pages_per_our
read_day_hours = all_book_time // days
print(read_day_hours)