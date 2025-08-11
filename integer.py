def generate_series(a):
    """
    Generates a series of odd numbers based on the input:
    - If 'a' is odd: generates first 'a' odd numbers.
    - If 'a' is even: generates first 'a - 1' odd numbers.

    Parameters:
    a (int): Input integer.

    Returns:
    list: A list of odd numbers.
    """
    count = a if a % 2 != 0 else a - 1
    return [2 * i + 1 for i in range(count)]


def main():
    try:
        a = int(input("Enter a positive integer: "))
        if a <= 0:
            print("Please enter a number greater than 0.")
            return

        series = generate_series(a)
        print("Output:", ', '.join(map(str, series)))

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()
