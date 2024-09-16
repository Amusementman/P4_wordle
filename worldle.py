word = "dingus"


#colors for printing
default = '\033[0m'
green = '\033[92m'
yellow = '\033[33m'

# #how color thing works
# print(green + "hello" + default) ; switched it so that hello is green but turns it back to default after

def generate_hint(guess):
    color = default
    hint = ""
    for i in range(5):
        if guess[i] ==  word[i]:
            # ^checks if letter is in right place
            color = green
        elif guess[i] in word:
            # ^ checks if letter is in word
            color = yellow
        else:
            color = default
        hint = hint + color + guess[i] + default
    return hint

def game_loop():
    user_guess = ""
    for i in range(6):
        user_guess = input("give a guess at the word: ")
        print(generate_hint(user_guess))
        if user_guess == word:
            print("Congrats! You super smart")
            break

game_loop()