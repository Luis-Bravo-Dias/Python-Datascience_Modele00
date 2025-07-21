import sys


def decoder(msg: str):
    """
    Takes a string and returns the translation to morse code
    """
    NESTED_MORSE = {" ": "/ ",
                    "A": ".- ",
                    "B": "-...",
                    "C": "-.-.",
                    "D": "-..",
                    "E": ".",
                    "F": "..-.",
                    "G": "--.",
                    "H": "....",
                    "I": "..",
                    "J": ".---",
                    "K": "-.-",
                    "L": ".-..",
                    "M": "--",
                    "N": "-.",
                    "O": "---",
                    "P": ".--.",
                    "Q": "--.-",
                    "R": ".-.",
                    "S": "...",
                    "T": "-",
                    "U": "..-",
                    "V": "...-",
                    "W": ".--",
                    "X": "-..-",
                    "Y": "-.--",
                    "Z": "--..",
                    "1": ".----",
                    "2": "..---",
                    "3": "...--",
                    "4": "....-",
                    "5": ".....",
                    "6": "-....",
                    "7": "--...",
                    "8": "---..",
                    "9": "----.",
                    "0": "-----"
                    }
    up_msg = msg.upper()
    code = ""

    for char in up_msg:
        code += NESTED_MORSE.get(char, "")
    return (code)


def main():
    argc = len(sys.argv)
    as_error = "AssertionError: the arguments are bad"
    try:
        assert argc == 2, as_error
        print(decoder(sys.argv[1]))
    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
