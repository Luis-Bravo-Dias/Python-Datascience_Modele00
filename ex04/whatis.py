import sys

argc = len(sys.argv)

if (argc > 1):
	try:
		assert argc <= 2,"AssertionError: more than one argument is provided"
		value = int(sys.argv[1])

		if (value % 2) == 0:
			print("I'm Even.")
		else:
			print("I'm Odd.")
	except ValueError as error:
		print("AssertionError: argument is not an integer")
	except AssertionError as error:
		print(error)