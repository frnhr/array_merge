
def list_merge(list1, list2):
    """ Merge two sorted lists.
    :param list1: list, sorted
    :param list2: list, sorted
    :return: merged list, sorted

    Tests:
    >>> l1 = [2, 3, 5, 6, 8, 9, 9, 9, 10, 11, 13, 15, ]
    >>> l2 = [1, 2, 3, 10, 100]
    >>> list_merge(l1, l2)
    [1, 2, 2, 3, 3, 5, 6, 7, 8, 8, 8, 10, 10, 11, 13, 15, 100]
    >>> list_merge([], [1, 2])
    [1, 2]
    >>> list_merge([1], [])
    [1]
    >>> list_merge([1], [1])
    [1, 1]
    """
    i, j = 0, 0
    result = []
    total = len(list1) + len(list2)
    while i + j < total:
        if i < len(list1) and list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    return result
