import sys

def print_count(str):
	"""
	Displays the sums of total characters, upper-case characters, lower-case characters,
	punctuation characters, digits and spaces of a string that receives as an argument.
	"""
	string = str
	upper_letters = 0
	lower_letters = 0
	p_marks = 0
	spaces = 0
	digits = 0

	punctuation = ".,;:!?\"'()]{[}-"

	for char in range(len(string)):
		if string[char].isupper():
			upper_letters += 1
		elif string[char].islower():
			lower_letters += 1
		elif string[char] in punctuation:
			p_marks += 1
		elif string[char].isspace():
			spaces += 1
		elif string[char].isdigit():
			digits += 1

	print("The text contains", len(string), "characters:")
	print(upper_letters, "upper letters")
	print(lower_letters, "lower letters")
	print(p_marks, "punctuation marks")
	print(spaces, "spaces")
	print(digits, "digits")


def main():
	argc = len(sys.argv)

	if (argc > 1):
		try:
			assert argc == 2,"AssertionError: more than one argument is provided"
			print_count(sys.argv[1])
		except AssertionError as error:
			print(error)
	else:
		print("What is the text to count?...")
		print_count(input())

		


if __name__ == "__main__":
	main()