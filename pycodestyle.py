def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    
    return sum(numbers) / len(numbers)


def main():
    """Main function."""
    numbers = [1, 2, 3, 4, 5]
    average = calculate_average(numbers)
    print(f"The average is: {average}")


if __name__ == "__main__":
    main()
