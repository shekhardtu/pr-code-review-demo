from math import pi

def calculate_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    area = pi * radius ** 2
    return area

def print_greeting(name: str) -> None:
    greeting = f"Hello, {name}"
    print(greeting)

def calculate_volume(length: float, width: float, height: float) -> float:
    if length < 0 or width < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    volume = length * width * height
    return volume

def main() -> None:
    area_of_circle = calculate_area(5)
    print("Area of the circle:", area_of_circle)

    print_greeting("John")

    volume_of_box = calculate_volume(5, 3, 2)
    print("Volume of the box:", volume_of_box)

if __name__ == '__main__':
    main()