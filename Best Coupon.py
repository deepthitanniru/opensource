X = int(input())
discount_10_percent = X*0.10
discount_flat_100 = 100
if discount_10_percent>discount_flat_100:
    final_amount=X-discount_10_percent
else:
    final_amount = X-discount_flat_100
print(int(final_amount))
