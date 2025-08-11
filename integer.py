from typing import List


def generate_odd_series(n: int) -> List[int]:
    """
    Generate a list of odd numbers based on the input integer 'n'.

    Rules:
    - If 'n' is odd: return first 'n' odd numbers.
    - If 'n' is even: return first 'n - 1' odd numbers.

    Parameters:
    ----------
    n : int
        The input integer

    Returns:
    -------
    List[int]
        A list of odd numbers as per the described rules.
    """
    count = n if n % 2 != 0 else n - 1
    return [2 * i + 1 for i in range(count)]


def get_user_input() -> int:
    """
    Prompt the user for input and validate it.

    Returns:
    -------
    int
        A valid positive integer input from the user.
    """
    while True:
        try:
            user_input = int(input("Enter a positive integer: "))
            if user_input > 0:
                return user_input
            else:
                print("Input must be a positive integer greater than zero.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def display_series(series: List[int]) -> None:
    """
    Print the list of numbers in a comma-separated format.

    Parameters:
    ----------
    series : List[int]
        The list of odd numbers to display.
    """
    print("Output:", ', '.join(map(str, series)))


def main() -> None:
    """
    Main function to run the odd series generator.
    """
    a = get_user_input()
    odd_series = generate_odd_series(a)
    display_series(odd_series)


if __name__ == "__main__":
    main()
