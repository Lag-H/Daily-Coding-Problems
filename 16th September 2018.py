# 16th september 2018 Daily Coding Problem #2
#
# Given an array of integers, return a new array such that each element at index
# i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

########################################################

def Product_Array (Sequence):
    '''Time Complexity  : O(n**2)
       Space Complexity : O(1)'''

    Resultant_List = []
    for i in range(len(Sequence)):
        temp_num = 1
        for j in range(len(Sequence)):
            if j != i:
                temp_num = temp_num * Sequence[j]
        Resultant_List.append(temp_num)
    return Resultant_List

def Product_Array_with_division (Sequence):
    '''Time Complexity  : O(n)
       Space Complexity : O(1)'''

    Resultant_List = []
    product = 1
    for i in Sequence:
        product = product * i
    for i in Sequence:
        Resultant_List.append((product/i))
    return Resultant_List

#######################################################

def testf():
    if Product_Array([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]:
        print('Yay')
    else:
        print('nay')

    if Product_Array_with_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]:
        print('Yay')
    else:
        print('nay')

    if Product_Array([3,2,1]) == [2,3,6]:
        print('Yay')
    else:
        print('nay')

    if Product_Array_with_division([3,2,1]) == [2,3,6]:
        print('Yay')
    else:
        print('nay')


testf()