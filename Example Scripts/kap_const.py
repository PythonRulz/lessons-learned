import copy
KAP = 6174

def calculate_kaprekar(nums):
    
    nums2 = copy.deepcopy(nums)
    nums2.sort()
    nums.sort()
    nums.reverse()
    num1 = int(''.join(nums))
    num2 = int(''.join(nums2))
    result = (num1 - num2)
    print(f"\n{num1} - {num2} = {num1 - num2}\n")
    if result != KAP:
        result = list(str(result))
        if len(result) < 4:
            result.insert(0,'0')
            calculate_kaprekar(result)
            return 'Done'
        else:
            calculate_kaprekar(result)
            return 'Done'



def main():
    
    valid = False
    while not valid:
        user_digits = input('''Enter a 4 digit number  All 4 digits must not be the same: ''')

        if len(user_digits) == 4 and user_digits.isdigit():
            if all(ele == user_digits[0] for ele in user_digits):
                print("\nDigits must not all be the same!")

            else:
                valid = True
        else:
            print("4 unique digits")
    print(calculate_kaprekar(list(user_digits)))

main()
    
