def parse_range(range_str):
    """Parse a range string into start and end integers."""
    start, end = map(int, range_str.split('-'))
    return start, end

def has_overlap(range1, range2):
    """Check if range1 overlaps with range2."""
    start1, end1 = range1
    start2, end2 = range2
    return start1 <= end2 and start2 <= end1

def count_overlaps(file_path):
    """Count how many pairs have overlapping ranges."""
    count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                range1_str, range2_str = line.strip().split(',')
                range1 = parse_range(range1_str)
                range2 = parse_range(range2_str)

                if has_overlap(range1, range2):
                    count += 1
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except ValueError:
        print(f"Error: Invalid format in line - {line}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return count

def run_test():
    """Run tests using test.txt and assert the expected outcomes."""
    test_result = count_overlaps('../test.txt')
    print(f"Test Result: {test_result}")
    assert test_result == 4, f"Test failed: Expected 4, got {test_result}"
    print("Test passed successfully.")

def main():
    """Main function to run the test and then process input.txt."""
    run_test()
    result = count_overlaps('../input.txt')
    print(f"Result from input.txt: {result}")

if __name__ == "__main__":
    main()
