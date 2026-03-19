#FIX: moved the function here from app.py.
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100

#FIX: moved the function here from app.py.
def parse_guess(raw: str):
    """Validates and converts the raw text input into an integer. Returns a tuple (ok, value,
  error_message). Handles floats (truncates them) and non-numeric strings."""
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: Messages were swapped — "Too High" said "Go HIGHER!" and "Too Low" said "Go LOWER!".
    # AI corrected the messages and moved the function here from app.py.
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


#FIX: moved the function here from app.py.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Adjusts the score based on the outcome:
        - Win → 100 - 10 * (attempt + 1), minimum 10 points
        - Too High on even attempt → +5 points (rewards even-attempt high guesses)
        - Too High on odd attempt → -5 points
        - Too Low → always -5 points
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
