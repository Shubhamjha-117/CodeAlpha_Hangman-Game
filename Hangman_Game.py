import random

words = ["python","computer","developer","keyboard","task"]

word = random.choice(words)

display = ["_"]*len(word)

attempts = 6
guessed_letters = []

print(f"You have {attempts} attempts to Guess the right word :")
print(" ".join(display))
while(attempts > 0 and "_" in display):
    
    user = input("Enter a letter :").lower()
    if len(user) != 1 or not user.isalpha():
        print("Enter a Valid Letter !!\n")
        continue
    if user in guessed_letters:
        print(f"You have already guessed {user},try another letter !!\n")
        continue
    guessed_letters.append(user)
    if user in word :
        for index,letter in enumerate(word) :
            if letter == user :
                display[index] = user 
                print(f"Correct Guess :{user} is in word !\n")
    else:
        print(f"Incorrect Letter :{user}")
        attempts -= 1
        print(f"You have {attempts} attempts left !!\n")
    print("Current Word :"," ".join(display))
if "_" not in display:
    print("Congratulation , You guessed the word .",word)
else:
    print(f"You Lose !!,correct word was {word}")

         
    