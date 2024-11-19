N = int(input())
matrix = [input().split() for _ in range(N)]
for row in matrix:
    print(*row[::-1])
