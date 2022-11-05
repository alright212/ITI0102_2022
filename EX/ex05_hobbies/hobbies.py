"""EX05 - Hobbies."""


def create_dictionary(data: str) -> dict:
    """
    Create dictionary about people and their hobbies ie. {name1: [hobby1, hobby2, ...], name2: [...]}.

    There should be no duplicate hobbies on 1 person.

    :param data: given string from database
    :return: dictionary where keys are people and values are lists of hobbies
    """
    dictionary = {}
    for i in data.split("\n"):
        name, hobby = i.split(":")
        if name not in dictionary:
            dictionary[name] = [hobby]
        elif hobby not in dictionary[name]:
            dictionary[name].append(hobby)
    return dictionary


def sort_dictionary(dictionary: dict) -> dict:
    """
    Sort dictionary values alphabetically.

    The order of keys is not important.

    sort_dictionary({"b":[], "a":[], "c": []})  => {"b":[], "a":[], "c": []}
    sort_dictionary({"": ["a", "f", "d"]})  => {"": ["a", "d", "f"]}
    sort_dictionary({"b":["d", "a"], "a":["c", "f"]})  => {"b":["a", "d"], "a":["c", "f"]}
    sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]})
        => {"Jack": ["hiking", "swimming"], "Charlie": ["games", "yoga"]}

    :param dictionary: dictionary to sort
    :return: sorted dictionary
    """
    for word in dictionary:
        dictionary[word].sort()
    return dictionary


def create_dictionary_with_hobbies(data: str) -> dict:
    """
    Create dictionary about hobbies and their hobbyists ie. {hobby1: [name1, name2, ...], hobby2: [...]}.

    :param data: given string from database
    :return: dictionary, where keys are hobbies and values are lists of people. Values are sorted alphabetically
    """
    dictionary = create_dictionary(data)
    new_dictionary = {}
    for i in dictionary:
        for j in dictionary[i]:
            if j not in new_dictionary:
                new_dictionary[j] = [i]
            else:
                new_dictionary[j].append(i)
    return sort_dictionary(new_dictionary)


def find_people_with_most_hobbies(data: str) -> list:
    """
    Find the people who have the most hobbies.

    :param data: given string from database
    :return: list of people with most hobbies. Sorted alphabetically.
    """
    dictionary = create_dictionary(data)
    maximum = 0
    for i in dictionary:
        if len(dictionary[i]) > maximum:
            maximum = len(dictionary[i])
    list_of_people = [i for i in dictionary if len(dictionary[i]) == maximum]
    return sorted(list_of_people)


def find_least_popular_hobbies(data: str) -> list:
    """
    Find the least popular hobbies.

    :param data: given string from database
    :return: list of least popular hobbies. Sorted alphabetically.
    """
    dictionary = create_dictionary_with_hobbies(data)
    minimum = 100
    for i in dictionary:
        if len(dictionary[i]) < minimum:
            minimum = len(dictionary[i])
    list_of_hobbies = [i for i in dictionary if len(dictionary[i]) == minimum]
    return sorted(list_of_hobbies)


def sort_names_and_hobbies(data: str) -> tuple:
    """
    Create a tuple of sorted names and their hobbies.

    The structure of the tuple is as follows:
    (
        (name1, (hobby1, hobby2)),
        (name2, (hobby1, hobby2)),
         ...
    )

    For each person, there is a tuple, where the first element is the name (string)
    and the second element is an ordered tuple of hobbies (ordered alphabetically).
    All those person-tuples are ordered by the name of the person and are inside a tuple.
    """
    dictionary = create_dictionary(data)
    list_of_tuples = [(i, tuple(sorted(dictionary[i]))) for i in dictionary]
    return tuple(sorted(list_of_tuples))


def find_people_with_hobbies(data: str, hobbies: list) -> set:
    r"""
    Find all the different people with certain hobbies.

    It is recommended to use set here.

    Example:
        data="John:running\nMary:running\nJohn:dancing\nJack:dancing\nJack:painting\nSmith:painting"
        hobbies=["running", "dancing"]
    Result:
        {"John", "Mary", "Jack"}
    """
    dictionary = create_dictionary(data)
    set_of_people = set()
    for i in dictionary:
        for j in dictionary[i]:
            if j in hobbies:
                set_of_people.add(i)
    return set_of_people


