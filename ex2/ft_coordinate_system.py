import sys
import math

def ft_from_input():
    origin = (0, 0, 0)
    try:    
        pos = tuple(int(x) for x in sys.argv[1].split(","))
    except Exception as e:
        print(f"Error: Invalide Arguments!!")
        pos = (10, 20, 5)
        print(f"Using default coordinats {pos}")

    print(f"\nPosition created: {pos}")
    distance = math.sqrt((pos[0]-origin[0])**2 + (pos[1]-origin[1])**2 + (pos[2]-origin[2])**2)
    print(f"Distance between {origin} and {pos}: {distance:.2f}")

def ft_coordinate_system(position):
    origin = (0, 0, 0)
    try:
        pos = tuple(int(x) for x in position.split(","))
        print(f"Parsed position: {pos}")
        distance = math.sqrt((pos[0]-origin[0])**2 + (pos[1]-origin[1])**2 + (pos[2]-origin[2])**2)
        print(f"Distance between {origin} and {pos}: {distance:.1f}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: (\"{e}\",)")
if __name__ == "__main__":
    try:
        print("=== Game Coordinate System ===")
        ft_from_input()
        print(f"\nParsing coordinates: \"3,4,0\"")
        ft_coordinate_system("3,4,0")
        print(f"\nParsing invalid coordinates: \"abc,def,ghi\"")
        ft_coordinate_system("abc,def,ghi")
        pos = (3, 4, 0)
        print("\nUnpacking demonstration:")
        x, y, z = pos
        X, Y, Z = pos
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={X}, Y={Y}, Z={Z}")
    except Exception as e:
        print(f"Error: {e}")