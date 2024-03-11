n = 1
penny = .001

while n <= 31:
    print(f"Day {n} = ${penny:,.3f}")
    penny += penny
    n += 1
