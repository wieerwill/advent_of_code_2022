def find_top_three_calories(file_path):
    """
    Finds the top three Elves carrying the most calories from a file.

    Args:
    file_path (str): Path to the file containing calorie counts.

    Returns:
    int: The sum of calories carried by the top three Elves.
    """
    with open(file_path, 'r') as file:
        calories_list = file.read()

    # Split the input into groups of calorie counts for each Elf
    elf_calorie_groups = calories_list.strip().split('\n\n')

    # Calculate calories for each Elf
    calories_sums = [sum(map(int, group.split('\n'))) for group in elf_calorie_groups]

    # Find the top three sums
    top_three_sums = sorted(calories_sums, reverse=True)[:3]

    return sum(top_three_sums)

def test():
    # Test the function
    total_calories = find_top_three_calories('../test.txt')

    # Assertion for testing
    assert total_calories == 45000, f"Expected 45000 calories but got {total_calories}"

    print(f"Test Passed: Total calories carried by the top three Elves: {total_calories}\n")

# Run the test
test()

# Use the function with actual input file
total_calories = find_top_three_calories('../input.txt')
print(f"From input.txt: Total calories carried by the top three Elves: {total_calories}")
