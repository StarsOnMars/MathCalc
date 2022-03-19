# Marvins Rochemont, Prof. Osheroff, COP1500
# A simple program for math functions, basically a calculator

# Main issue of code currently is that every input is being used with the selection, which leads to confusion.
# Could have simple operations scrapped for more "higher learning" formulas. This would be the prototype, essentially.


# Main Intro
def main():
	print("Welcome to the Math Manager!")
	start = input("Would you like to start?: ")
	if (start.startswith("Y")) or (start.startswith("y")):
		print("Great!")
		menu1()
	else:
		print("Goodbye!")


# Menu


def menu1():
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


def menu2():
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


def menu3():
	usr_select3 = input("Exponentiation, Comparisons, Random Number Generator, more")
	if (usr_select3 == "exponentiation") or (usr_select3 == "Exponentiation"):
		calc_exponent()
	elif (usr_select3 == "comparisons") or (usr_select3 == "Comparisons"):
		calc_compare()
	elif (usr_select3 == "random number generator") or (usr_select3 == "rng") or (usr_select3 == "Random number generator") or (usr_select3 == "Random Number Generator") or (usr_select3 == "RNG"):
		randomng()
	elif (usr_select3 == "more") or (usr_select3 == "More"):
		menu4()
	elif (usr_select3 == "back") or (usr_select3 == "Back"):
		menu3()
	else:
		print("Invalid choice. Try again or type 'back' to leave the menu.")

		
# Calculation Hub


def calculate_sum():
	add1 = int(input("What's the first number you'd like to add?: "))
	add2 = int(input("What's the second number you'd like to add?: "))
	summ = add1 + add2
	print(add1, "+", add2, "=", summ)


def calculate_differ():
	sub1 = int(input("What's the number you want to subtract?: "))
	sub2 = int(input("What's the number you want to subtract it by?: "))
	differ = sub1 - sub2
	print(sub1, "-", sub2, "=", differ)


def calculate_product():
	factor1 = int(input("What's the first factor?: "))
	factor2 = int(input("What's the second factor?: "))
	product = factor1 * factor2
	print(factor1, "*", factor2, "=", product)


def calculate_quotient():
	dividend = int(input("What's the dividend?: "))
	divisor = int(input("What's the divisor?: "))
	quotient = dividend / divisor
	print(dividend, "/", divisor, "=", quotient)


def calculate_mass():
	density = int(input("What's the density of the object?: "))
	volume = int(input("What's the volume of the object?: "))
	mass = density / volume
	print("The mass of the object is", mass)


def calculate_density():
	mass = int(input("What's the mass of the object?: "))
	volume = int(input("What's the volume of the object?: "))
	density = mass / volume
	print("The density of the object is", density)


def calculate_volume():
	mass = int(input("What's the mass of the object?: "))
	density = int(input("What's the density of the object?: "))
	volume = mass / density
	print("The volume of the object is", volume)


# Call to Main


main()
