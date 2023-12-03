def choose_shape(opponent_move, desired_outcome):
    """Chooses the appropriate shape based on the opponent's move and the desired outcome."""
    # Mapping of moves to counter-moves for loss, draw, win
    counter_moves = {
        'A': {'X': 'Scissors', 'Y': 'Rock', 'Z': 'Paper'},      # Opponent: Rock
        'B': {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'},      # Opponent: Paper
        'C': {'X': 'Paper', 'Y': 'Scissors', 'Z': 'Rock'}       # Opponent: Scissors
    }
    return counter_moves[opponent_move][desired_outcome]

def calculate_score(shape, outcome):
    """Calculates and returns the score for a single round."""
    score_map = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
    outcome_score = {'X': 0, 'Y': 3, 'Z': 6}  # Loss, Draw, Win
    return score_map[shape] + outcome_score[outcome]

def process_file(file_path):
    """Processes the given file and returns the total score."""
    total_score = 0
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            line = line.strip()
            # Validate line format
            if len(line) != 3 or line[1] != ' ':
                raise ValueError(f"Invalid format in line {line_number}: '{line}'")
            opponent_move, desired_outcome = line[0], line[2]
            # Validate moves
            if opponent_move not in 'ABC' or desired_outcome not in 'XYZ':
                raise ValueError(f"Invalid move in line {line_number}: '{line}'")
            # Determine the shape to choose
            your_shape = choose_shape(opponent_move, desired_outcome)
            # Calculate and add round score
            total_score += calculate_score(your_shape, desired_outcome)
    return total_score

def run_tests():
    """Runs tests using the test.txt file."""
    test_score = process_file('../test.txt')
    print(f"Test score: {test_score}")
    assert test_score == 12, f"Test failed, expected 12, got {test_score}"
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
