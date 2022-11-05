"""Create schedule from the given file."""
import re
from datetime import datetime


def formatted_time(hours: str, minutes: str) -> str:
    """Format 24 hour time to the 12 hour time."""
    hours = int(hours)
    minutes = int(minutes)
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        return ""
    if hours < 12:
        am_pm = "AM"
        if hours == 0:
            hours = 12
    else:
        am_pm = "PM"
        if hours > 12:
            hours -= 12
    return "{:d}:{:02d} {}".format(hours, minutes, am_pm)


def create_schedule(input_string: str) -> list:
    """Create schedule."""
    schedule = {}

    return find_match(input_string, schedule)


def find_match(input_string, schedule):
    """Find schedule match."""
    for match in re.finditer(
            r"(?<=\s|\n)(\d{1,2})\D(\d{1,2})\s+([A-Za-z]+)", input_string
    ):
        times = formatted_time(match.group(1), match.group(2))
        if not times:
            continue

        entry = match.group(3).lower()

        if times not in schedule:
            schedule[times] = [entry]
        elif entry not in schedule[times]:
            schedule[times].append(entry)
    return sorted(schedule.items(), key=lambda x: datetime.strptime(x[0], "%I:%M %p"))


def empty_table() -> str:
    """Create table."""
    table = "--------------------\n" + "|  time | entries  |\n"
    table += "--------------------\n"
    table += "| No entries found |\n"
    table += "--------------------\n"
    return table


def not_empty_table(table: str) -> bool:
    """Check if table is not empty."""
    return table != empty_table()


def get_max_width_time(schedule: list) -> int:
    """Get max width of time."""
    max_width_time: int = 4

    for time, entry in schedule:
        width_time: int = len(time)
        max_width_time = max(max_width_time, width_time)

    return max_width_time


def get_width_entry(schedule: list) -> int:
    """Get max width of entries."""
    max_width_entry: int = 7

    for time, entry in schedule:
        width_entry: int = len(", ".join(entry))
        max_width_entry = max(max_width_entry, width_entry)

    return max_width_entry


def get_max_width(max_width_time: int, max_width_entry: int) -> int:
    """Get max width of table."""
    return max_width_time + max_width_entry + 7


def get_table_sizes(schedule: list) -> tuple:
    """Get table sizes."""
    max_width_time: int = get_max_width_time(schedule)
    max_width_entry: int = get_width_entry(schedule)
    return max_width_time, max_width_entry


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    schedule = create_schedule(input_string)
    if not schedule:
        return empty_table()
    max_width_time, max_width_entry = get_table_sizes(schedule)
    max_width = get_max_width(max_width_time, max_width_entry)
    table = tables(max_width, max_width_entry, max_width_time, schedule)
    return table


def tables(max_width, max_width_entry, max_width_time, schedule):
    """Create table."""
    table = "-" * max_width + "\n"
    table += "| {:>{}} | {:<{}} |\n".format(
        "time", max_width_time, "entries", max_width_entry
    )
    table += "-" * max_width + "\n"
    for time, entries in schedule:
        table += "| {:>{}} | {:<{}} |\n".format(
            time, max_width_time, ", ".join(entries), max_width_entry
        )
    table += "-" * max_width
    return table


def create_schedule_file(input_string: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    schedule = create_schedule(input_string)
    table = create_schedule_string(schedule)
    with open(output_filename, "w") as file:
        file.write(table)


if __name__ == "__main__":
    print(create_schedule_string("go 15:03 correct done"))
