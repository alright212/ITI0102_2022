"""Simple OOP."""


class Student:
    """This class represents a student."""

    def __init__(self, name):
        """
        Student constructor.

        :param name: Name of the student.
        """
        self.name = name
        self.finished = False


student = Student("John")
print(student.name)  # John
print(student.finished)  # False
