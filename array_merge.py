
def list_merge(list1, list2):
    """ Merge two sorted lists.
    :param list1: list, sorted
    :param list2: list, sorted
    :return: merged list, sorted

    Tests:
    >>> l1 = [2, 3, 5, 6, 8, 9, 9, 9, 10, 11, 13, 15, ]
    >>> l2 = [1, 2, 3, 10, 100]
    >>> list_merge(l1, l2)
    [1, 2, 2, 3, 3, 5, 6, 8, 9, 9, 9, 10, 10, 11, 13, 15, 100]
    >>> list_merge([], [1, 2])
    [1, 2]
    >>> list_merge([1], [])
    [1]
    >>> list_merge([1], [1])
    [1, 1]
    """
    counters = [0, 0]
    lists = (list1, list2)
    result = []
    total = len(list1) + len(list2)
    while sum(counters) < total:
        if counters[0] >= len(lists[0]):
            # nothing left in list 0, use 1:
            next_from = 1
        elif counters[1] >= len(lists[1]):
            # nothing left in list 1, use 0:
            next_from = 0
        else:
            # both lists have more elements, pick minimum:
            if lists[0][counters[0]] <= lists[1][counters[1]]:
                next_from = 0
            else:
                next_from = 1
        # append minimum to result:
        result.append(lists[next_from][counters[next_from]])
        # increase counter:
        counters[next_from] += 1
        # all done:
    return result
