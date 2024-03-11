with open('yoda.txt', 'w') as f:
    f.write("powerful")
    f.seek(0)
    print(f.read())
    
