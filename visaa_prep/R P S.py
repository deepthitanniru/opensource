v , c = input().split()
result = {"RS": "Vignesh", "PR": "Vignesh", "SP": "Vignesh", "SR": "Charan", "RP": "Charan", "PS": "Charan"}
print(result.get( v+ c, "NULL"))
