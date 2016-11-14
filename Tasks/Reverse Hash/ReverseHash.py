import math

#  Reverse hash
#   Reverts your hash back into a string

letters = "acdegilmnoprstuw"


def string_from_hash(hash):
    h = int(hash)
    result = ""
    indices = []
    while h > 7:
        ind = (h % 37)
        indices.append(ind)
        h = int(h / 37)         # int used to convert float values to int
        # python 2.7 converting a / b = int
        # python 3.5 converting a / b = float
        # hence, int to take care of all scenarios

    for ind in indices:
        result = letters[ind] + result

    return result
