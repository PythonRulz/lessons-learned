import random

words = ['EVAPORATE', 'RINGS', 'DICTIONARY', 'COMPUTER', 'FELLOWSHIP',
         'CAPITAL', 'ADDRESS', 'BEACH', 'RESORT', 'ISLAND', 'MOUNTAIN',
         'COUNTRY', 'TELEVISION', 'TEMPLE', 'DEFLECTION']

def game_play(word, guesses):
    hint = ''
    count = 0
    last_guess = guesses[-1]
    for letter in word:
        if letter in guesses:
            hint += letter
        else:
            hint += '-'
        if letter == last_guess:
            count += 1
    if count > 1:
        print(f"There are {count} \"{last_guess}\"'s in the word")
    elif count == 1:
        print(f"There is {count} \"{last_guess}\" in the word")
    else:
        print(f"There are no \"{last_guess}\"'s in the word")
    return hint

def main():
    secret_word = random.choice(words)
    guessed = False
    guesses = []
    length_word = len(secret_word)
    print(f"The word has {length_word} letters in it")
    while not guessed:
        
        user_guess = input("Guess a letter: ").upper()
        if user_guess in guesses:
            print("You've already guessed that letter")
        elif len(user_guess) == length_word:
            guesses.append(user_guess)
            if user_guess == secret_word:
                guessed = True
            else:
                print(f"Sorry that is incorrect")        
        elif len(user_guess) == 1:
            guesses.append(user_guess)
            res = game_play(secret_word, guesses)
            if res == secret_word:
                guessed = True
            else:
                print(res)
        else:
            print(f"Invalid Entry")
        
    print(f"You got it")

main()
        
    
