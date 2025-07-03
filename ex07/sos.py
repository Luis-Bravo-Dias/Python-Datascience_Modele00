import sys


def main():
    argc = len(sys.argv)
    as_error = "AssertionError: the arguments are bad"
    NESTED_MORSE = { " ": "/ ",
                    "A": ".- ",
                    "B": "-...",
                    "C": "-.-.",
                    "D": "-..",
                    "E": ".",
                    "F": "..-."
                   }

    try:
        assert argc == 2, as_error
    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()