import random

start = int(input("Beginning: "))
end = int(input("End: "))

secret_number = random.randint(start, end)
tries = 1

while True:
    guess = int(input("Enter Guess: "))

    if guess < secret_number:
        print("Ehh Close GO big")
        tries+=1
    elif guess > secret_number:
        print("Awhhh Fuckk Too big 😫 Go smaller")
        tries+=1
    else:
        print(f"Yeahhhh baby that's the number 😘\nYou have Tried = {tries}")
        break