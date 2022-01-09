word_file = open("words.txt", "r")
output_file = open("clean_words.txt", "w")
word_list = word_file.readlines()

for word in word_list:
    dupe = False
    for letter in word:
        if word.count(letter) > 1:
            dupe = True
    if not dupe:
        output_file.write(word)
