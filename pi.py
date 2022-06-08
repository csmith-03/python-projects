# Name: Channing Smith
# pi.py
#
# Problem: The purpose of this program is to precisely calculate pi
# from a given input of N using 3 different series and also calculate
# the approximation error.
#
# Inputs: The user will input N which the higher the input, the more
# accurate the approximation of pi will be.
#
# Outputs: The outputs will be the approximation of pi using 3
# different series and also the approximation error.
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work, but I
# received help from Anthony and tutor.
import math
# This will use the input of N throughout all three series using a list.
def entering_n():
    # Gets input from user for N
    n = int(input("How many terms would you like to enter?"))
    functions = [pi_wallis , pi_gregory , pi_nilakantha , pi_euler]
    for func in functions:
        func(n)


def pi_wallis(n):
    total = 1
    denom = 1
    num = 0
    # Below is the loop that calculates numerator and
    # denominator patterns.
    for i in range(n):
        denom += i % 2 * 2
        num += (i - 1) % 2 * 2
        # value is used to represent the entire fraction
        value = num / denom
        # This print statement is optional but allows me to see the
        # pattern of each value
        print(num , "/" , denom)
        total *= value
    total = total * 2
    # calculates approx error
    approximation_error = abs(math.pi - total)
    print("Wallis Approximation:" , total)
    print("Approximation Error:" , approximation_error)

def pi_gregory(n):
    # Start total at 0
    total = 0
    for i in range(n):
        # Numerator is constantly 4, so num = 4 sets that as the
        # permanent value for num.
        num = 4
        # The denom at i is being multiplied by 2 and adding 1 each
        # time looped through.
        denom = (2 * i) + 1
        # The value definition calculates the alternating sequence.
        value = (num / denom) * (-1) ** i
        total += value
        # This print statement is optional but allows me to see the
        # pattern of each value
        print(num , "/" , denom)
    # calculates approx error
    approximation_error = abs(math.pi - total)
    print("Gregory Approximation:" , total)
    print("Approximation Error:", approximation_error)

def pi_nilakantha(n):
    total = 3
    # Set the numerator equal to -4 so that the alternating sequence
    # starts negative.
    num = -4
    for i in range(1 , n , 1):
        num *= -1
        # Below is splitting the denominator into 3 sections and finding
        # a sequence for each one.
        denom_1 = (2 * i)
        denom_2 = denom_1 + 1
        denom_3 = denom_2 + 1
        # This denom calciulates all three denominators
        # multiplied together.
        denom = denom_1 * denom_2 * denom_3
        # Value will be used to represent the entire fraction including
        # numerator and denominator.
        value = (num / denom)
        total += value
        # This print statement is optional but allows me to see the
        # pattern of each value
        print(num , "/" , denom)
    # calculates approx error
    approximation_error = abs(math.pi - total)
    print("Nilakantha Approximation:" , total)
    print("Approximation Error:", approximation_error)


def pi_euler(n):
    total = 0
    # Set denom equal to 1 because it starts at 1 and increases
    # by 1 each time.
    denom = 1
    # The loop will start at 1 and increase by 1.
    for i in range(1 , n , 1):
        num = 1
        # The denom is raised to the 2nd power.
        denom = (i ** 2)
        # Value will be used to represent the entire fraction including
        # numerator and denominator.
        value = num / denom
        total += value
        # This print statement is optional but allows me to see the
        # pattern of each value
        print(num, "/", denom)
    # calculates approx error
    approximation_error = abs(math.pi - total)
    # Uses sqrt to take the square root and multiply by 6 to get a full
    # pi instead of pi ^ 2 / 6.
    print("Euler Approximation:" , math.sqrt(total * 6))
    print("Approximation Error:", approximation_error)




def main():
    entering_n()


main()
