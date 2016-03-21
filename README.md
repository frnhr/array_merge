# Array merge

A test task for a project, nothing interesting here...

## What is "array"?

Word "array" doesn't mean much in Python. Closest to arrays in C are 
lists in Python.

But there are other iterable things in Python that are not list 
(because if it quacks like a duck...) so another way to translate "array" to 
Python is to say "iterable".

## Merge arrays

Task: make a function that accepts N sorted arrays returns a new sorted array 
that contains all items from the input arrays.

## Implementation 1 - using builtins

Simplest and almost always sufficient:

    def list_chain_and_sort(*lists):
        from itertools import chain
        return sorted(chain(*lists))
        
I suspect this runs in `O(n log(n))` and this is quite adequate.

If, however, `O(n)` is required...


## Implementation 2 - pick and choose
 
    def list_merge(*lists):
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

     Basically, built up the array by iterating over input arrays and choosing
     next element to be smallest.

Possible improvements:

 - pre-allocating `results` list *might* yield better results (something
   like `results = [None] * total_items`
   

## Implementation 3 - generators

But realistically, when dealing with 100s of millions of items in lists, we
are probably dealing with generators (or we should, anyway).

To that end, this implementation receives and returns a generator.


    def merge_iterables(*iterables):
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
                min_item = min(filter(lambda i: i not in {EMPTY, STOPPED},
                                      next_items))
            except:
                return  # all next_items are STOPPED, we are done
    
            min_index = next_items.index(min_item)
            next_items[min_index] = EMPTY
            yield min_item


This implementation holds only one item in memory for every iterable provided 
to the function. It is most efficient in terms of both memory and cpu. 
But of course, it requires generators at input. 

Generators can be made from lists using `iter(a_list)`, though that negates 
the benefits of generators since the entire list is already in memory. 
The result will still be a generator, of course, and if used correctly,
can be memory-efficient (e.g. if not cast to list with 
`list(resulting_generator)`).
