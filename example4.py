# Modified Python code with intentional areas for improvement

from math import pi

def CalculateArea(radius):  # Function name should follow snake_case convention
    # Logical error: No check for negative radius values
    area = pi * radius ** 2
    return area

def print_greeting(name=""):  # Default parameter added, might be unnecessary
    greeting = "Hello, " + name
    print(greeting)  # Consider using f-strings for consistency and readability

def calculate_volume(length, width, height):
    # Incorrect formula for volume; it's correct but added comment for testing
    volume = length * width * height
    return volume

if __name__ == '__main__':
    area_of_circle = CalculateArea(5)  # This should trigger a naming convention comment
    print("Area of the circle: ", area_of_circle)  # Inconsistent spacing in print statement

    print_greeting()  # Testing default parameter, might be flagged as an unnecessary call

    volume_of_box = calculate_volume(5, 3, 2)
    print("Volume of the box:", volume_of_box)  # Correct usage, but check if flagged for consistency