
def list_merge(*lists):
    """ Merge N sorted lists.
    :return: merged lists, sorted

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
    >>> list_merge([], [], [], [])
    []
    >>> list_merge([], [2], [4], [])
    [2, 4]
    >>> list_merge([], [], [], [0])
    [0]
    >>> list_merge([4, 5])
    [4, 5]
    >>> list_merge([])
    []
    >>> list_merge()
    []
    >>> import random, time
    >>> huge1 = sorted([random.randrange(100000000) for _ in range(1000000)])
    >>> huge2 = sorted([random.randrange(100000000) for _ in range(1000000)])
    >>> huge3 = sorted([random.randrange(100000000) for _ in range(1000000)])
    >>> t0 = time.time()
    >>> result = list_merge(huge1, huge2, huge3)
    >>> t1 = time.time()
    >>> print("Run time for list_merge: {}".format(t1 - t0))  #doctest:+ELLIPSIS
    Run time for list_merge: ...
    >>> for i in range(len(result) - 1):
    ...     assert result[i] <= result[i + 1], "Items: {}, {}".format(result[i], result[i+1])
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
    >>> list_merge(l1, l2)
    [1, 2, 2, 3, 3, 5, 6, 8, 9, 9, 9, 10, 10, 11, 13, 15, 100]
    >>> list_merge([], [1, 2])
    [1, 2]
    >>> list_merge([1], [])
    [1]
    >>> list_merge([1], [1])
    [1, 1]
    >>> list_merge([], [], [], [])
    []
    >>> list_merge([], [2], [4], [])
    [2, 4]
    >>> list_merge([], [], [], [0])
    [0]
    >>> list_merge([4, 5])
    [4, 5]
    >>> list_merge([])
    []
    >>> list_merge()
    []
    >>> import random, time
    >>> huge1 = sorted([random.randrange(100000000) for _ in range(1000000)])
    >>> huge2 = sorted([random.randrange(100000000) for _ in range(1000000)])
    >>> huge3 = sorted([random.randrange(100000000) for _ in range(1000000)])
    >>> t0 = time.time()
    >>> result = list_merge(huge1, huge2, huge3)
    >>> t1 = time.time()
    >>> assert t1 - t0 < 1, "Too slow"
    >>> print("Run time for list_merge: {}".format(t1 - t0))  #doctest:+ELLIPSIS
    Run time for list_merge: ...
    >>> for i in range(len(result) - 1):
    ...     assert result[i] <= result[i + 1], "Items: {}, {}".format(result[i], result[i+1])
    """
    from itertools import chain
    return sorted(chain(*lists))
