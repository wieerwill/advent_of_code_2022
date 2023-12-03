def calculate_item_priority(item):
    """Calculate the priority of the item based on its case and alphabetical position."""
    if 'a' <= item <= 'z':
        return ord(item) - ord('a') + 1
    elif 'A' <= item <= 'Z':
        return ord(item) - ord('A') + 27
    else:
        raise ValueError(f"Invalid item type: {item}")

def find_common_badge(rucksacks):
    """Find the common badge item type in a group of three rucksacks."""
    common_items = set(rucksacks[0])
    for rucksack in rucksacks[1:]:
        common_items.intersection_update(set(rucksack))
    if len(common_items) != 1:
        raise ValueError("Invalid group: no unique badge found")
    return common_items.pop()

def process_groups(file_path):
    """Process the groups of rucksacks from a file and return the sum of badge priorities."""
    total_priority = 0
    with open(file_path, 'r') as file:
        rucksacks = []
        for line in file:
            rucksacks.append(line.strip())
            if len(rucksacks) == 3:
                badge = find_common_badge(rucksacks)
                total_priority += calculate_item_priority(badge)
                rucksacks = []
    return total_priority

# Run tests and process the actual input
try:
    test_result = process_groups("../test.txt")
    print(f"Test Result: {test_result}")
    final_result = process_groups("../input.txt")
    print(f"Final Result: {final_result}")
except Exception as e:
    print(f"Error: {e}")
