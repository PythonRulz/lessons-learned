l1 = [67, 12, 46, 43, 13]

print(l1.index(43))
try:

    print(l1.index(44))
except ValueError:
    print(f"44 does not exist in the l1")
    
    

