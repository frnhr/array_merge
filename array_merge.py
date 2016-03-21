
def list_merge(*lists):
    """ Merge N sorted lists.
    :return: merged lists, sorted

    Tests:
    >>> l1 = [2, 3, 5, 6, 8, 9, 9, 9, 10, 11, 13, 15, ]
    >>> l2 = [1, 2, 3, 10, 100]
    >>> list_merge(l1, l2)
    [1, 2, 2, 3, 3, 5, 6, 8, 9, 9, 9, 10, 10, 11, 13, 15, 100]
    >>> list_merge([], [1, 2], [], [-1])
    [-1, 1, 2]
    >>> list_merge()
    []
    """
    counters = [0] * len(lists)
    result = []
    next_from = True
    while next_from is not None:
        next_from = None
        for list_i, counter in enumerate(counters):
            if counter is None:
                continue
            if counter >= len(lists[list_i]):
                counters[list_i] = None
                continue
            if next_from is None:
                # first non-eshausted list, take the element:
                next_from = list_i
            else:
                # compare and take if smaller:
                if lists[list_i][counters[list_i]] < lists[next_from][counters[next_from]]:
                    next_from = list_i
        if next_from is not None:
            # append minimum to result:
            result.append(lists[next_from][counters[next_from]])
            # increase counter:
            counters[next_from] += 1
            # all done:
    return result


def list_chain_and_sort(*lists):
    """ Merge N sorted lists.
    :return: merged lists, sorted

    Tests:
    >>> l1 = [2, 3, 5, 6, 8, 9, 9, 9, 10, 11, 13, 15, ]
    >>> l2 = [1, 2, 3, 10, 100]
    >>> list_chain_and_sort(l1, l2)
    [1, 2, 2, 3, 3, 5, 6, 8, 9, 9, 9, 10, 10, 11, 13, 15, 100]
    >>> list_chain_and_sort([], [1, 2])
    [1, 2]
    >>> list_chain_and_sort()
    []
    """
    from itertools import chain
    return sorted(chain(*lists))


def merge_iterables(*lists):
    """ Merge N sorted lists.
    :return: merged lists, sorted

    Tests:
    >>> l1 = [2, 3, 5, 6, 8, 9, 9, 9, 10, 11, 13, 15, ]
    >>> l2 = [1, 2, 3, 10, 100]
    >>> merge_iterables(l1, l2)  #doctest:+ELLIPSIS
    <generator ...>
    >>> list(merge_iterables(l1, l2))
    [1, 2, 2, 3, 3, 5, 6, 8, 9, 9, 9, 10, 10, 11, 13, 15, 100]
    >>> list(merge_iterables([], [1, 2]))
    [1, 2]
    >>> list(merge_iterables())
    []
    """
    counters = [0] * len(lists)
    next_from = True
    while next_from is not None:
        next_from = None
        for list_i, counter in enumerate(counters):
            if counter is None:
                continue
            if counter >= len(lists[list_i]):
                counters[list_i] = None
                continue
            if next_from is None:
                # first non-eshausted list, take the element:
                next_from = list_i
            else:
                # compare and take if smaller:
                if lists[list_i][counters[list_i]] < lists[next_from][counters[next_from]]:
                    next_from = list_i
        if next_from is not None:
            # yield the selected item:
            yield lists[next_from][counters[next_from]]
            # increase counter:
            counters[next_from] += 1


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests.txt", globs=locals(), verbose=True)