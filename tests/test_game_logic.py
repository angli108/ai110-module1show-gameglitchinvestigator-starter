from logic_utils import check_guess


# --- Tests targeting the two bugs that were fixed ---

def test_too_high_message_says_go_lower():
    # Bug: "Too High" was returning "Go HIGHER!" instead of "Go LOWER!"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message, got: {message!r}"

def test_too_low_message_says_go_higher():
    # Bug: "Too Low" was returning "Go LOWER!" instead of "Go HIGHER!"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message, got: {message!r}"

def test_numeric_comparison_not_string():
    # Bug: secret was cast to str on even attempts, causing "5" > "10" (string order)
    # to return "Too High" when 5 < 10 and should be "Too Low".
    outcome, _ = check_guess(5, 10)
    assert outcome == "Too Low", (
        f"Expected 'Too Low' for guess=5, secret=10, got {outcome!r}. "
        "String comparison '5' > '10' is True, which was the original bug."
    )


--- Original tests ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
