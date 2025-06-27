from ft_filter import ft_filter
import sys


def main():
    argc = len(sys.argv)
    as_error = "AssertionError: the arguments are bad"

    try:
        assert argc == 3, as_error
        S = sys.argv[1]
        N = int(sys.argv[2])
        assert all(word.isalnum() for word in S.split()), as_error

        first_list = [word for word in S.split()]
        new_list = list(ft_filter(lambda x: len(x) > N, first_list))
        #print(first_list)
        print(new_list)
        #print(filter.__doc__)
        #print(ft_filter.__doc__)
    except ValueError:
        print(as_error)
    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
