prev_day = 22120

def yesterday ():
    with open('previous_day_close.txt','w') as prev_d:
        prev_d.write(str(prev_day))
    print(prev_day)

    
    
