import math


def main() -> None:
    print("=== Game Coordinate System ===\n")
    data = [(10, 20, 5), "3,4,0", "abc,def,ghi"]
    start_data = (0, 0, 0)
    tuples = []
    for element in data:
        try:
            if (element.__class__ is tuple):
                print(f"Position created: {element}")
                x, y, z = element
                x1, y1, z1 = start_data
                try:
                    x2 = float(x)
                    y2 = float(y)
                    z2 = float(z)
                    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2
                                         + (z2 - z1)**2)
                    print(f"Distance between {start_data} and {element}:"
                          f" {distance:.2f}")
                    print()
                except ValueError as e:
                    print(e)
            elif (element.__class__ is str):
                elm = tuple(element.split(','))
                try:
                    x2, y2, z2 = elm
                    int(x2)
                    x2 = float(x2)
                    int(y2)
                    y2 = float(y2)
                    int(z2)
                    z2 = float(z2)
                    elm = (x2, y2, z2)
                    tuples += [elm]
                    x1, y1, z1 = start_data
                    print(f'Parsing coordinates: "{element}"')
                    print(f"Parsed position: ({x2:g}, {y2:g}, {z2:g}))")
                    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2
                                         + (z2 - z1)**2)
                    print(f"Distance between {start_data} and "
                          f"({x2:g}, {y2:g}, {z2:g}): {distance}")
                    print()
                except ValueError as e:
                    print(f'Parsing invalid coordinates: "{element}"')
                    msg, = e.args
                    print(f"Error parsing coordinates: {msg}")
                    print(f"Error details - Type: ValueError, Args: {e.args}")
                    print()
        except Exception as e:
            print(e)
    for t in tuples:
        x, y, z = t
        print("Unpacking demonstration:")
        print(f"Player at x={x:g}, y={y:g}, z={z:g}")
        print(f"Coordinates: X={x:g}, Y={y:g}, Z={z:g}")
        print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
