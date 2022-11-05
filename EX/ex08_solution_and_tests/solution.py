"""Solution to functions."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    time = time
    coffee_needed = coffee_needed
    return True if 18 <= time <= 24 else 5 <= time <= 17 and coffee_needed


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    a = a
    b = b
    c = c
    if a == 5 and b == 5 and c == 5:
        return 10
    elif a == b == c:
        return 5
    elif a != b and a != c and b != c:
        return 1
    else:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    if small_baskets + big_baskets * 5 < ordered_amount:
        return -1

    if ordered_amount >= 5 and big_baskets:
        return fruit_order(small_baskets, big_baskets - 1, ordered_amount - 5)

    if small_baskets < ordered_amount:
        return -1

    if ordered_amount > 0:
        return 1 + fruit_order(small_baskets - 1, big_baskets, ordered_amount - 1)

    return 0
