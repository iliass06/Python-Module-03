import sys
import math


def calculate_distance(pos1: tuple, pos2: tuple) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


def ft_from_input() -> None:
    origin = (0, 0, 0)
    if len(sys.argv) == 2:
        try:
            pos = tuple(int(x) for x in sys.argv[1].split(","))
        except ValueError:
            print("Error: invalid arguments. Using default coordinates.")
            pos = (10, 20, 5)
    elif len(sys.argv) > 2:
        print("Error: too many arguments. Using default coordinates.")
        pos = (10, 20, 5)
    else:
        pos = (10, 20, 5)
    print(f"\nPosition created: {pos}")
    distance = calculate_distance(origin, pos)
    print(f"Distance between {origin} and {pos}: {distance:.2f}")


def ft_coordinate_system(position: str) -> None:
    origin = (0, 0, 0)
    try:
        pos = tuple(int(x) for x in position.split(","))
        print(f"Parsed position: {pos}")
        distance = calculate_distance(origin, pos)
        print(f"Distance between {origin} and {pos}: {distance:.1f}")
    except ValueError as e:
        msg, = e.args
        print(f"Error parsing coordinates: {msg}")
        print(f"Error details - Type: ValueError, Args: {e.args}")


if __name__ == "__main__":
    try:
        print("=== Game Coordinate System ===")
        ft_from_input()
        print("\nParsing coordinates: \"3,4,0\"")
        ft_coordinate_system("3,4,0")
        print("\nParsing invalid coordinates: \"abc,def,ghi\"")
        ft_coordinate_system("abc,def,ghi")
        pos = (3, 4, 0)
        print("\nUnpacking demonstration:")
        x, y, z = pos
        X, Y, Z = pos
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={X}, Y={Y}, Z={Z}")
    except Exception as e:
        print(f"Error: {e}")
