"""Math."""


def average(a: int, b: int, c: int, d: int) -> float:
    """
    Implement a function that has 4 numeric parameters.

    Each parameter must be multiplied by number of its position in the function (x, y, z = 1, 2, 3).
    Calculate and return the average.

    Examples:
    average(0, 0, 0, 4) === 4
    average(1, 2, 3, 4) == 7.5
    average(5, 0, 5, 1) == 6
    """
    if a == 0 and b == 0 and c == 0 and d == 0:
        return 0
    else:
        return (a + 2 * b + 3 * c + 4 * d) / 4


def school_pressure(ects: int, weeks: int) -> float:
    """
    Implement a function to know how many hours are needed per week if each ECTS is 26 hours.

    If it's not possible in time then return -1.

    Examples:
    school_pressure(30, 12) == 65
    school_pressure(1, 1) == 26
    school_pressure(1, 0) == -1
    """
    hours_per_week = 7 * 24
    hours_per_ects = 26
    if ects * hours_per_ects > hours_per_week * weeks:
        return -1
    try:
        return ects * hours_per_ects / weeks
    except ZeroDivisionError:
        return -1


def add_fractions(a: int, b: int, c: int, d: int) -> str:
    """
    Implement a function that takes 4 parameters.

    Parameters a and b denote the first fraction like a/b.
    Parameters c and d denote the second fraction like c/d.

    Find and return a fraction in string format that is the sum of a/b and c/d.

    NB! the fraction does not have to be in the simplest form.
    NB! the answer should not contain any commas.

    Examples:
    add_fractions(1, 3, 1, 3) # 1/3 + 1/3 => there are many correct answers like "2/3" and "6/9"
    add_fractions(2, 5, 1, 5) # 2/5 + 1/5 => there are many correct answers like "3/5" and "15/25"
    """
    return f"{str(a * d + b * c)}/{str(b * d)}"


print(
    add_fractions(1, 2, 1, 2)
)  # => 1/2 + 1/2 => Possible results "1/1", "4/4", "2/2", etc
print(
    add_fractions(3, 1, 1, 1)
)  # => 3/1 + 1/1 => Possible results "4/1", "16/4", "8/2", etc
print(
    add_fractions(1, 6, 3, 5)
)  # => 1/6 + 3/5 => Possible results "23/30", "46/60", etc


print(school_pressure(30, 12))
print(school_pressure(1, 1))
