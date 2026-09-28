from __future__ import annotations


def without(s: Link, i: int) -> Link:
    """Return a new linked list like s but without the element at index i.

    >>> s = Link(3, Link(5, Link(7, Link(9))))
    >>> without(s, 0)
    Link(5, Link(7, Link(9)))
    >>> without(s, 2)
    Link(3, Link(5, Link(9)))
    >>> without(s, 4)  # There is no index 4, so all of s is retained.
    Link(3, Link(5, Link(7, Link(9))))
    """
    "*** YOUR CODE HERE ***"
    p = Link.empty
    q = p
    for j in range(i):
        if s != Link.empty:
            if q == Link.empty:
                q = Link(s.first)
                p = q
                s = s.rest
            else:
                q.rest = Link(s.first)
                s = s.rest
                q = q.rest
    if s != Link.empty:
        s = s.rest
    while s != Link.empty:
        if q != Link.empty:
            q.rest = Link(s.first)
            s = s.rest
            q = q.rest
        else:
            q = Link(s.first)
            p = q
            s = s.rest
    return p


def duplicate_link(s: Link, val: int) -> None:
    """Mutates s so that each element equal to val is followed by another val.

    >>> x = Link(5, Link(4, Link(5)))
    >>> duplicate_link(x, 5)
    >>> x
    Link(5, Link(5, Link(4, Link(5, Link(5)))))
    >>> y = Link(2, Link(4, Link(6, Link(8))))
    >>> duplicate_link(y, 10)
    >>> y
    Link(2, Link(4, Link(6, Link(8))))
    >>> z = Link(1, Link(2, Link(2, Link(3))))
    >>> duplicate_link(z, 2) # ensures that back to back links with val are both duplicated
    >>> z
    Link(1, Link(2, Link(2, Link(2, Link(2, Link(3))))))
    """
    "*** YOUR CODE HERE ***"
    while s != Link.empty:
        if s.first == val:
            p = s
            s = s.rest
            p.rest = Link(val)
            p.rest.rest = s
        else:
            s = s.rest



def slice_link(link: Link, start: int, end: int) -> Link:
    """Slices a linked list from start to end (as with a normal Python list) and returns
    a linked list. You do NOT have to support negative indices.

    >>> link = Link(3, Link(1, Link(4, Link(1, Link(5, Link(9))))))
    >>> new = slice_link(link, 1, 4)
    >>> print(new)
    (1 4 1)
    >>> print(slice_link(link, 0, 2))
    (3 1)
    >>> print(slice_link(link, 0, 6))
    (3 1 4 1 5 9)
    >>> print(slice_link(link, 2, 2))
    ()
    >>> print(slice_link(link, 2, 3))
    (4)
    >>> print(slice_link(link, 3, 100))
    (1 5 9)
    >>> print(slice_link(link, 10, 12))
    ()
    """
    "*** YOUR CODE HERE ***"
    s = link
    for _ in range(start):
        if s != Link.empty:
            s = s.rest
        else:
            return ()
    p = Link(0)
    q = p
    for _ in range(end - start):
        if s != Link.empty:
            q.rest = Link(s.first)
            q = q.rest
            s = s.rest
        else:
            break
    return p.rest



def has_cycle(link: Link) -> bool:
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    p = q = link
    while q != Link.empty:
        q = q.rest
        if q == Link.empty:
            return False
        q = q.rest
        if q == Link.empty:
            return False
        p = p.rest
        if p == q:
            return True

def has_cycle_constant(link: Link) -> bool:
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    p = q = link
    while q != Link.empty:
        q = q.rest
        if q == Link.empty:
            return False
        q = q.rest
        if q == Link.empty:
            return False
        p = p.rest
        if p == q:
            return True


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    (5 7 (8 9))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '('
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + ')'

