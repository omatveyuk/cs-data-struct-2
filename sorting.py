#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    swap = False

    for i in xrange(len(lst) - 1):
        for j in xrange(len(lst) - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swap = True

        if not swap:
            # list is already sorted
            break

    return lst     


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """
    result = []

    #reverse lists
    # reverse_list1 = []
    # reverse_list2 = []
    # for i in xrange(len(list1)):
    #     reverse_list1.append(list1.pop())
    # for i in xrange(len(list2)):
    #     reverse_list2.append(list2.pop())

    # #merge lists
    # while len(reverse_list1) > 0 or len(reverse_list2) > 0:
    #     if reverse_list1 == []:
    #         result.extend(reverse_list2.pop())
    #     elif reverse_list2 == []:
    #         result.append(reverse_list1.pop())
    #     elif reverse_list1[len(list1)-1] > reverse_list2[len(list2)-1]:
    #         result.append(reverse_list2.pop())
    #     else:
    #         result.append(reverse_list1.pop())

    # return result

    index_list1 = 0
    index_list2 = 0
    result = []

    while index_list1 < len(list1) and index_list2 < len(list2):
        if list1[index_list1] < list2[index_list2]:
            result.append(list1[index_list1])
            index_list1 += 1
        else:
            result.append(list2[index_list2])
            index_list2 += 1    

    while index_list1 < len(list1):
        result.append(list1[index_list1])
        index_list1 += 1

    while index_list2 < len(list2):
        result.append(list2[index_list2])
        index_list2 += 1

    return result

##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    >>> merge_sort([9, 6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9, 9]
    >>> merge_sort([])
    []
    """
    index = len(lst)/2
    #base case:
    if len(lst) < 2:
        return lst

    lst1 = merge_sort(lst[:index])
    lst2 = merge_sort(lst[index:])
    return merge_lists(lst1, lst2)




#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
