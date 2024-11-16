A , B, C, X = map(int, input().split())
print("YES" if X in [A + B, A + C, B + C] or X < max(A + B, A + C, B + C) else "NO")
