def parse_range(range_str):
    """Parse a range string into start and end integers."""
    start, end = map(int, range_str.split('-'))
    return start, end

def is_contained(range1, range2):
    """Check if range1 is fully contained within range2."""
    start1, end1 = range1
    start2, end2 = range2
    return start2 <= start1 and end1 <= end2

def count_full_containments(file_path):
    """Count how many times one range in a pair fully contains the other."""
    count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                range1_str, range2_str = line.strip().split(',')
                range1 = parse_range(range1_str)
                range2 = parse_range(range2_str)

                if is_contained(range1, range2) or is_contained(range2, range1):
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
    test_result = count_full_containments('../test.txt')
    print(f"Test Result: {test_result}")
    assert test_result == 2, f"Test failed: Expected 2, got {test_result}"
    print("Test passed successfully.")

def main():
    """Main function to run the test and then process input.txt."""
    run_test()
    result = count_full_containments('../input.txt')
    print(f"Result from input.txt: {result}")

if __name__ == "__main__":
    main()
