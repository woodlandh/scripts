# The function list_merge(a, b) takes two lists of sorted, non-overlapping numeric ranges and merges them into a single list of sorted, non-overlapping numeric ranges by combining ranges which overlap.
# Ranges are expressed as tuples of the form (start, end) where both start and end are numbers (but not necessarily integers) and start <= end.  
# Range endpoints are both inclusive to the range, which is to say that the range (1, 2) contains the values 1 and 2 and all numbers in between, and therefore the ranges (1, 2) and (2, 5) overlap because they both contain 2.
# 
# Example:
#     a = [(0, 5), (6, 8), (12, 100)]
#     b = [(1, 7), (8, 10), (25, 50), (75, 200)]
#     list_merge(a, b) = [(0, 10), (12, 200)]
# 
# Implement the list_merge() function and any other helpers you need for your implementation.
# 

def list_merge(a, b):
    """
    Takes two lists of sorted, non-overlapping numeric ranges
    and merges them into a single list of sorted,
    non-overlapping numeric ranges by combining overlaps
    Parameters:
      a, b - a list of sorted, non-overlapping numeric ranges 
    """
    ret_l = []
    if not a:
        return b
    elif not b:
        return a
    process_l = order_to_process(a,b)
    print(process_l)
    q = process_l.pop(0)
    while process_l:
        curr = process_l.pop(0)
        if overlaps(q, curr):
            q = merge_tupls(q, curr)
        else:
            ret_l.append(q)
            q = curr
    ret_l.append(q)
    return ret_l


def order_to_process(a, b):
    """
    Takes two sorted lists of tuples and returns a
    combined list sorted by lowest first element
    Paramters:
      a, b - a sorted list of tuples
    """
    ret_l = []
    while a and b:
        ret_l.append(a.pop(0) if a <= b else b.pop(0))
    ret_l.extend(a)
    ret_l.extend(b)
    return ret_l

def merge_tupls(tupl1, tupl2):
    """
    Takes two tuples and returns a new tuple of
    their min and max, assumes range (low,high)
    Parameters:
      tupl1, tupl2 - a tuple range
    """
    return (min(tupl1[0],tupl2[0]),max(tupl1[1],tupl2[1]))

def overlaps(tupl1, tupl2):
    """
    Takes two ranges as tuples and returns a boolean
    determining if they overlap inclusively
    Parameters:
      r1, r2 - a tuple range
    """
    r1 = range(tupl1[0],tupl1[1]+1)
    r2 = range(tupl2[0],tupl2[1]+1)
    return bool(set(r1) & set(r2))

####################
# PYTEST
# http://doc.pytest.org/en/latest/
# py.test list_merge.py -v
####################

def test_overlaps():
    assert overlaps((0,9),(2,3)) == True #inclusive
    assert overlaps((0,1),(1,2)) == True #overlap
    assert overlaps((0,1),(2,3)) == False #exclusive

def test_merge_tupl():
    assert merge_tupls((0,1),(1,2)) == (0,2) #overlap
    assert merge_tupls((0,10),(1,2)) == (0,10) #inclusive

def test_order_to_process():
    a = [(0,1),(4,5),(8,9),(10,11)]
    b = [(1,2),(6,7)]
    assert order_to_process(a,b) == [(0,1),(1,2),(4,5),(6,7),(8,9),(10,11)]
    a = [(0,100)]
    b = [(1,10)]
    assert order_to_process(a,b) == [(0,100),(1,10)]

def test_list_merge():
    a = [(0, 5), (6, 8), (12, 100)]
    b = [(1, 7), (8, 10), (25, 50), (75, 200)]
    assert list_merge(a, b) == [(0, 10), (12, 200)] # example supplied
    a = [(0,1), (2,3), (7,8)]
    b = [(1,2), (5,6), (8,10)]
    assert list_merge(a, b) == [(0,3),(5,6),(7,10)]
    a = [(0,100)]
    b = [(90,100), (95,105)]
    assert list_merge(a, b) == [(0,105)]
    a = []
    b = [(1,5),(6,10)]
    assert list_merge(a, b) == b

