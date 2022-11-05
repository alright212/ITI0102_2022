"""EX01 Hello."""


"""
1. Print Hello
Example output:

What is your name? Mari
Hello, Mari! Enter a random number: 5
Great! Now enter a second random number: 4
5 + 4 is 9

"""
name = input("What is your name? ")
print(f"Hello, {name}!")
num1 = int(input("Enter a random number: "))
num2 = int(input("Great! Now enter a second random number: "))
print(f"{num1} + {num2} is {num1 + num2}")
