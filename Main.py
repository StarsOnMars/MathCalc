""" Math Manager!™
A simple program for math functions, basically a calculator. """
__author__ = "Marvins Rochemont"


# Modules
import random


# Menus
def main():
    """
    Used to start the program.
    """
    print("Welcome to the Math Manager!")
    start = input("Would you like to start, yes or no?: ")
    if (start.startswith("Y")) or (start.startswith("y")):
        print("Great!")
        menu1()
    elif start == "":
        print("Please enter a response.")
        main()
    else:
        print("Goodbye!")


# Menu
def menu1():
    """
    The first menu system for the program, allowing for simple choices to be made.
    """
    usr_select = input("Add, Subtract, Multiply, Divide or more?: ")

    if (usr_select == "Add") or (usr_select == "add"):
        calculate_sum()
        menu1()

    elif (usr_select == "Subtract") or (usr_select == "subtract"):
        calculate_differ()
        menu1()

    elif (usr_select == "Multiply") or (usr_select == "multiply"):
        calculate_product()
        menu1()

    elif (usr_select == "Divide") or (usr_select == "divide"):
        calculate_quotient()
        menu1()

    elif (usr_select == "more") or (usr_select == "More"):
        menu2()

    elif (usr_select == "back") or (usr_select == "Back"):
        main()
    else:
        print("Invalid choice. Try again or enter 'back' to leave the menu.")
        menu1()


def menu2():
    """
    The second menu system used for slightly more advanced calculations.
    """
    usr_select2 = input("Mass, Density, Volume, or more?: ")

    if (usr_select2 == "Mass") or (usr_select2 == "mass"):
        calculate_mass()
        menu1()

    elif (usr_select2 == "Density") or (usr_select2 == "density"):
        calculate_density()
        menu1()

    elif (usr_select2 == "Volume") or (usr_select2 == "volume"):
        calculateVolume()
        menu1()

    elif (usr_select2 == "More") or (usr_select2 == "more"):
        menu3()

    elif (usr_select2 == "back") or (usr_select2 == "Back"):
        menu1()

    else:
        print("Invalid choice. Try again or enter 'back' to leave the menu.")
        menu2()


def menu3():
    """
    The third menu system used for more eccentric uses, such as the Random Number Generator.
    """
    usr_select3 = input("Exponentiation, Comparisons, Random Number Generator (RNG), more?: ")
    if (usr_select3 == "exponentiation") or (usr_select3 == "Exponentiation"):
        calc_exponent()
    elif (usr_select3 == "comparisons") or (usr_select3 == "Comparisons"):
        calc_compare()
    elif (usr_select3 == "random number generator") or (usr_select3 == "rng") or (usr_select3 == "RNG"):
        randomng()
    elif (usr_select3 == "more") or (usr_select3 == "More"):
        menu4()
    elif (usr_select3 == "back") or (usr_select3 == "Back"):
        menu2()
    else:
        print("Invalid choice. Try again or type 'back' to leave the menu.")
        menu3()


def menu4():
    """
    The last menu system used for mainly evaluation work.
    """
    usr_select4 = input("Integration Project Eval, Credits, or go back?: ")
    if (usr_select4 == "Integration") or (usr_select4 == "Integration Project Eval"):
        integrationproj()
    elif (usr_select4 == "Credits") or (usr_select4 == "credits"):
        credit_list()
    elif (usr_select4 == "back") or (usr_select4 == "Back"):
        menu3()
    else:
        print("Invalid choice. Try again or type 'back' to leave the menu.")
        menu4()


# Calculation Hub


def calculate_sum():
    """
    This function calculates two values given by the user and outputs a sentence with the answer.
    """
    print("Can't take values that are in fraction or decimal form.")
    add1 = int(input("What's the first number you'd like to add?: "))
    add2 = int(input("What's the second number you'd like to add?: "))
    summ = add1 + add2
    print(add1, "+", add2, "=", summ)
    menu1()


def calculate_differ():
    """
    This function subtracts two values given by the user and outputs a sentence with the answer.
    """
    print("Can't take values that are in fraction or decimal form.")
    sub1 = int(input("What's the number you want to subtract?: "))
    sub2 = int(input("What's the number you want to subtract it by?: "))
    differ = sub1 - sub2
    print(sub1, "-", sub2, "=", differ)
    menu1()


def calculate_product():
    """
    This function multiplies two values given by the user and outputs a sentence with the answer.
    """
    print("Can't take values that are in fraction or decimal form.")
    factor1 = int(input("What's the first factor?: "))
    factor2 = int(input("What's the second factor?: "))
    product = factor1 * factor2
    print(factor1, "*", factor2, "=", product)
    menu1()


