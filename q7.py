# Write a function named as solution which takes a list containing strings with
# versions numbers separated by two dots as argument. This function should return the versions after sorting.
#
# Example 1
# In: solution([‘1.2.1’,‘1.0.9’,‘0.7.6’,‘7.4.0’,‘2.1.3’])
# Out: [‘0.7.6‘,‘1.0.9’,‘1.2.1’,‘2.1.3’,’7.4.0’]

def key(version):
    return list(map(int, version.split('.')))


def solution(lst):
    return sorted(lst, key=key)


x = ["1.2.1", "1.0.9", "0.7.6", "7.4.0", "2.1.3"]

solution(x)

