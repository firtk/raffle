import random
import os

os.system("cls")

sys_random = random.SystemRandom()

choices = []
print("Enter the choices one by one [Type -1 when you done]: ")

choice = ""
counter = 1
while not choice == "-1":
    choice = str(input("{}. Choice: ".format(counter)))

    if counter <= 2 and choice == "-1":
        print("Enter more than one choice.")
        choice = ""
        continue

    if choice not in choices:
        choices.append(choice)
        counter += 1
    else:
        print("Please enter different choice.")
choices.pop() # Deletes last item from the list

number_of_draws = 1
while not(number_of_draws >= 3 and number_of_draws % 2 == 1):
    try:
        number_of_draws = input("Enter how many times do you want the raffle to be drawn ?\n[Press 'enter' for only one times]: ")
        if not number_of_draws:
            number_of_draws = 1
            break
        else:
            number_of_draws = int(number_of_draws)
        if not(number_of_draws >= 3 and number_of_draws % 2 == 1):
            raise ValueError
    except ValueError:
        print("Please enter odd number greater or equal to 3.")

if number_of_draws == 1:
    winner = sys_random.choice(choices)
    print("Winner: {}".format(winner))
else:
    results = []
    while True:
        result = sys_random.choice(choices)
        results.append(result)
        if results.count(result) == ( int(number_of_draws) - ( (int(number_of_draws) -1) / 2) ):
            print("\nWinner: {}, won by {} times".format(result, results.count(result)))
            break
input("\nPress any key for leaving...")
