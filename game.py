import random
'''
word game! 

- get a n-letter target word
- for each 5 letter guesses
    - for each letter in word
        - mark not in target, in target wrong place, or right place
    - print result

'''
target_len = int(input("How many letters? "))

word_file = open("clean_words.txt", "r")
word_list = word_file.readlines()
filtered_list = list(filter(lambda x: len(x) == target_len + 1, word_list))

target_word = random.choice(filtered_list).rstrip()


matched = False
confirmed_excluded = []
confirmed_matched = []
confused = []

qwerty = "qwertyuiopasdfghjklzxcvbnm"

while not matched:
    output_string = ""
    guess = input("Make your guess, fool: ")
    if guess == "surrender":
        print(target_word)
    elif guess == target_word:
        print("You win!!")
        matched = True
    else:
        confirmed_matched = []
        confused = []

        for idx, letter in enumerate(guess):
            output_string += letter
            if letter not in target_word:
                confirmed_excluded.append(letter)
                output_string += "(x)"
            else: # check if location is right
                if target_word[idx] == letter:
                    confirmed_matched.append(letter)
                else: # wrong place!
                    confused.append(letter)
                    output_string += "(?)"
            output_string += " "
        
        print("\nResult: " + output_string)

        print("")
        print("Confirmed excluded: " + " ".join(list(filter(lambda x: x in confirmed_excluded, qwerty))))
        print("Out of place: " + " ".join(list(filter(lambda x: x in confused, qwerty))))
        print("Not Guessed: " + " ".join(list(filter(lambda x: x not in confused + confirmed_excluded, qwerty))))

        print("")

