"""KT1."""


def capitalize_string(s: str) -> str:
    """
    Return capitalized string.

    The first char is capitalized, the rest remain as they are.

    capitalize_string("abc") => "Abc"
    capitalize_string("ABc") => "ABc"
    capitalize_string("") => ""
    """
    string = ""
    if len(s) == 0:
        return string
    else:
        string = s[0].upper() + s[1:]
        return string


def has_seven(nums):
    """
    Whether the list has three 7s and no repeated consecutive elements.

    Given a list if ints, return True if the value 7 appears in the list exactly 3 times
    and no consecutive elements have the same value.

    has_seven([1, 2, 3]) => False
    has_seven([7, 1, 7, 7]) => False
    has_seven([7, 1, 7, 1, 7]) => True
    has_seven([7, 1, 7, 1, 1, 7]) => False
    """
    consecutive_elements = False
    count = 0
    for i in range(len(nums)):
        if nums[i] == 7:
            count += 1
        if i != 0 and nums[i] == nums[i - 1]:
            consecutive_elements = True
    if count == 3 and consecutive_elements is False:
        return True
    else:
        return False


def list_move(initial_list: list, amount: int, factor: int) -> list:
    """
    Create amount lists where elements are shifted right by factor.

    This function creates a list with amount of lists inside it.
    In each sublist, elements are shifted right by factor elements.
    factor >= 0

    list_move(["a", "b", "c"], 3, 0) => [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
    list_move(["a", "b", "c"], 3, 1) => [['a', 'b', 'c'], ['c', 'a', 'b'], ['b', 'c', 'a']]
    list_move([1, 2, 3], 3, 2) => [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    list_move([1, 2, 3], 4, 1) => [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 2, 3]]
    list_move([], 3, 4) => [[], [], []]
    """
    result = []
    if factor > len(initial_list) and initial_list:
        factor %= len(initial_list)
    for _ in range(amount):
        result.append(initial_list)
        initial_list = initial_list[-factor:] + initial_list[:-factor]
    return result


def parse_call_log(call_log: str) -> dict:
    """
    Parse calling logs to find out who has been calling to whom.

    There is a process, where one person calls to another,
    then this another person call yet to another person etc.
    The log consists of several those call-chains, separated by comma (,).
    One call-chain consists of 2 or more names, separated by colon (:).

    The function should return a dict where the key is a name
    and the value is all the names the key has called to.

    Each name has to be in the list only once.
    The order of the list or the keys in the dictionary are not important.

    Input:
    - consists of 0 or more "chains"
    - chains are separated by comma (,)
    - one chain consists of 2 or more names
    - name is 1 or more symbols long
    - there are no commas nor colons in the name
    - names are separated by colon (:)

    parse_call_log("") => {}
    parse_call_log("ago:kati,mati:malle") => {"ago": ["kati"], "mati": ["malle"]}
    parse_call_log("ago:kati,ago:mati,ago:kati") => {"ago": ["kati", "mati"]}
    parse_call_log("ago:kati:mati") => {"ago": ["kati"], "kati": ["mati"]}
    parse_call_log("mati:kalle,kalle:malle:mari:juri,mari:mati") =>
    {'mati': ['kalle'], 'kalle': ['malle'], 'malle': ['mari'], 'mari': ['juri', 'mati']}

    :param call_log: the whole log as string
    :return: dictionary with call information
    """
    call_log_dict = {}
    call_log_list = call_log.split(",")
    for call_log_item in call_log_list:
        call_log_item_list = call_log_item.split(":")
        for i in range(len(call_log_item_list) - 1):
            if call_log_item_list[i] not in call_log_dict:
                call_log_dict[call_log_item_list[i]] = [call_log_item_list[i + 1]]
            elif call_log_item_list[i + 1] not in call_log_dict[call_log_item_list[i]]:
                call_log_dict[call_log_item_list[i]].append(call_log_item_list[i + 1])
    return call_log_dict


if __name__ == "__main__":
    print(capitalize_string("abc"))  # => "Abc"
    print(capitalize_string("ABc"))  # => "ABc"
    print(capitalize_string(""))  # => ""
    print()
    print(has_seven([1, 2, 3]))  # => False
    print(has_seven([7, 1, 7, 7]))  # => False
    print(has_seven([7, 1, 7, 1, 7]))  # => True
    print(has_seven([7, 1, 7, 1, 1, 7]))  # => False
    print()
    print(
        list_move(["a", "b", "c"], 3, 0)
    )  # => [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
    print(
        list_move(["a", "b", "c"], 3, 1)
    )  # => [['a', 'b', 'c'], ['c', 'a', 'b'], ['b', 'c', 'a']]
    print(list_move([1, 2, 3], 3, 2))  # => [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    print(list_move([1, 2, 3], 4, 1))  # => [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 2, 3]]
    print(list_move([], 3, 4))  # => [[], [], []]
    print()
    print(parse_call_log(""))  # => {}
    print(
        parse_call_log("ago:kati,mati:malle")
    )  # => {"ago": ["kati"], "mati": ["malle"]}
    print(parse_call_log("ago:kati,ago:mati,ago:kati"))  # => {"ago": ["kati", "mati"]}
    print(parse_call_log("ago:kati:mati"))  # => {"ago": ["kati"], "kati": ["mati"]}
    print(parse_call_log("mati:kalle,kalle:malle:mari:juri,mari:mati"))  # =>
    # {'mati': ['kalle'], 'kalle': ['malle'], 'malle': ['mari'], 'mari': ['juri', 'mati']}
