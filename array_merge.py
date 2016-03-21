
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
        # decide which list should give next item in result:
        for list_i, counter in enumerate(counters):
            # setting counter to None marks list as exhausted
            # skip exhausted lists:
            if counter is None:
                continue
            # mark this list as exhausted if reached its end:
            if counter >= len(lists[list_i]):
                counters[list_i] = None
                continue
            # if we are here, it means that there is at least one
            # non-exhausted list available (we didn't hit a "continue")
            if next_from is None:
                # this is the first non-exhausted list, take the element:
                next_from = list_i
            else:
                # this is second+ non-exhausted list,
                # compare and take if smaller:
                if lists[list_i][counters[list_i]] < lists[next_from][counters[next_from]]:
                    next_from = list_i
        # we have a decision which list will give next item
        # (only last run will have `next_from` set to `None`)
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


def merge_iterables(*iterables):
    """ Merge N sorted lists.
    :return: merged lists, sorted

    Tests:
    >>> l1 = iter(range(8, 12))  # generator: [8, 9, 10, 11]
    >>> l2 = iter(range(0, 21, 10))  # generator: [0, 10, 20]
    >>> merge_iterables(l1, l2)  #doctest:+ELLIPSIS
    <generator ...>
    >>> list(_)
    [0, 8, 9, 10, 10, 11, 20]
    >>> list(merge_iterables(iter([]), iter([1, 2])))
    [1, 2]
    >>> list(merge_iterables())
    []
    """
    EMPTY = object()
    STOPPED = object()
    next_items = [EMPTY] * len(iterables)
    while True:
        for i, iterable in enumerate(iterables):
            if next_items[i] is EMPTY:
                try:
                    next_items[i] = next(iterable)
                except StopIteration:
                   next_items[i] = STOPPED
        try:
            min_item = min(filter(lambda i: i is not STOPPED,
                                  next_items))
        except:
            return  # all next_items are STOPPED, we are done

        min_index = next_items.index(min_item)
        next_items[min_index] = EMPTY
        yield min_item


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests.txt", globs=locals(), verbose=True)