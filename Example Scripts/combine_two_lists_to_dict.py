brands = ['Nike', 'Adidas', 'Asics', 'Hoka', 'Other(Puma, Reebok, Saucony)']
inventory = [180, 395, 250, 170, 45, 30, 40]

inv_dict = {brands[i] : inventory[i] for i in range(len(brands))}
inv_dict['Other(Puma, Reebok, Saucony'] = inventory[4]+inventory[5]+inventory[6]
print(inv_dict)
done_searching = False

while not done_searching:
    search = input("Search brand: ").title()
    if search == 'Other':
       print(f"{search} (Puma, Reebok, Saucony): {inv_dict['Other(Puma, Reebok, Saucony)']} pairs in stock\n")
    elif search not in brands:
        print(f"{search}: Not available\n")        
    else:
        print(f"{search}: {inv_dict[search]} pairs in stock\n")
        search_again = input("'Q' to quit or any other key to search again: ").upper()
        if search_again == 'Q':
            break
print('Goodbye')

    
        
