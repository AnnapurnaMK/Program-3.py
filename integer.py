def generate_series(a: int) -> list[int]:
    count = a if a % 2 else a - 1
    return [2 * i + 1 for i in range(count)]

def main():
    try:
        a = int(input("Enter a positive integer: "))
        if a <= 0:
            raise ValueError
        print("Output:", ', '.join(map(str, generate_series(a))))
    except ValueError:
        print("Invalid input! Please enter a positive integer.")

if __name__ == "__main__":
    main()
