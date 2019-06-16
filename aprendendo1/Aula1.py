import random
random_number = random.randint(1, 10)

DEBUG = True
CLOSE_THRESHOLD = 3
lives = 3
users_guess = None

if DEBUG == True:
    print("DEBUG: the answer is {}".format(random_number))
    
""""
def check_result(guess, answer, threshold):
    if guess == answer:
        return 1
    elif (answer - guess) < threshold:
        return 0
    else:
        return -1
assert check_result(5, 5, 3) == 1
assert check_result(4, 5, 3) == 0
assert check_result(5, 1, 3) == -1
if DEBUG:
    print("passing all tests!")
""""

while random_number != users_guess and lives > 0:
    number_input = input("Guess a number between 1 and 10: ")
    users_guess = int(number_input)

    results = check_results(users_guess, random_number, CLOSE_THRESHOLD)

    if random_number == users_guess:
        print("you win")

    elif abs(random_number - users_guess) < CLOSE_THRESHOLD:
        print("almost there! play again")

    else:
        print ("you loose")

    lives -= 1
    print("you have {} lives left".format(lives))

print("thank you for playing")

    


