X, Y , Z = map(int, input().split())
total_cost_with_trainer = X+Y   
if total_cost_with_trainer <= Z:
    result = 2
elif X <= Z:
    result = 1
else:
    result = 0
print(result)    
