import random

MARGIN = 2
EASY_DIFF = '1'
MED_DIFF = '2'
HARD_DIFF = '3'
QUIT_OPTION = '4'

def guessing_game():
    difficulty = input("How many characters?\n1. Easy (4-5 characters) \n2. Medium (6 characters) \n3. Hard (7-8 characters)\n4. Quit\nInput the number of your selection: ")

    while (difficulty != QUIT_OPTION):
        if difficulty == EASY_DIFF:
            easy_difficulty(MARGIN)
            difficulty = input("\nHow many characters?\n1. Easy (4-5 characters) \n2. Medium (6 characters) \n3. Hard(7-8 characters)\n4. Quit\nInput the number of your selection: ")
     
        elif difficulty == MED_DIFF:
            med_difficulty(MARGIN)
            difficulty = input("\nHow many characters?\n1. Easy (4-5 characters) \n2. Medium (6 characters) \n3. Hard(7-8 characters)\n4. Quit\nInput the number of your selection: ")
     
        elif difficulty == HARD_DIFF:
            hard_difficulty(MARGIN)
            difficulty = input("\nHow many characters?\n1. Easy (4-5 characters) \n2. Medium (6 characters) \n3. Hard(7-8 characters)\n4. Quit\nInput the number of your selection: ")
     
        else:
            print('Make sure your input is a number!')
            difficulty = input("\nHow many characters?\n1. Easy (4-5 characters) \n2. Medium (6 characters) \n3. Hard(7-8 characters)\n4. Quit\nInput the number of your selection: ")

    print("Thanks for playing!")

def easy_difficulty(margin):
    easy_words = ["onyx", "brim", "wisp", "spire", "crypt","rune", "veil", "muse", "gale", "hymn"]

    e_word = random.choice(easy_words)

    start_of_word = e_word[0:margin]
    blanks_of_word = '_' * len(e_word[margin:])
    scrambled = scramble_word(e_word, margin)

    print(f"{scrambled}")
    print(f"{start_of_word}{blanks_of_word}")

    ans = input("Finish the word: ")

    while (ans.lower() != e_word):
        print(f"\n{start_of_word}{blanks_of_word}")
        ans = input("Nope! Try again: ")
    print("\nYou got it! Yippee!")

def med_difficulty(margin):
    medium_words = ["cinder", "riddle", "vellum", "locus", "quill","meadow", "goblet", "oracle", "mantle", "seraph"]

    m_word = random.choice(medium_words)
    start_of_word = m_word[0:margin]
    blanks_of_word = '_' * len(m_word[margin:])

    scrambled = scramble_word(m_word, margin)

    print(f"{scrambled}")
    print(f"{start_of_word}{blanks_of_word}")

    ans = input("Finish the word: ")

    while (ans.lower() != m_word):
        print(f"\n{start_of_word}{blanks_of_word}")
        ans = input("Nope! Try again: ")
    print("\nYou got it! Wow!")

def hard_difficulty(margin):
    hard_words = ["obsidian", "chimera", "verdant", "bastion", "zephyr","phantom", "labyrinth", "tempest", "runestone", "eclipse"]

    h_word = random.choice(hard_words)
    start_of_word = h_word[0:margin]
    blanks_of_word = '_' * len(h_word[margin:])

    scrambled = scramble_word(h_word, margin)

    print(f"{scrambled}")
    print(f"{start_of_word}{blanks_of_word}")

    ans = input("Finish the word: ")

    while (ans.lower() != h_word):
        print(f"\n{start_of_word}{blanks_of_word}")
        ans = input("Nope! Try again: ")
    print("\nYou got it! Amazing!")

def scramble_word(word, margin):
    scrambled_word = word

    while word[0: margin] == scrambled_word[0: margin]:
        characters = list(word)
        random.shuffle(characters)

        scrambled_word = ''.join(characters)

    return scrambled_word


guessing_game()
