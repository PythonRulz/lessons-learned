def get_input():
    num_in = []
    user_inp = input("Enter a number of any type 'finish' to quit: \n--> ").upper()
    while user_inp != "FINISH":
        if user_inp == 'FINISH':
            continue
        num_in.append(user_inp)
        user_inp = input("--> ").upper()
    return num_in

def count_nums(user_list):
    nums_to_count = ['1', '5', '10']
    for num in nums_to_count:
        if num == '1':
            one = user_list.count(num)
        elif num == '5':
            five = user_list.count(num)
        else:
            ten = user_list.count(num)
    return(one, five, ten)

def output_result(result):
        print(f"The number '1' appears {result[0]} times in the list")
        print(f"The number '5' appears {result[1]} times in the list")
        print(f"The number '10' appears {result[2]} times in the list")
user_list = get_input()
number_count = count_nums(user_list)
output_result(number_count)


        
        
        
    
