# 18th September 2018, Daily Coding Problem #4
#
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

# Helper Function
def low_pos_int(List):
    List.sort()
    for i in List:
        if i > 0:
            return List.index(i)
    return -1

def lowest_integer (List):
    '''Time Complexity  : O(n)
       Space Complexity : O(1)'''
    # Ignoring the O(nlogn) time complexity of timsort

    List.sort()
    i = List[low_pos_int(List)]
    if i > 1 or i <= 0 :
        return 1
    else:
        while True:
            i += 1
            if i not in List:
                return i


def Testf():
    List1 = [3, 4, -1, 1]
    List2 = [1, 1, 0, -1, -2]
    List3 = [2, 3, -7, 6, 8, 1, -10, 15]
    List4 = [2, 3, 7, 6, 8, -1, -10, 15]

    if lowest_integer(List1) == 2:
        print('yay1')
    else:
        print('nay1')

    if lowest_integer(List2) == 2:
        print('yay2')
    else:
        print('nay2')

    if lowest_integer(List3) == 4:
        print('yay3')
    else:
        print('nay3')

    if lowest_integer(List4) == 1:
        print('yay4')
    else:
        print('nay4')

Testf()
