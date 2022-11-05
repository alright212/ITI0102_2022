"""EX03 ID code."""


def find_id_code(text: str) -> str:
    """
    Find ID-code from given text.

    Given string may include any number of numbers, characters and other symbols mixed together.
    The numbers of ID-code may be between other symbols - they must be found and concatenated.
    ID-code contains of exactly 11 numbers. If there are not enough numbers, return 'Not enough numbers!',
    if there are too many numbers, return 'Too many numbers!' If ID-code can be found, return that code.
    You don't have to validate the ID-code here. If it has 11 numbers, then it is enough for now.

    :param text: string
    :return: string
    """
    numbers = "".join(char for char in text if char.isdigit())
    if len(numbers) == 11:
        return numbers
    elif len(numbers) < 11:
        return "Not enough numbers!"
    else:
        return "Too many numbers!"


def the_first_control_number_algorithm(text: str) -> str:
    """
    Check if given value is correct for control number in ID code only with the first algorithm.

    The first algorithm can be calculated with ID code's first 10 numbers.
    Each number must be multiplied with its corresponding digit
    (in this task, corresponding digits are: 1 2 3 4 5 6 7 8 9 1), after which all the values are summarized
    and divided by 11. The remainder of calculation should be the control number.

    If the remainder is less than 10 and equal to the last number of ID code,
    then that's the correct control number and the function should return the ID code.
    Otherwise, the control number is either incorrect or the second algorithm should be used.
    In this case, return "Needs the second algorithm!".

    If the string contains more or less than 11 numbers, return "Incorrect ID code!".
    In other case use the previous algorithm to get the code number out of the string
    and find out, whether its control number is correct.

    The "Module 11" method is used to calculate the check number, using weights (multipliers).
    In the function the_first_control_number_algorithm(text: str), firstly, we use the following weights of the first scale (1 2 3 4 5 6 7 8 9 1).
    The calculation is made with the first 10 digits of the personal identification number. Each number is multiplied by the corresponding weight number from the first scale. The obtained values are summarized and divided by 11. If the remainder of the division is less than 10, then the reminder is the control number.
    If the reminder is greater than or equal to 10, then the control number is either incorrect or second scale weights must be used.

    :param text: string
    :return: string
    """
    id_code = find_id_code(text)
    if id_code in ["Not enough numbers!", "Too many numbers!"]:
        return "Incorrect ID code!"
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    sum_of_id_code_nr = sum(int(id_code[i]) * weights[i] for i in range(10))
    if sum_of_id_code_nr % 11 < 10:
        return (
            id_code
            if sum_of_id_code_nr % 11 == int(id_code[10])
            else "Incorrect ID code!"
        )

    else:
        return "Needs the second algorithm!"


def is_valid_gender_number(gender_nr: int) -> bool:
    """
    Check if given value is correct for gender number in ID code.

    :param gender_number: int
    :return: boolean
    """
    return gender_nr in range(1, 7)


def get_gender(gender_nr: int) -> str:
    """Check the gender of a person based on their gender number."""
    return "female" if gender_nr % 2 == 0 else "male"


def is_valid_year_number(year_number: int) -> bool:
    """Check if given value is correct for year number in ID code."""
    if 0 <= year_number <= 99:
        return True
    elif 1800 <= year_number <= 1899:
        return True
    elif 1900 <= year_number <= 1999:
        return True
    elif 2000 <= year_number <= 2099:
        return True
    elif 2100 <= year_number <= 2199:
        return True
    elif 2200 <= year_number <= 2299:
        return True
    else:
        return False


def is_valid_month_number(month_number: int) -> bool:
    """Check if given value is correct for month number in ID code."""
    return 1 <= month_number <= 12


def is_valid_birth_number(birth_number: int) -> bool:
    """Check if given value is correct for birth number in ID code."""
    return birth_number >= 1 and birth_number <= 999


def is_leap_year(year_number: int) -> bool:
    """Check if given value is correct for year number in ID code."""
    if year_number % 4 == 0:
        return (
            year_number % 100 == 0 and year_number % 400 == 0 or year_number % 100 != 0
        )
    else:
        return False


def get_full_year(gender_number: int, year_number: int) -> int:
    """Define the 4-digit year when given person was born."""
    if gender_number in range(1, 3):
        return 1800 + year_number
    elif gender_number in range(3, 5):
        return 1900 + year_number
    elif gender_number in range(5, 7):
        return 2000 + year_number
    else:
        return None


def get_birth_place(birth_number: int) -> str:
    """Find the place where the person was born."""
    if 1 <= birth_number <= 10:
        return "Kuressaare"
    elif 11 <= birth_number <= 20:
        return "Tartu"
    elif 21 <= birth_number <= 220:
        return "Tallinn"
    elif 221 <= birth_number <= 270:
        return "Kohtla-Järve"
    elif 271 <= birth_number <= 370:
        return "Tartu"
    elif 371 <= birth_number <= 420:
        return "Narva"
    elif 421 <= birth_number <= 470:
        return "Pärnu"
    elif 471 <= birth_number <= 710:
        return "Tallinn"
    elif 711 <= birth_number <= 999:
        return "undefined"
    else:
        return "Wrong input!"


def is_valid_control_number(id_code: str) -> bool:
    """Check if given value is correct for control number in ID code."""
    if the_first_control_number_algorithm(id_code) != "Needs the second algorithm!":
        return the_first_control_number_algorithm(id_code) == id_code
    weights = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    sum_of_id_code_nr = 0
    for i in range(10):
        sum_of_id_code_nr += int(id_code[i]) * weights[i]
        balance = sum_of_id_code_nr % 11
    if balance == 10:
        balance = 0
    return False if balance >= 10 else balance == int(id_code[10])


