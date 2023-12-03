def calculate_score(opponent_move, your_move):
    """Calculates and returns the score for a single round."""
    # Mapping opponent and your moves to Rock, Paper, Scissors
    move_map = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
    # Mapping moves to score
    score_map = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
    # Determine the outcome
    if move_map[opponent_move] == move_map[your_move]:
        return score_map[move_map[your_move]] + 3  # Draw
    elif (move_map[opponent_move], move_map[your_move]) in [('Rock', 'Scissors'), ('Scissors', 'Paper'), ('Paper', 'Rock')]:
        return score_map[move_map[your_move]]  # Lose
    else:
        return score_map[move_map[your_move]] + 6  # Win

def process_file(file_path):
    """Processes the given file and returns the total score."""
    total_score = 0
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            line = line.strip()
            # Validate line format
            if len(line) != 3 or line[1] != ' ':
                raise ValueError(f"Invalid format in line {line_number}: '{line}'")
            opponent_move, your_move = line[0], line[2]
            # Validate moves
            if opponent_move not in 'ABC' or your_move not in 'XYZ':
                raise ValueError(f"Invalid move in line {line_number}: '{line}'")
            # Calculate and add round score
            total_score += calculate_score(opponent_move, your_move)
    return total_score

def run_tests():
    """Runs tests using the test.txt file."""
    test_score = process_file('../test.txt')
    print(f"Test score: {test_score}")
    assert test_score == 15, f"Test failed, expected 15, got {test_score}"
    print("Test passed.")

def main():
    # Run tests first
    try:
        run_tests()
    except Exception as e:
        print(f"Error during testing: {e}")
        return

    # Process the main input file
    try:
        final_score = process_file('../input.txt')
        print(f"Final score: {final_score}")
    except Exception as e:
        print(f"Error processing input.txt: {e}")

if __name__ == "__main__":
    main()
