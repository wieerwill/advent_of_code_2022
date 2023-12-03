def calculate_item_priority(item):
    """Calculate the priority of the item based on its case and alphabetical position."""
    if 'a' <= item <= 'z':
        return ord(item) - ord('a') + 1
    elif 'A' <= item <= 'Z':
        return ord(item) - ord('A') + 27
    else:
        raise ValueError(f"Invalid item type: {item}")

def find_common_item(rucksack):
    """Find the common item type that appears in both compartments of the rucksack."""
    half_length = len(rucksack) // 2
    first_compartment = set(rucksack[:half_length])
    second_compartment = rucksack[half_length:]

    for item in second_compartment:
        if item in first_compartment:
            return item
    raise ValueError("No common item type found in both compartments")

def process_rucksack_contents(file_path, is_test=False):
    """Process the contents of rucksacks from a file and return the sum of item priorities."""
    total_priority = 0
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) % 2 != 0:
                raise ValueError("Rucksack contents must be of even length")
            common_item = find_common_item(line)
            item_priority = calculate_item_priority(common_item)
            total_priority += item_priority
            if is_test:
                print(f"Rucksack: {line}, Common Item: '{common_item}', Priority: {item_priority}")
    return total_priority

def run_tests():
    """Run tests to validate the algorithm with predefined test cases."""
    test_result = process_rucksack_contents("../test.txt", is_test=True)
    print(f"Test Result: {test_result}")
    assert test_result == 157, f"Test failed, expected 157 but got {test_result}"
    print("Test passed successfully.")

def main():
    """Main function to process the actual input and display the result."""
    try:
        run_tests()  # First, run the tests
        final_result = process_rucksack_contents("../input.txt")  # Then process the actual input
        print(f"Final Result: {final_result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
