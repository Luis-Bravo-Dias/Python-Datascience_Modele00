import sys

def main():
	argc = len(sys.argv)
	string = ""
	upper_letters = 0
	lower_letters = 0
	p_marks = 0
	spaces = 0
	digits = 0

	punctuation = ".,;:!?\"'()]{[}-"

	if (argc > 1):
		try:
			assert argc == 2,"AssertionError: more than one argument is provided"
			string = sys.argv[1]
		except AssertionError as error:
			print(error)
	else:
		print("What is the text to count?...")
		string = input()
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

		


if __name__ == "__main__":
	main()