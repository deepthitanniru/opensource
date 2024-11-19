n = int(input())
reversed_n = int(str(abs(n))[::-1]) * (1 if n > 0  else -1)
print(reversed_n if -(2**31 - 1) <= reversed_n <= (2**31 - 1) else 0)