def calculate_quotient():
    """
    This function divides two values given by the user and outputs a sentence with the answer.
    """
    print("Can't take values that are in fraction or decimal form.")
    dividend = int(input("What's the dividend?: "))
    divisor = int(input("What's the divisor?: "))
    quotient = dividend / divisor
    print(dividend, "/", divisor, "=", quotient)
    menu1()


def calculate_mass():
    """
    This function finds the mass of an object, given the density and volume.
    The density is divided by the volume and the answer is output via a sentence.
    """
    density = float(input("What's the density of the object?: "))
    volume = float(input("What's the volume of the object?: "))
    mass = density / volume
    print("The mass of the object is", mass)
    menu2()


def calculate_density():
    """
    This function finds the density of an object, given the mass and volume.
    The mass is divided by the volume and the answer is output via a sentence.
    """
    mass = float(input("What's the mass of the object?: "))
    volume = float(input("What's the volume of the object?: "))
    density = mass / volume
    print("The density of the object is", density)
    menu2()


def calculate_volume():
    """
    This function calculates the volume of an object, given the density and mass.
    The mass is divided by the density, and the answer is output via a sentence.
    """
    mass = float(input("What's the mass of the object?: "))
    density = float(input("What's the density of the object?: "))
    volume = mass / density
    print("The volume of the object is", volume)
    menu2()


def calc_exponent():
    """
    This function can calculate the value of a number raised by an exponent.
    It takes the values given by the user for the base and power and raises that number to the power given.
    """
    base = int(input("What's the number you wanna raise?: "))
    power = int(input("What's the number you wanna raise it to?: "))
    expo = base ** power
    print(base, "to the power of", power, "is", expo)
    menu3()


def calc_compare():
    """
    This function is a simple comparison function for fun.
    The user inputs two numbers, and it tells you which one is larger, smaller, or equal to each other.
    """
    num1 = int(input("What's the first number you want to compare?: "))
    num2 = int(input("What's the second number you want to compare?: "))
    if num1 > num2:
        print(num1, "is greater than", num2)
    elif num1 < num2:
        print(num1, "is less than", num2)
    elif num1 == num2:
        print(num1, "is equal to", num2)
    else:
        print("Error: Invalid numbers.")
    menu3()


def randomng():
    """
    This function is a random number generator. It's my favorite one because it can be set to any parameter set,
    and is useful for things such as Dungeons and Dragons, for dice rolls.
    """
    val1 = int(input("What's the lowest number it can generate?: "))
    val2 = int(input("What's the highest number it can generate?: "))
    rand_num = random.randint(val1, val2)
    print("The random number generated is:", rand_num)
    menu3()


def integrationproj():
    """
    This menu is designed for things that couldn't fit in the program or that I couldn't see how to put it in.
    It ends up activating different functions to show that I understand what's needed.
    """
    print("This section is designed to be filled for things I wasn't able to fill up.")
    print("1. Modulus + Floor Division\n 2. Loops\n 3. Number Guesser")
    usr_choice = input("Please enter the appropriate number here: ")
    if usr_choice == "1":
        intprojblock1()

    elif usr_choice == "2":
        intprojblock2()

    elif usr_choice == "3":
        intprojblock3()

    elif (usr_choice == "back") or (usr_choice == "Back"):
        menu4()
    else:
        print("Invalid selection, either type 'back' or choose the appropriate number.")
        integrationproj()


def credit_list():
    """
    This function is solely for a credits list I wanted to add.
    """
    print("Author: Marvins Rochemont")
    print("Math Manager!™ Copyright 2022")
    print("For Prof. Osheroff's Intro to Computer Science. COP1500, Spring 2022.")
    print("Written in Python.")
    menu4()


def intprojblock1():
    """
    This function is to satisfy the modulus and floor division parameters of the project.
    """
    num_choice1 = int(input("Please input one number: "))
    num_choice2 = int(input("Please input another number: "))
    modu = num_choice1 % num_choice2
    floor_div = num_choice1 // num_choice2
    print("The modulus of", num_choice1, "and", num_choice2, "is", modu)
    print("The remainder of", num_choice1, "and", num_choice2, "is", floor_div)
    integrationproj()


def intprojblock2():
    """
    This function is to satisfy the loop parameters of the project.
    """
    print("Watch a number get looped for your enjoyment!")
    looped_number = int(input("Which number do you want to see over and over?: "))
    loop_duration = int(input("How long should it go on for?: "))
    num_loop = 0
    for x in range(loop_duration):
        print(x)
        if x == looped_number:
            print("Done!", num_loop, "amount of loops done.")
        num_loop += 1
        integrationproj()


def intprojblock3():
    digit = random.randint(1, 10)
    print("Multiple tries to get it right. A value between 1 and 10.")
    guess = int(input("What would the number be?: "))
    while guess != digit:
        print("Wrong answer. Try again.")
        guess = (int(input("What would the number be?: ")))

    print("You got the answer!")
    integrationproj()

# Call to Main


if __name__ == "__main__":
    main()
