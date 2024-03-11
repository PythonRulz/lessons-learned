for num in range (1, 11):
    print(f"2 x {num} = ", end='')
    x = (input())
    if x.isalpha:
        print("Wrong, numbers only please")
    elif x != str(num * 2):
        print("Incorrect")
        print("The correct answer is:", (num * 2))
    elif x == str(num * 2):
        print("Correct")
    else:
        print("Wait")
