print ("lets play guess this word.") #time to play

secret_word = input("Enter a secret word to guess: ") # gather the secret word
secret_word = secret_word.lower() # convert to lower
guesses = "" # this is the string that will show what has been guessed later
turns = 6 # how many chances they get to enter a wrong character.

# a very very tricky while loop.
while turns > 0:         # will be true until the turns counter makes turns = 0
    count = 0   # this count determines wether to print _ or the character
    for char in secret_word: # looking at characters in the secret word
        if char in guesses: #  this is used to display the correct letters and _'s
            print (char, end="")
        else:
            print ("_ ",end="") # this print the _ for every char in secretword
            count += 1   # ends the for loop continues to the next part
    if count == 0: # you won the game end the loop.
        print ()
        print ("You win")
        break
    print ()
    print ()
    print ()
    guess = input("guess a character:")
    count2 = 0
    if len(guess) > 1:
        count2 += 1
        while count2 > 0:
            print ("you can only guess 1 character at a time")
            count2 -= 1
    guess = guess.lower()  #lower        # it is time to guess the letters.
    guesses += guess
    if guess not in secret_word:  # if statement for if guess is not in word
        turns -= 1       # subtract from turns
        print ()
        print ()
        print ("Wrong")
        print ("Letters guessed so far: ",guesses) # end of loop show guessed letters
        print ("You have", + turns, 'more guesses') # show turns left
        if turns == 0:   # END GAME
            print ("The word was",secret_word,"You Loose")
