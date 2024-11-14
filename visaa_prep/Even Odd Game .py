N = input()
digit_sum = 0
for digit in N:
    digit_sum += int(digit)
if digit_sum % 2 == 0:
    print("Vignesh")
else:
    print("Charan")
