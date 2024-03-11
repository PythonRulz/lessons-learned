price = 50
total = 0
loop = True
coin_list = [5,10,25]

while loop == True:
    coin = int(input("Insert Coins: "))
    if coin in coin_list:
        total += coin
    else:
        print(f"5 10 or 25 only please")
    due = price - total

    if due > 0:
        print(f"amount due: {abs(due)}")
    elif due == 0:
        print("")

    else:
        due <= 0
        due *= -1
        print(f"change owed: {due}")
        loop = False
        break