def find_two_people_with_most_common_hobbies(data: str) -> tuple:
    """
    Find a pair of people who have the highest ratio of common to different hobbies.

    Common hobbies are the ones that both people have.
    Different hobbies are the ones that only one person has.

    Example:
    John has:
        running
        walking
    Mary has:
        dancing
        running
    Nora has:
        running
        singing
        dancing

    Pairs and corresponding common and different hobbies; ratio
    John and Mary; common: running; diff: walking, dancing; ratio: 1/2
    John and Nora; common: running; diff: walking, singing, dancing; ratio: 1/3
    Mary and Nora; common: running, dancing; diff: singing; ratio: 2/1

    So the best result is Mary and Nora. It doesn't matter in which order the names are returned.

    If multiple pairs have the same best ratio, it doesn't matter which pair is returned.

    The exception is when multiple pairs share all of their hobbies, in which case the pair with
    the most shared hobbies is returned.

    A pair with only common hobbies is better than any other pair with at least 1 different hobby.

    Example:
    John has:
        running
        walking
    Mary has:
        running
        walking
    Nora has:
        running
    Oprah has:
        running
    Albert has:
        tennis
        basketball
        football
    Xena has:
        tennis
        basketball
        football
        dancing

    John and Mary have 2 common, 0 different. Ratio 2/0
    Nora and Mary (also Nora and John, Oprah and John, Oprah and Mary) have 1 common, 1 different. Ratio 1/1
    Nora and Oprah have 1 common, 0 different. Ratio 1/0
    Albert and Xena have 3 common, 1 different. Ratio 3/1

    In that case the best pair is John and Mary. If the number of different hobbies is 0,
    then this is better than any pair with at least 1 different hobby.
    Out of the pairs with 0 different hobbies, the one with the highest number
    of common hobbies is the best.
    If there are multiple pairs with the highest number of common hobbies,
    any pair (and in any order) is accepted.

    If there are less than 2 people in the input, return None.
    """
    # Create a dictionary with names as keys and hobbies as values
    dictionary = create_dictionary(data)
    best_value = 0
    best_pair = ()
    if len(dictionary) < 2:
        return None
    for name, hobbies_list in dictionary.items():
        for name2, hobbies_list2 in dictionary.items():
            if name != name2:
                common = set()
                different = set()
                for hobby in hobbies_list:
                    for hobby2 in hobbies_list2:
                        if hobby == hobby2:
                            common.add(hobby)
                        else:
                            different.update({hobby}, {hobby2})
                different_hobbies = different.difference(common)
                value = len(different_hobbies) if different_hobbies else 0.1
                if len(common) / value >= best_value:
                    best_value = len(common) / value
                    best_pair = (name, name2)
    return best_pair


if __name__ == "__main__":
    sample_data = """Jack:crafting\nPeter:hiking\nWendy:gaming\nMonica:tennis\nChris:origami\nSophie:sport\nMonica:design\nCarmen:sport\nChris:sport\nMonica:skateboarding\nCarmen:cooking\nWendy:photography\nMonica:tennis\nCooper:yoga\nWendy:sport\nCooper:movies\nMonica:theatre\nCooper:yoga\nChris:gaming\nMolly:fishing\nJack:skateboarding\nWendy:fishing\nJack:drawing\nMonica:baking\nSophie:baking\nAlfred:driving\nAlfred:shopping\nAlfred:crafting\nJack:drawing\nCarmen:shopping\nCarmen:driving\nPeter:drawing\nCarmen:shopping\nWendy:fitness\nAlfred:travel\nJack:origami\nSophie:design\nJack:pets\nCarmen:dance\nAlfred:baking\nSophie:sport\nPeter:gaming\nJack:skateboarding\nCooper:football\nAlfred:sport\nCooper:fitness\nChris:yoga\nWendy:football\nMolly:design\nJack:hiking\nMonica:pets\nCarmen:photography\nJack:baking\nPeter:driving\nChris:driving\nCarmen:driving\nPeter:theatre\nMolly:hiking\nWendy:puzzles\nJack:crafting\nPeter:photography\nCarmen:theatre\nSophie:crafting\nCarmen:cooking\nAlfred:gaming\nPeter:theatre\nCooper:hiking\nChris:football\nChris:pets\nJack:football\nMonica:skateboarding\nChris:driving\nCarmen:pets\nCooper:gaming\nChris:hiking\nJack:cooking\nPeter:fishing\nJack:gaming\nPeter:origami\nCarmen:movies\nSophie:driving\nJack:sport\nCarmen:theatre\nWendy:shopping\nCarmen:pets\nWendy:gaming\nSophie:football\nWendy:theatre\nCarmen:football\nMolly:theatre\nPeter:theatre\nMonica:flowers\nMolly:skateboarding\nPeter:driving\nSophie:travel\nMonica:photography\nCooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""

    sort_result = sort_names_and_hobbies(sample_data)
    # if the condition after assert is False, error will be thrown
    assert isinstance(sort_result, tuple)
    assert len(sort_result) == 10
    assert sort_result[0][0] == "Alfred"
    assert len(sort_result[0][1]) == 7
    assert sort_result[-1] == (
        "Wendy",
        (
            "fishing",
            "fitness",
            "football",
            "gaming",
            "photography",
            "puzzles",
            "shopping",
            "sport",
            "theatre",
        ),
    )
    # if you see this line below, then everything seems to be ok!
    print("sorting works!")

    sample_data = (
        """Jack:painting\nPeter:painting\nJack:running\nMary:running\nSmith:walking"""
    )
    print(find_people_with_hobbies(sample_data, ["running", "painting"]))
    print(
        find_people_with_hobbies(
            "John:running\nMary:running\nJohn:dancing\nJack:dancing\nJack:painting\nSmith:painting",
            ["running", "dancing"],
        )
    )  # {"John", "Mary", "Jack"}

    sample_data = """John:running\nJohn:walking\nMary:dancing\nMary:running\nNora:running\nNora:singing\nNora:dancing"""
    print(find_two_people_with_most_common_hobbies(sample_data))  # ('Mary', 'Nora')
