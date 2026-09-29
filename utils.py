def print_title(text, width=60):
    line = "=" * width
    print(line)
    print(text.center(width))
    print(line)


def print_rule(width=60):
    print("-" * width)


def get_number(message, minimum=0, maximum=None):
    """Read a numeric value and keep asking until it is valid."""
    while True:
        try:
            value = float(input(message))
            if value < minimum:
                print("  -> Please enter a value within the allowed range.")
                continue
            if maximum is not None and value > maximum:
                print("  -> Please enter a value within the allowed range.")
                continue
            return value
        except ValueError:
            print("  -> Please enter a valid numeric value.")
