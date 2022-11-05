"""TK1."""


def format_time(minutes: int) -> str:
    """
    Given minutes as an int, return correctly formatted time in hours and minutes.

    Correct format would be '{hours}h {minutes}min'.
    However, if there is not enough minutes to form an hour, show only minutes.
    In that case the format would be '{minutes}min'.
    But when there are no remaining minutes, show only hours.
    In that case the format would be '{hours}h'.
    One hour contains of 60 minutes.

    Examples:
    1) given 112 minutes, return '1h 52min'.
    2) given 23 minutes, return '23min'.
    3) given 180 minutes, return '3h'.

    :param minutes: given minutes
    :return: formatted time in hours and minutes
    """
    hours = minutes // 60
    minutes %= 60
    if hours > 0 and minutes > 0:
        return f"{hours}h {minutes}min"
    elif hours > 0 and minutes == 0:
        return f"{hours}h"
    elif hours == 0 and minutes > 0:
        return f"{minutes}min"
    else:
        return "0min"


# print(format_time(112))
# print(format_time(23))
# print(format_time(180))
# print(format_time(0))


def caught_speeding(speed, is_birthday):
    """
    Return which category speeding ticket you would get.

    You are driving a little too fast, and a police officer stops you.
    Write code to compute the result, encoded as an int value:
    0=no ticket, 1=small ticket, 2=big ticket.
    If speed is 60 or less, the result is 0.
    If speed is between 61 and 80 inclusive, the result is 1.
    If speed is 81 or more, the result is 2.
    Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

    caught_speeding(60, False) => 0
    caught_speeding(65, False) => 1
    caught_speeding(65, True) => 0

    :param speed: Speed value.
    :param is_birthday: Whether it is your birthday (boolean).
    :return: Which category speeding ticket you would get (0, 1, 2).
    """
    if is_birthday:
        if speed <= 65:
            return 0
        elif speed <= 85:
            return 1
        else:
            return 2
    elif speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2


# print(caught_speeding(60, False))
# print(caught_speeding(65, False))
# print(caught_speeding(65, True))
# print(caught_speeding(85, False))


def first_half(text: str) -> str:
    """
    Return the first half of an string.

    The length of the string is even.

    first_half('HaaHoo') => 'Haa'
    first_half('HelloThere') => 'Hello'
    first_half('abcdef') => 'abc'
    """
    return text[: len(text) // 2] if len(text) % 2 == 0 else None


# print(first_half('HaaHoo'))
# print(first_half('HelloThere'))
# print(first_half('abcdef'))


def num_as_index(nums: list) -> int:
    """
    Return element which index is the value of the smaller of the first and the last element.

    If there is no such element (index is too high), return the smaller of the first and the last element.

    num_as_index([1, 2, 3]) => 2 (1 is smaller, use it as index)
    num_as_index([4, 5, 6]) => 4 (4 is smaller, but cannot be used as index)
    num_as_index([0, 1, 0]) => 0
    num_as_index([3, 5, 6, 1, 1]) => 5

    :param nums: list of non-negative integers.
    :return: element value in the specific index.
    """
    if nums[0] < nums[-1]:
        return nums[nums[0]] if nums[0] < len(nums) else nums[0]
    else:
        return nums[nums[-1]] if nums[-1] < len(nums) else nums[-1]


# print(num_as_index([1, 2, 3]))
# print(num_as_index([4, 5, 6]))
# print(num_as_index([0, 1, 0]))
# print(num_as_index([3, 5, 6, 1, 1]))


def remove_in_middle(text, to_remove):
    """
    Remove substring from the text, except for the first and the last occurrence.

    remove_in_middle("abc", "def") => "abc"
    remove_in_middle("abcabcabc", "abc") => "abcabc"
    remove_in_middle("abcdabceabcabc", "abc") => "abcdeabc"
    remove_in_middle("abcd", "abc") => "abcd"
    remove_in_middle("abcdabc", "abc") => "abcdabc"
    remove_in_middle("ABCAaaaAA", "a") => "ABCAaaAA

    :param text: string from where the remove takes place.
    :param to_remove: substring to be removed.
    :return: string with middle substrings removed.
    """
    if text.find(to_remove) in [-1, text.rfind(to_remove)]:
        return text
    if text.find(to_remove) + len(to_remove) > text.rfind(to_remove):
        return text

    begin = text.find(to_remove) + len(to_remove)
    end = text.rfind(to_remove)

    middle = text[begin:end].replace(to_remove, "")
    return text[:begin] + middle + text[end:]


if __name__ == "__main__":
    print("Hello world!")
    print(remove_in_middle("abc", "def"))
    print(remove_in_middle("abcabcabc", "abc"))
    print(remove_in_middle("abcdabceabcabc", "abc"))
    print(remove_in_middle("abcd", "abc"))
    print(remove_in_middle("abcdabc", "abc"))
    print(remove_in_middle("ABCAaaaAA", "a"))
