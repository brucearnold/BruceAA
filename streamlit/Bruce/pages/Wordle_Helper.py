word_list = []  # "alarm", "stray", "court", "happy"]


def load_words():
    global word_list
    # with open("newwordlist.txt","r") as f:
    #   contents = f.readlines()
    #   for line in contents:
    #     word_list.append(line)
    with open("wordlist.txt", "r") as f:
        content = f.read()
    word_list = content.split()
    print(len(word_list))


def list_words():
    global word_list
    for word in word_list:
        print(word)
    print(len(word_list))


def best_word():
    global word_list
    chosen_letters = input("which letters? ").upper()
    for word in word_list:
        matches = True
        # print(f"checking {word}")
        for letter in word:
            # print(f"checking {letter} in {letters}")
            if letter not in chosen_letters:
                # print(f"no {letter} in {letters}")
                matches = False
        if matches == True:
            print(word)


def remove_words():
    global word_list
    letter = input("remove words with which letter? ").upper()
    word_list = [word for word in word_list if letter not in word]
    # for word in word_list:
    #   print(f"{letter} in {word} is {letter in word}")


def exact_position():
    global word_list
    letter = input("confirm words with exact position? ").upper()
    pos = int(input("In which position? "))

    word_list = [word for word in word_list if word[pos - 1] == letter]


def approximate_position():
    global word_list
    letter = input("confirm words with some position? ").upper()
    word_list = [word for word in word_list if letter in word]


def somewhere_else():
    global word_list
    letter = input("which letter is somewhere else? ").upper()
    pos = int(input("but not in which position? "))
    word_list = [
        word for word in word_list
        if (letter in word and word[pos - 1] != letter)
    ]


def most_common_letters():
    global word_list
    letter_list = {}
    for word in word_list:
        for letter in word:
            if letter in letter_list:
                letter_list[letter] += 1
            else:
                letter_list[letter] = 1
    marklist = sorted(letter_list.items(), key=lambda x: x[1])
    sortdict = dict(marklist)
    print(sortdict)


load_words()

stop = False
while not stop:
    answer = input(
        "what do you want to do? \n[l]ist words, [r]emove words, [e]xact position, [a]pproximate position, [n]ot here but somewhere else, [b]est word\n"
    )
    if answer == "l":  # list
        list_words()
    elif answer == "r":  # remove
        remove_words()
    elif answer == "e":  # exact position
        exact_position()
    elif answer == "a":  # approximate
        approximate_position()
    elif answer == "n":  # not here but somewhere else
        somewhere_else()
    elif answer == "m":
        most_common_letters()
    elif answer == "s":
        load_words()
    elif answer == "b":
        best_word()
    else:
        stop = True
