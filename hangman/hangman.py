import random
print("HANGMAN")
game=""
while game!="play" and game!="exit":
    game=input('Type "play" to play the game, "exit" to quit')
if game=="play":
    attempts=8
    word=["python", "java", "javascript", "php"]
    game_word=word[random.randint(0,3)]
    user_word="-"*(len(game_word))
    user_word1=""
    a=0
    user_letter_old=""
    while attempts!=0:
        if user_word==game_word:
            a=1
            break
        print(" ")
        print(user_word)
        user_letter=input("Input a letter:")
        if len(user_letter)!=1:
            print("You should input a single letter")
        elif user_letter.isupper()==True:
            print("Please enter a lowercase English letter")
        elif user_letter==user_letter_old:
            print("You've already guessed this letter")
        elif user_letter in game_word and user_letter in user_word:
            print("You've already guessed this letter")
        elif user_letter in game_word:
            for i in range(len(user_word)):
                if user_letter in game_word[i]:
                    user_word1=user_word1+user_letter
                else:
                    user_word1=user_word1+user_word[i]
            user_word=user_word1
            user_word1=""
        else:
            print("That letter doesn't appear in the word")
            attempts=attempts-1
        user_letter_old=user_letter
    if a!=1:
        print("You lost!")
    else:
        print("You guessed the word!")
        print("You survived!")
else:
    print("")
#game_word_answer=game_word[:3]+"-"*(len(game_word)-3)