# LOOPS (16pts TOTAL)

# PROBLEM 1 (Fibonacci - 4pts)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.

sequence = 0
fib1 = 1
fib2 = 0
while sequence <= 1000:
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
    sequence = fib3
    if sequence <= 1000:
        print(fib3)


# PROBLEM 2 (Dice Sequence - 6pts)
# You roll five six-sided dice, one by one.
# What is the probability that the value of each die
# is greater than OR EQUAL TO the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.

print("\n")

from random import *

trial = 0
test = 0
success = 0

while trial <= 10000:
    test = 0
    dice1 = randrange(1, 7)
    dice2 = randrange(1, 7)
    if dice2 >= dice1:
        test += 1
    dice3 = randrange(1, 7)
    if dice3 >= dice2:
        test += 1
    dice4 = randrange(1, 7)
    if dice4 >= dice3:
        test += 1
    dice5 = randrange(1, 7)
    if dice5 >= dice4:
        test += 1
    if test == 4:
        success += 1
    trial += 1

print(success, "out of 10000 were successful")


# PROBLEM 3 (Number Puzzler - 6pts)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve. 

print("\n")

for a in range(1,10):
    for b in range(10):
        for c in range(10):
            for d in range(1,10):
                num = str(a) + str(b) + str(c) + str(d)
                num_reverse = str(d) + str(c) + str(b) + str(a)
                print(num, num_reverse)