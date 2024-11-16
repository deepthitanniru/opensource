year = int(input())
print("YES" if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else"NO")
