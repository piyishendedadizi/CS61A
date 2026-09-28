SOURCE_FILE = __file__


def num_eights(num: int) -> int:
    """Returns the number of times 8 appears as a digit of num.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if num // 10 == 0:
        if num == 8:
            return 1
        else:
            return 0
    else:
        if num % 10 == 8:
            return 1 + num_eights(num // 10)
        else:
            return num_eights(num // 10)


def digit_distance(num: int) -> int:
    """Determines the digit distance of num.

    >>> digit_distance(3)
    0
    >>> digit_distance(777) # 0 + 0
    0
    >>> digit_distance(314) # 2 + 3
    5
    >>> digit_distance(31415926535) # 2 + 3 + 3 + 4 + ... + 2
    32
    >>> digit_distance(3464660003)  # 1 + 2 + 2 + 2 + ... + 3
    16
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(SOURCE_FILE, 'digit_distance',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if num // 10 == 0:
        return 0
    else:
        n = num // 10
        return abs(n % 10 - num % 10) + digit_distance(num // 10)


def interleaved_sum(num: int, f_odd, f_even) -> int:
    """Compute the sum f_odd(1) + f_even(2) + f_odd(3) + ..., up
    to num.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1   + 2*2 + 3   + 4*4 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1*1 + 2   + 3*3 + 4   + 5*5
    41
    >>> interleaved_sum(4, triple, square)   # 1*3 + 2*2 + 3*3 + 4*4
    32
    >>> interleaved_sum(4, square, triple)   # 1*1 + 2*3 + 3*3 + 4*3
    28
    >>> from construct_check import check
    >>> check(SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
    True
    >>> check(SOURCE_FILE, 'interleaved_sum', ['BitAnd', 'BitOr', 'BitXor']) # ban bitwise operators, don't worry about these if you don't know what they are
    True
    """
    "*** YOUR CODE HERE ***"
    flag = 1
    n = 1
    re = 0
    def ssum(flag, n, re) -> int:
        if flag == 1:
            flag = 0
            re += f_odd(n)
            n += 1
            if n > num:
                return re
            else:
                return ssum(flag, n, re)
        else:
            flag = 1
            re += f_even(n)
            n += 1
            if n > num:
                return re
            else:
                return ssum(flag, n, re)
    return ssum(1, 1, 0)


def next_smaller_dollar(bill: int) -> int:
    """Returns the next smaller bill in order."""
    if bill == 200:
        return 100
    if bill == 100:
        return 50
    if bill == 50:
        return 20
    if bill == 20:
        return 10
    elif bill == 10:
        return 5
    elif bill == 5:
        return 1
    else:
        return 0

def count_dollars(sum_needed: int) -> int:
    """Return the number of ways to make change.

    >>> count_dollars(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills
    6
    >>> count_dollars(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
    4
    >>> count_dollars(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill
    10
    >>> count_dollars(45)  # How many ways to make change for 45 dollars?
    44
    >>> count_dollars(100) # How many ways to make change for 100 dollars?
    344
    >>> count_dollars(200) # How many ways to make change for 200 dollars?
    3274
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(SOURCE_FILE, 'count_dollars', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def count(sum_needed, next):
        if sum_needed < 0:
            return 0
        elif sum_needed == 0:
            return 1
        else:
            use_100, use_50, use_20, use_10, use_5, use_1 = 0, 0, 0, 0, 0, 0
            if next == 200:
                use_100 = count(sum_needed - 100, next_smaller_dollar(200))
                use_50 = count(sum_needed - 50, next_smaller_dollar(100))
                use_20 = count(sum_needed - 20, next_smaller_dollar(50))
                use_10 = count(sum_needed - 10, next_smaller_dollar(20))
                use_5 = count(sum_needed - 5, next_smaller_dollar(10))
                use_1 = count(sum_needed - 1, next_smaller_dollar(5))
            elif next == 100:
                use_100 = count(sum_needed - 100, next_smaller_dollar(200))
                use_50 = count(sum_needed - 50, next_smaller_dollar(100))
                use_20 = count(sum_needed - 20, next_smaller_dollar(50))
                use_10 = count(sum_needed - 10, next_smaller_dollar(20))
                use_5 = count(sum_needed - 5, next_smaller_dollar(10))
                use_1 = count(sum_needed - 1, next_smaller_dollar(5))
            elif next == 50:
                use_50 = count(sum_needed - 50, next_smaller_dollar(100))
                use_20 = count(sum_needed - 20, next_smaller_dollar(50))
                use_10 = count(sum_needed - 10, next_smaller_dollar(20))
                use_5 = count(sum_needed - 5, next_smaller_dollar(10))
                use_1 = count(sum_needed - 1, next_smaller_dollar(5))
            elif next == 20:
                use_20 = count(sum_needed - 20, next_smaller_dollar(50))
                use_10 = count(sum_needed - 10, next_smaller_dollar(20))
                use_5 = count(sum_needed - 5, next_smaller_dollar(10))
                use_1 = count(sum_needed - 1, next_smaller_dollar(5))
            elif next == 10:
                use_10 = count(sum_needed - 10, next_smaller_dollar(20))
                use_5 = count(sum_needed - 5, next_smaller_dollar(10))
                use_1 = count(sum_needed - 1, next_smaller_dollar(5))
            elif next == 5:
                use_5 = count(sum_needed - 5, next_smaller_dollar(10))
                use_1 = count(sum_needed - 1, next_smaller_dollar(5))
            elif next == 1:
                use_1 = count(sum_needed - 1, next_smaller_dollar(5))
            return use_100 + use_50 + use_20 + use_10 + use_5 + use_1
    return count(sum_needed, 200)
    



def shuffle(s: list) -> list:
    """Return a shuffled list that interleaves the two halves of s.

    >>> shuffle(range(6))
    [0, 3, 1, 4, 2, 5]
    >>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    >>> shuffle(letters)
    ['a', 'e', 'b', 'f', 'c', 'g', 'd', 'h']
    >>> shuffle(shuffle(letters))
    ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']
    >>> letters  # Original list should not be modified
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    """
    assert len(s) % 2 == 0, 'len(seq) must be even'
    "*** YOUR CODE HERE ***"
    num = len(s)
    arr1 = []
    arr2 = []
    arr = []
    for i in range(num // 2):
        arr1 += [s[i]]
    for i in range((num // 2), num):
        arr2 += [s[i]]
    for i in range(num // 2):
        arr += [arr1[i]] + [arr2[i]]
    return arr


def deep_map(f, s: list) :
    """Replace all non-list elements x with f(x) in the nested list s.

    >>> six = [1, 2, [3, [4], 5], 6]
    >>> deep_map(lambda x: x * x, six)
    >>> six
    [1, 4, [9, [16], 25], 36]
    >>> # Check that you're not making new lists
    >>> s = [3, [1, [4, [1]]]]
    >>> s1 = s[1]
    >>> s2 = s1[1]
    >>> s3 = s2[1]
    >>> deep_map(lambda x: x + 1, s)
    >>> s
    [4, [2, [5, [2]]]]
    >>> s1 is s[1]
    True
    >>> s2 is s1[1]
    True
    >>> s3 is s2[1]
    True
    """
    "*** YOUR CODE HERE ***"
    for i in range(len(s)):
        if type(s[i]) != list:
            s[i] = f(s[i])
        else:
            deep_map(f, s[i])


def next_larger_dollar(bill: int) -> int:
    """Returns the next larger bill in order."""
    if bill == 1:
        return 5
    elif bill == 5:
        return 10
    elif bill == 10:
        return 20
    elif bill == 20:
        return 50
    elif bill == 50:
        return 100
    else:
        return 0

def count_dollars_upward(sum_needed: int) -> int:
    """Return the number of ways to make change using bills.

    >>> count_dollars_upward(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills
    6
    >>> count_dollars_upward(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
    4
    >>> count_dollars_upward(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill
    10
    >>> count_dollars_upward(45)  # How many ways to make change for 45 dollars?
    44
    >>> count_dollars_upward(100) # How many ways to make change for 100 dollars?
    344
    >>> count_dollars_upward(200) # How many ways to make change for 200 dollars?
    3274
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(SOURCE_FILE, 'count_dollars_upward', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def count(sum_needed, num):
        if sum_needed < 0:
            return 0
        elif sum_needed == 0:
            return 1
        elif num == 0:
            return 0
        else:
            sum_use = count(sum_needed, next_larger_dollar(num))
            sum_notuse = count(sum_needed - num, num)
            return sum_use + sum_notuse
    return count(sum_needed, 1)
