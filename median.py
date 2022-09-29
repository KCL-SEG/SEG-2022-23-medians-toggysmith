"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]

        numbers.sort()

        if len(numbers) % 2 == 0: # If even
            first_number = numbers[len(numbers) // 2 - 1]
            second_number = numbers[len(numbers) // 2]

            print((first_number + second_number) / 2)
        else: # If odd:
            print(numbers[len(numbers) // 2])
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
