import random

words = ("rock", "telephone", "elephant", "scorpio", "dark", "occupation", "wine", "introduction", "tropical", "opponent", "entitlement", "director", "referral", "charity", "timetable", "sculpture", "radiation", "delivery", "technique", "manufacturer", "trolley", "ignorance")
word = random.choice(words)
lives = len(word)
print("Your word has", len(word), "letters, you have", lives, "attempts to find it")
guess_letter = set()
attempts = 0

while lives > 0:
    found = True 
    for char in word:
        if char in guess_letter:
            print(char, end=" ")
        else:
            print("_", end=" ")
            found = False

    if found:
        print("\nCongratulations, you have found the word:", word)
        break

    guess = input("\nEnter a letter: ").lower()  
    if guess in guess_letter:
        print("You already guessed that letter.")
    else:
        guess_letter.add(guess)
        if guess in word:
            print("Correct!")
        else:
            print("Wrong, try again!")
            lives -= 1
            print("You have", lives, "attempts left")

if lives == 0:
    print("Sorry, you have run out of attempts. The word was:", word)
