# In a prison cells are stacked in triangular shape, and cells are give ids staring from the corner as follow.
#
# | 7
# | 4 8
# | 2 5 9
# | 1 3 6 10
#
# Each cell can represent as points [x, y], with x being distance from the
# vertical wall, and y being the height from the ground.
#
# For Example the cell at [1, 1] has ID 1, the cell at [3, 2]
# has ID 9, and the cell at [2, 3] has ID 8. This pattern of
# numbering continues indefinitely (as more cells are being added).
#
# Write function solution([x, y]) which returns the cell ID
# at location [x, y]. Each value of x and y will be at least 1 and no greater than 1
# 00,000. As the cell ID may be very large number, return it in form of string.
#
# Example 1
# In: solution([5,10])
# Out: '96'

def solution(x,y):
    id = (x + y - 2) * (x + y - 1) // 2 + x
    return str(id)