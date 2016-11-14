from Hash import hash
from ReverseHash import string_from_hash


def test():
	# valid strings
    valid_strs = ["guard", "scooter", "leepadg"]
    for str in valid_strs:
        hash_val = hash(str)
        non_hash_val = string_from_hash(hash_val)
        if non_hash_val == str:
            print(("{0}: success").format(str))
        else:
            print(("{0}: failed").format(str))

    # invalid strings
    invalid_strs = ["clarke", "bruce"]
    for str in invalid_strs:
        hash_val = hash(str)
        if hash_val is not None:
            print('Hashed value:', hash_val)


if __name__ == "__main__":
    test()
