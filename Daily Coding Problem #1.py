# Daily Coding Problem #1
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?


def SumInList (Lst, k):
    '''Time complexity  : O(n**2)
       Space complexity : O(1)   '''

    for i in range(len(Lst)):
        for j in range(i+1, len(Lst)):
            if Lst[i] + Lst[j] == k:
                return True
    return False


def Testf ():
    L1 = [1,3,4,6,7,0]
    L2 = [3,85,34,23,44]
    L3 = [10, 15, 3, 7]

    if SumInList(L1, 1):
        print('Test 1 complete')
    else:
        print('Test 1 wrong')

    if not SumInList(L1, 100):
        print('Test 2 complete')
    else:
        print('Test 2 wrong')

    if SumInList(L2, 47):
        print('Test 3 complete')
    else:
        print('Test 3 wrong')

    if not SumInList(L2, 40):
        print('Test 4 complete')
    else:
        print('Test 4 wrong')

    if SumInList(L3, 17):
        print('Test 5 complete')
    else:
        print('Test 5 wrong')

Testf()

