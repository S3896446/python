def print_pattern(rows):
    for i in range(1, rows * 2):
        if i <= rows:
            stars = i
        else:
            stars = rows * 2 - i
        print("* " * stars)

if __name__ == "__main__":
    rows = 5
    print_pattern(rows)
