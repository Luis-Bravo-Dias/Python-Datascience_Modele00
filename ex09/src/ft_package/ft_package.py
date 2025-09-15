def print_count(str):
    """
    Displays the sums of total characters, upper-case characters,
    lower-case characters, punctuation characters,
    digits and spaces of a string that receives as an argument.
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


def ft_filter(function, iterable):
    """
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """

    for item in iterable:
        if function:
            if function(item):
                yield item
        elif item:
            yield item

def decoder(msg: str):
    """
    Takes a string and returns the translation to morse code
    """
    NESTED_MORSE = {" ": "/ ",
                    "A": ".- ",
                    "B": "-... ",
                    "C": "-.-. ",
                    "D": "-.. ",
                    "E": ". ",
                    "F": "..-. ",
                    "G": "--. ",
                    "H": ".... ",
                    "I": ".. ",
                    "J": ".--- ",
                    "K": "-.- ",
                    "L": ".-.. ",
                    "M": "-- ",
                    "N": "-. ",
                    "O": "--- ",
                    "P": ".--. ",
                    "Q": "--.- ",
                    "R": ".-. ",
                    "S": "... ",
                    "T": "- ",
                    "U": "..- ",
                    "V": "...- ",
                    "W": ".-- ",
                    "X": "-..- ",
                    "Y": "-.-- ",
                    "Z": "--.. ",
                    "1": ".---- ",
                    "2": "..--- ",
                    "3": "...-- ",
                    "4": "....- ",
                    "5": "..... ",
                    "6": "-.... ",
                    "7": "--... ",
                    "8": "---.. ",
                    "9": "----. ",
                    "0": "----- "
                    }
    up_msg = msg.upper()
    code = ""

    for char in up_msg:
        code += NESTED_MORSE.get(char, "")
    return code.rstrip()


def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    total = len(lst)
    bar_len = 61
    for i, item in enumerate(lst, 1):
        percent = int(i / total * 100)
        filled = (percent * bar_len) // 100
        bar = "=" * (filled - 1) + ">" + " " * (bar_len - filled)
        print(f"\r{percent}%[{bar}] {i}/{total}", end="", flush=True)
        yield item
    print()


def count_in_list(lst: list, element):
    """
    Return how many times 'element' appears in 'lst'.
    """

    result = 0
    for i in lst:
        if i == element:
            result += 1
    return result
