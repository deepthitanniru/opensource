def unique_elements(arr):
    seen = set()
    unique = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            unique.append(num)
    return unique

N = int(input())
arr = list(map(int, input().split()))
result = unique_elements(arr)
print(" ".join(map(str, result)))
