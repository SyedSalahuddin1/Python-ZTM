import random
secret = random.randint(1, 100) 
attempts = 0

while True:
    user_guess = input("Please guess the number or 'q' to quit: ")
    if user_guess.lower() == "q":
        print("Game Exited!")
        break
    
    try:
        user_guess = int(user_guess)
    except ValueError:
        print("Please enter a number❌❌.")           
        continue
    
    attempts += 1

    if user_guess == secret:
        print(f"You guessed the correct answer, The number was {secret}!")
        print(f"You took {attempts} to guess the correct answer!")
        continue
    elif user_guess > secret:
        print("Too High! try lower.")
    else: 
        print("Too Low! try higher.")

