from Crawler import result_count, find_results


# Case #1:
#   > Open the URL
#   > Search shoes
#   > Check the count on report
#   > Verify the count got from the program
print('\r\nVerification #1')
count = result_count('shoes')
print('Shoes count:', count)


# Case #2:
#   > Open the URL
#   > Search shoes
#   > Go to 10th page
#   > Verify that products name is same as returned by the program
print('\r\nVerification #2')
ind = 1
result = find_results('shoes', 10)
for name in result:
    print('{0}: {1}'.format(ind, name))
    ind += 1
