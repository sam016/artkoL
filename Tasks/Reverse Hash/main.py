import sys
from ReverseHash import string_from_hash


def main(args):
    hash = 930846109532517  # default hash, asked in assignment
    if len(args) is 2:
        # if user has passed a hash as an argument while executing a program
        hash = args[1]

    print(string_from_hash(hash))


if __name__ == "__main__":
    main(sys.argv)
