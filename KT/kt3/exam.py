"""KT3."""


def last_to_first(s):
    """
    Move last symbol to the beginning of the string.

    last_to_first("ab") => "ba"
    last_to_first("") => ""
    last_to_first("hello") => "ohell"
    """
    return s[-1] + s[:-1] if s else s


def only_one_pair(numbers: list) -> bool:
    """
    Whether the list only has one pair.

    Function returns True, if the list only has one pair (two elements have the same value).
    In other cases:
     there are no elements with the same value
     there are more than 2 elements with the same value
     there are several pairs
    returns False.

    only_one_pair([1, 2, 3]) => False
    only_one_pair([1]) => False
    only_one_pair([1, 2, 3, 1]) => True
    only_one_pair([1, 2, 1, 3, 1]) => False
    only_one_pair([1, 2, 1, 3, 1, 2]) => False
    """
    count = 0
    if len(numbers) < 2:
        return False
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                count += 1
    return count == 1


def pentabonacci(n: int) -> int:
    """
    Find the total number of odd values in the sequence up to the f(n) [included].

    The sequence is defined like this:
    f(0) = 0
    f(1) = 1
    f(2) = 1
    f(3) = 2
    f(4) = 4
    f(n) = f(n - 1) + f(n - 2) + f(n - 3) + f(n - 4) + f(n - 5)

    Keep in mind that 1 is the only value that is duplicated in the sequence
    and must be counted only once.

    pentabonacci(5) -> 1
    pentabonacci(10) -> 3
    pentabonacci(15) -> 5

    :param n: The last term to take into account.
    :return: Total number of odd values.
    """
    if n == 0:
        return 0
    elif n < 5:
        return 1
    else:
        fib_list = [0, 1, 1, 2, 4]
        counter = 1
        for i in range(5, n + 1):
            sum_of_nazi = sum(fib_list[j] for j in range(i - 5, i))
            fib_list.append(sum_of_nazi)
            if sum_of_nazi % 2 != 0:
                counter += 1
        return counter


def swap_dict_keys_and_value_lists(d: dict) -> dict:
    """
    Swap keys and values in dict.

    Values are lists.
    Every element in this list should be a key,
    and current key will be a value for the new key.
    Values in the result are lists.

    Every list in input dict has at least 1 element.
    The order of the values in the result dict is not important.

    swap_dict_keys_and_value_lists({"a": ["b", "c"]}) => {"b": ["a"], "c": ["a"]}
    swap_dict_keys_and_value_lists({1: [2, 3], 4: [2, 5]}) => {2: [1, 4], 3: [1], 5: [4]}
    swap_dict_keys_and_value_lists({}) => {}
    swap_dict_keys_and_value_lists({1: [2]}) => {2: [1]}
    """
    d_swap = {}
    for key, value in d.items():
        for v in value:
            if v in d_swap:
                d_swap[v].append(key)
            else:
                d_swap[v] = [key]
    return d_swap


if __name__ == "__main__":
    assert last_to_first("ab") == "ba"
    assert last_to_first("") == ""
    assert last_to_first("hello") == "ohell"

    assert only_one_pair([1, 2, 3]) is False
    assert only_one_pair([1]) is False
    assert only_one_pair([1, 2, 3, 1]) is True
    assert only_one_pair([1, 2, 1, 3, 1]) is False
    assert only_one_pair([1, 2, 1, 3, 1, 2]) is False

    assert pentabonacci(5) == 1
    assert pentabonacci(10) == 3
    assert pentabonacci(15) == 5

    assert swap_dict_keys_and_value_lists({"a": ["b", "c"]}) == {"b": ["a"], "c": ["a"]}
    assert swap_dict_keys_and_value_lists({1: [2, 3], 4: [2, 5]}) == {
        2: [1, 4],
        3: [1],
        5: [4],
    }  # or {2: [4, 1], 3: [1], 5: [4]}
    assert swap_dict_keys_and_value_lists({}) == {}
    assert swap_dict_keys_and_value_lists({1: [2]}) == {2: [1]}
