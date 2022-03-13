import random
# guess user input
# function names guess_random_number()
# it has three parameters tries , start , stop
# Write a while loop that loops as long as tries is not equal to 0.
# Inside the while loop, print the number of tries remaining.
# Prompt the user to input a guess.


def guess_random_number(tries, start, stop):
    num = random.randint(start, stop)
    while tries != 0:
        guess = int(input(f"Guess a number between {start} and {stop}:"))
        print("Number of tries left: ", tries)
        tries = tries - 1

        if tries == 0:
            print("You have failed to guess the number: ", num)
            break
        elif (guess > num):
            print("Guess lower!")
        elif (guess < num):
            print("Guess higher!")
        elif(guess == num):
            print("You guessed the current number!")
            return


# driver code for task 2
guess_random_number(5, 0, 10)
# linear search
# Provide a parameter list of three parameters: tries, start , and stop. Assume that each of these will be passed an integer value.
# Inside the function:
# use for loop
# every time you make a comparison decrement the tries variable until
# there are no more tries left
# show the target # and success/ failure messages

# test task 2
# Comment out the task driver code for Task 1.
# Then write test driver code for this task at the bottom of your file, as follows:
# Call the guess_random_num_linear() function.
# Provide arguments such that the value of tries in the
#  function will be initialized to 5, and the random number
# will be generated in the range of 0 to 10 inclusive.
# Since there are 11 potential numbers, and the computer
#  only gets 5 tries, the computer will guess correctly around half the time,
#  and incorrectly the other ~half.
# Save your code, then run
# it multiple times to make sure you see both
#  failure and success cases, which should look
# similar to this:


def guess_random_num_linear(tries, start, stop):
    tries2 = tries
    num_guess = int(input("The number for the program to guess is: "))
    # now we can do a linear search to see if the program guessed the number\
    for start in range(tries):
        num = random.randint(int(start), int(stop))
        print("Number of tries left: ", tries2)
        print("The program is guessing... ", num)
        tries2 = tries2 - 1
        if (num == num_guess):
            return "The program has guessed the correct number!"

        elif tries2 == 0 and num != num_guess:
            return "The program has failed to guess the correct number."


print("\n\n")
print(guess_random_num_linear(5, 0, 10))
# Task 3: Guess the number programmatically using binary search.
# Write the code to generate a random number,
# then have your program guess it using binary search.

# Write a function named guess_random_num_binary().
# Provide a parameter list of three parameters: tries, start, and stop. Assume that each of these will be passed an integer value.
# Inside the function:
# Use the random module to generate a random number between the start and stop integers, inclusive.
# Revisit your exercise on binary search. Use what you learned there to implement a binary search algorithm for the program to guess the randomly generated target number, and print an appropriate success message if the correct number is guessed.
# As in the other tasks, only allow the number of guesses determined by the tries argument.
# If the program has not guessed the number using binary search within the number of tries allotted, print an appropriate failure message.

# Test Task 3
# Comment out the task driver code for Task 2.
# Then write test driver code for this task at the bottom of your file, as follows:
# Call the guess_random_num_binary() function.
# Provide arguments such that the value of tries in the function will be initialized to 5, and the random number will be generated in the range of 0 to 100 inclusive.
# Save and run your code. Again, the computer may or may not guess correctly before it runs out of tries. So you will need to run your code more than once to verify that it works for both cases. The result should be similar to this:
# binary search


def guess_random_num_binary(tries, start, stop):
    num = int(input("Random number to find: "))
    lower_bound = start
    upper_bound = stop
    while lower_bound <= upper_bound:
        middle = (lower_bound + upper_bound) // 2
        if middle == num:
            print("The program has guessed the correct number!")
            return
        if middle > num:
            upper_bound = middle - 1
            tries = tries - 1
            print("Guessing lower!")
        else:
            lower_bound = middle + 1
            print("Guessing higher!")
            tries = tries - 1
    return -1


print("\n\n")
guess_random_num_binary(5, 0, 100)
