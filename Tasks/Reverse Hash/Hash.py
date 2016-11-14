import re

#
# hash() pseudocode
#
# Int64 hash(String s) {
#     Int64 h = 7
#     String letters = "acdegilmnoprstuw"
#     for(Int32 i=0; i < s.length; i + +) {
#         h = (h * 37 + letters.indexOf(s[i]))
#     }
#     return h
# }

letters = "acdegilmnoprstuw"

# converts a string into a hash
def hash(str):
    if validate(str) is not True:
        print('Invalid input:', str)
        return None

    h = 7
    for ch in str:
        h = h * 37 + letters.index(ch)
    return h


# validates the string passsed
def validate(str):
    regex = re.compile('[' + letters + ']')
    result = regex.sub('', str)
    return result == ''