def is_valid_day_number(
    gender_number: int, year_number: int, month_number: int, day_number: int
) -> bool:
    """Check if given value is correct for day number in ID code."""
    # Write your code here
    days_in_a_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    if is_leap_year(get_full_year(gender_number, year_number)):
        days_in_a_month[2] = 29
    return 1 <= day_number <= days_in_a_month[month_number]


def is_id_valid(id_code: str) -> bool:
    """Check if given ID code is valid and return the result (True or False)."""
    if len(id_code) != 11 or len(id_code) < 11 or id_code.isdigit() is False:
        return False
    if not is_valid_year_number(int(id_code[1:3])):
        return False
    if not is_valid_gender_number(int(id_code[0])):
        return False
    if not is_valid_month_number(int(id_code[3:5])):
        return False
    if not is_valid_day_number(
        int(id_code[0]), int(id_code[1:3]), int(id_code[3:5]), int(id_code[5:7])
    ):
        return False
    if not is_valid_birth_number(int(id_code[7:10])):
        return False
    return is_valid_control_number(id_code)


def get_data_from_id(id_code: str) -> str:
    """Return the data from ID code."""
    if is_id_valid(id_code):
        return f"This is a {get_gender(int(id_code[0]))} born on {id_code[5:7]}.{id_code[3:5]}.{get_full_year(int(id_code[0]), int(id_code[1:3]))} in {get_birth_place(int(id_code[7:10]))}."
    else:
        return "Given invalid ID code!"


if __name__ == "__main__":
    print("\nFind ID code:")
    print(find_id_code(""))  # -> "Not enough numbers!"
    print(find_id_code("123456789123456789"))  # -> "Too many numbers!"
    print(find_id_code("ID code is: 49403136526"))  # -> "49403136526"
    print(find_id_code("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"

    print()
    print("The first control number algorithm:")
    print(the_first_control_number_algorithm(""))  # -> "Incorrect ID code!"
    print(
        the_first_control_number_algorithm("123456789123456789")
    )  # -> "Incorrect ID code!"
    print(
        the_first_control_number_algorithm("ID code is: 49403136526")
    )  # -> "49403136526"
    print(
        the_first_control_number_algorithm("efs4  9   #4aw0h 3r 1a36g5j2!!6-")
    )  # -> "49403136526"
    print(the_first_control_number_algorithm("50412057633"))  # -> "50412057633"
    print(
        the_first_control_number_algorithm(
            "Peeter's ID is euf50weird2fs0fsk51ef6t0s2yr7fyf4"
        )
    )  # -> "Needs
    # the second algorithm!"

    print("\nGender number:")
    for i in range(9):
        print(f"{i} {is_valid_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False

    print("\nGet gender:")
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(50))  # -> True

    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False

    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True

    print("\nLeap year:")
    print(is_leap_year(1804))  # -> True
    print(is_leap_year(1800))  # -> False

    print("\nGet full year:")
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001

    print("\nChecking where the person was born")
    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"
    print(get_birth_place(220))  # -> "Tallinn"
    print(get_birth_place(471))  # -> "Tallinn"

    print("\nControl number:")
    print(is_valid_control_number("49808270244"))  # -> True
    print(is_valid_control_number("60109200187"))  # -> False, it must be 6
    print(is_valid_control_number("49808270245"))  # -> False, it must be 4
    print(is_valid_control_number("50102080870"))  # -> True
    print(is_valid_control_number("47411136015"))  # -> True

    print("\nDay number:")
    print(is_valid_day_number(4, 5, 12, 25))  # -> True
    print(is_valid_day_number(3, 10, 8, 32))  # -> False
    print("\nFebruary check:")
    print(
        is_valid_day_number(4, 96, 2, 30)
    )  # -> False (February cannot contain more than 29 days in any circumstances)
    print(
        is_valid_day_number(4, 99, 2, 29)
    )  # -> False (February contains 29 days only during leap year)
    print(is_valid_day_number(4, 8, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(is_valid_day_number(4, 22, 4, 31))  # -> False (April contains max 30 days)
    print(is_valid_day_number(4, 18, 10, 31))  # -> True
    print(
        is_valid_day_number(4, 15, 9, 31)
    )  # -> False (September contains max 30 days)

    print("\nOverall ID check::")
    print(is_id_valid("49808270244"))  # -> True
    print(is_id_valid("12345678901"))  # -> False
    print(is_id_valid("49808270245"))  # -> False
    print(is_id_valid("60109200187"))  # -> False
    print(is_id_valid("50102080870"))  # -> True
    print(is_id_valid("47411136015"))  # -> True
    print(is_id_valid("34501234215"))  # -> True

    print("\nFull message:")
    print(
        get_data_from_id("49808270244")
    )  # -> "This is a female born on 27.08.1998 in Tallinn."
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"
    print(get_data_from_id("50102080870"))
    print(get_data_from_id("47411136015"))
    print(get_data_from_id("52343678901"))  # -> "Given invalid ID code!"
    print(get_data_from_id("34501234215"))  # ->
    print(get_data_from_id("49403136515"))
    print(get_data_from_id("37605030299"))
    # print("\nTest now your own ID code:")
    # personal_id = input()  # type your own id in command prompt
    # print(is_id_valid(personal_id))  # -> True
    # print(get_data_from_id(personal_id))
