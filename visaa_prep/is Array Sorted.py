def is_sorted(n, arr):
    return 'true' if all(arr[i] <= arr[i+1] for i in range(n-1)) else 'false'

n = int(input())
arr = list(map(int, input().split()))
print(is_sorted(n, arr))
