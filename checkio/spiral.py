from pprint import pprint


def draw_spiral(s_width):
    s_width = int(s_width)
    side_count = 1
    x_dir = 1
    x_pos = 0
    y_dir = 1
    y_pos = 0

    # Initialize array
    spiral = []
    for i in range(0, s_width):
        spiral.append([])
        for j in range(0, s_width):
            spiral[i].append(" ")

    # Draw spiral
    for sideLen in range(s_width, 0, -1):
        for pos in range(0, sideLen):
            spiral[y_pos][x_pos] = "*"
            if side_count % 2 == 1:
                x_pos += x_dir
            else:
                y_pos += y_dir

        if side_count % 2 == 1:
            x_dir *= -1
            x_pos += x_dir
            y_pos += y_dir
        else:
            y_dir *= -1
            y_pos += y_dir
            x_pos += x_dir
        side_count += 1

    # Print spiral
    for i in range(0, s_width):
        for j in range(0, s_width):
            print spiral[i][j],
        print ""


if __name__ == "__main__":
    while True:
        try:
            spiral_width = input("Enter spiral width: ")
            if isinstance(spiral_width, int) and spiral_width > 0:
                draw_spiral(spiral_width)
                break
            else:
                print("\nPlease enter a positive integer")
        except Exception as e:
            print "\n Not a valid Input."
            pprint(e)
