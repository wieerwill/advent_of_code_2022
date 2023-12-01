def find_max_calories(file_path):
    """
    Finds the Elf carrying the most calories from a file.

    Args:
    file_path (str): Path to the file containing calorie counts.

    Returns:
    int, int: The index of the Elf and the maximum calories carried by that Elf.
    """
    with open(file_path, 'r') as file:
        calories_list = file.read()

    # Split the input into groups of calorie counts for each Elf
    elf_calorie_groups = calories_list.strip().split('\n\n')

    # Sum the calories for each Elf
    max_calories = 0
    max_elf_index = 0
    for index, group in enumerate(elf_calorie_groups):
        sum_calories = sum(map(int, group.split('\n')))
        if sum_calories > max_calories:
            max_calories = sum_calories
            max_elf_index = index + 1

    return max_elf_index, max_calories

def test():
    # Test the function
    max_elf_index, max_calories = find_max_calories('../test.txt')

    # Assertions for testing
    assert max_elf_index == 4, f"Expected Elf 4 but got Elf {max_elf_index}"
    assert max_calories == 24000, f"Expected 24000 calories but got {max_calories}"

    print(f"Test Passed: Elf {max_elf_index} is carrying the most calories: {max_calories} Calories\n")

# Run the test
test()

# Use the function with actual input file
max_elf_index, max_calories = find_max_calories('../input.txt')
print(f"From input.txt: Elf {max_elf_index} is carrying the most calories: {max_calories} Calories")
