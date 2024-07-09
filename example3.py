import math  # Added import for math module to use pi

# Corrected Python code with fixes for the intentional mistakes and errors

def calculate_area(radius):
    # Fixed: Added pi definition using math module
    area = math.pi * radius ** 2
    return area

def print_greeting(name):
    # Fixed: Corrected string concatenation and variable name typo
    greeting = f"Hello, {name}"  # Using f-string for better readability
    print(greeting)

def calculate_volume(length, width, height):
    # Fixed: Corrected formula for volume calculation
    volume = length * width * height
    return volume

if __name__ == '__main__':
    # Fixed: Corrected function name typo and added missing quotes around string
    area_of_circle = calculate_area(5)
    print("Area of the circle:", area_of_circle)

    print_greeting("John")  # Fixed: Added missing quotes around string

    # Fixed: Added missing argument for volume calculation
    volume_of_box = calculate_volume(5, 3, 2)
    print("Volume of the box:", volume_of_box)