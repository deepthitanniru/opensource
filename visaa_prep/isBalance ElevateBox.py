def calculate_balance_array(arr):
    n = len(arr)
    balance_array = []
    for i in range(n):
        left_weight = sum(arr[:i])
        right_weight = sum(arr[i+1:])
        balance = abs(left_weight - right_weight)
        balance_array.append(balance)
    return balance_array
n = int(input())
arr = list(map(int, input().split()))
result = calculate_balance_array(arr)
print(*result)
