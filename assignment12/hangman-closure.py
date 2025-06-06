def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        nonlocal guesses
        guesses.append(letter)
        result = ""
        for char in secret_word:
            if char in guesses:
                result += char
            else:
                result += "_"
        print(result)
        return "_" not in result
    return hangman_closure

if __name__ == "__main__":
    word = input("Enter the secret word: ").lower()
    game = make_hangman(word)

    while True:
        guess = input("Guess a letter:").lower()
        if game(guess):
            print("You won!")
            break
