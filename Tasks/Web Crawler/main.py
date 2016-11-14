import sys
from Crawler import result_count, find_results


# args= arguments passed from terminal
#       0: appname
#       1: first arg
#       2: second arg
#       n: nth arg
def main(args):
    # process arguments
    if len(args) is 2:
        count = result_count(args[1])
        print('Total {0} results found for {1}'.format(count, args[1]))
    elif len(args) is 3:
        ind = 1
        result = find_results(args[1], args[2])
        for name in result:
            print('{0}: {1}'.format(ind, name))
            ind += 1
    else:
        # if sufficient/wrong number of arguments are passed, then print the
        # usage of command
        print('usage:')
        print('{0} {1} [{2}]'.format(args[0], 'keyword', 'page_number'))


if __name__ == "__main__":
    main(sys.argv)
