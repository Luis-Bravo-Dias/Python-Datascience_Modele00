from ft_filter import ft_filter
import sys

print(filter.__doc__)

def main():
    argc = len(sys.argv)
    as_error = "AssertionError: more than one argument is provided"

    if (argc > 1):
        try:
            assert argc == 2, as_error
           
        except AssertionError as error:
            print(error)


if __name__ == "__main__":
    main()