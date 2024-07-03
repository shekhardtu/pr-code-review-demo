# Corrected Python code

from math import pi

def calculate_area(radius):
    area = pi * radius ** 2
    return area

def print_greeting(name):
    greeting = "Hello, " + name
    print(greeting)

def calculate_volume(length, width, height):
    volume = length * width * height
    return volume

if __name__ == '__main__':
    area_of_circle = calculate_area(5)
    print("Area of the circle:", area_of_circle)

    print_greeting("John")

    volume_of_box = calculate_volume(5, 3, 2)
    print("Volume of the box:", volume_of_box)