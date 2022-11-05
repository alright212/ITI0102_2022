"""File handling exercise."""

import csv
from datetime import datetime


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    filename = open(filename, "r")
    return filename.read()


def read_file_contents_to_list(filename: str) -> list:
    r"""
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.
    The order of the list should be the same as in the file.

    List elements should not contain new line (\n).

    :param filename: File to read.
    :return: List of lines.
    """
    filename = open(filename, "r")
    return [line.strip() for line in filename]


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    filename = open(filename, "r")
    reader = csv.reader(filename)
    return list(reader)


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file does not exist, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    filename = open(filename, "w")
    filename.write(contents)


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    with open(filename, "w") as file:
        file.write("\n".join(lines))


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def merge_dates_and_towns_into_csv(
    dates_filename: str, towns_filename: str, csv_output_filename: str
) -> None:
    """
    Merge information from two files into one CSV file.

    Dates file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    Towns file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.
    There are no headers in the input files.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    dates = read_file_contents_to_list(dates_filename)
    towns = read_file_contents_to_list(towns_filename)
    people = {}
    contents = ["name,town,date"]
    for date in dates:
        name, date = date.split(":")
        people[name] = [date, "-"]
    for town in towns:
        name, town = town.split(":")
        if name in people:
            people[name][1] = town
        else:
            people[name] = ["-", town]
    contents.extend(
        ",".join([name, value[1], people[name][0]]) for name, value in people.items()
    )

    write_lines_to_file(csv_output_filename, contents)


def read_csv_file_into_list_of_dicts(filename: str) -> list:
    """
    Read csv file into list of dictionaries.
    Header line will be used for dict keys.

    Each line after header line will result in a dict inside the result list.
    Every line contains the same number of fields.

    Example:
    name,age,sex
    John,12,M
    Mary,13,F

    Header line will be used as keys for each content line.
    The result:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    If there are only header or no rows in the CSV-file,
    the result is an empty list.

    The order of the elements in the list should be the same
    as the lines in the file (the first line becomes the first element etc.)

    :param filename: CSV-file to read.
    :return: List of dictionaries where keys are taken from the header.
    """
    data = read_csv_file(filename)
    return [] if len(data) == 0 else [dict(zip(data[0], row)) for row in data[1:]]


def write_list_of_dicts_to_csv_file(filename: str, data: list) -> None:
    """
    Write list of dicts into csv file.

    Data contains a list of dictionaries.
    Dictionary key represents the field.

    Example data:
    [
      {"name": "john", "age": "23"}
      {"name": "mary", "age": "44"}
    ]
    Will become:
    name,age
    john,23
    mary,44

    The order of fields/headers is not important.
    The order of lines is important (the same as in the list).

    Example:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]
    Will become:
    name,age,town
    john,12,
    mary,,London

    Fields which are not present in one line will be empty.

    The order of the lines in the file should be the same
    as the order of elements in the list.

    :param filename: File to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """

    headers = []
    values = []
    if not data:
        write_lines_to_file(filename, [])
        return None
    for dictionary in data:
        for key in dictionary:
            if key not in headers:
                headers.append(key)
    for dictionary in data:
        temp_values = []
        for header in headers:
            value = dictionary.get(header)
            if value is not None:
                temp_values.append(value)
            else:
                temp_values.append("")
        values.append(temp_values)
    write_csv_file(filename, [headers] + values)


def is_valid_date(date: str) -> bool:

    """
    1. Check if date is valid.
    2. If date is valid, return True.
    3. If date is invalid, return False.
    """

    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def date_conversion(date: str) -> str:
    """
    1. Convert date from YYYY-MM-DD to DD.MM.YYYY
    2. If date is invalid, return None
    """
    if is_valid_date(date):
        return datetime.strptime(date, "%Y-%m-%d").strftime("%d.%m.%Y")
    else:
        return None


def convert_the_ints(data: list)-> list:
    """
    1. Check if list contains valid ints.
    2. If list contains valid ints, return True.
    3. If list contains invalid ints, return False.
    4. Convert values to ints.
    5. Return list of ints.
    """
    int_list = []
    for row in data:
        if str(row).isdigit():
            int_list.append(int(row))
        elif not row:
            int_list.append(None)
        else:
            return data
    return int_list


def read_csv_file_into_list_of_dicts_using_datatypes(filename: str) -> list:
    """
    Read data from file and cast value into different datatypes.
    If a field contains only numbers, turn this into int.
    If a field contains only dates (in format dd.mm.yyyy), turn this into date.
    Otherwise the datatype is string (default by csv reader).

    Example:
    name,age
    john,11
    mary,14

    Becomes ('age' is int):
    [
      {'name': 'john', 'age': 11},
      {'name': 'mary', 'age': 14}
    ]

    But if all the fields cannot be cast to int, the field is left to string.
    Example:
    name,age
    john,11
    mary,14
    ago,unknown

    Becomes ('age' cannot be cast to int because of "ago"):
    [
      {'name': 'john', 'age': '11'},
      {'name': 'mary', 'age': '14'},
      {'name': 'ago', 'age': 'unknown'}
    ]

    Example:
    name,date
    john,01.01.2020
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': datetime.date(2020, 1, 1)},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    Example:
    name,date
    john,01.01.2020
    mary,late 2021

    Becomes:
    [
      {'name': 'john', 'date': "01.01.2020"},
      {'name': 'mary', 'date': "late 2021"},
    ]

    Value "-" indicates missing value and should be None in the result
    Example:
    name,date
    john,-
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': None},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    None value also doesn't affect the data type
    (the column will have the type based on the existing value).

    The order of the elements in the list should be the same
    as the lines in the file.

    For date, strptime can be used:
    https://docs.python.org/3/library/datetime.html#examples-of-usage-date
    """
    return read_csv_file_into_list_of_dicts(filename)

if __name__ == "__main__":
    # read_csv_file_into_list_of_dicts("input.csv")
    # print(read_csv_file_into_list_of_dicts("input.csv"))

    read_csv_file_into_list_of_dicts_using_datatypes("input.csv")
    print(read_csv_file_into_list_of_dicts_using_datatypes("input.csv"))
