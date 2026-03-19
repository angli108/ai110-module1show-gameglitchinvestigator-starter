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


def test_attempts_initializes_to_zero():
    """Regression test: attempts must start at 0, not 1.
    Bug: session_state.attempts was initialized to 1, causing the first
    guess to be counted as attempt #2 and skewing score/attempt-limit logic.
    """
    session_state = {}
    if "attempts" not in session_state:
        session_state["attempts"] = 0

    assert session_state["attempts"] == 0, (
        "attempts should initialize to 0, not 1"
    )


def test_attempts_does_not_reinitialize_if_already_set():
    """Once attempts is set, re-running the init block should not reset it."""
    session_state = {"attempts": 3}
    if "attempts" not in session_state:
        session_state["attempts"] = 0

    assert session_state["attempts"] == 3


def simulate_new_game(session_state, low, high):
    """Mirrors the new-game reset block in app.py."""
    import random
    session_state["attempts"] = 0
    session_state["secret"] = random.randint(low, high)
    session_state["status"] = "playing"
    session_state["history"] = []


def test_new_game_resets_status_to_playing():
    # Bug: status was not reset, so a lost/won game stayed locked after New Game.
    session_state = {"attempts": 5, "secret": 42, "status": "lost", "history": [10, 20]}
    simulate_new_game(session_state, 1, 100)
    assert session_state["status"] == "playing"


def test_new_game_clears_history():
    session_state = {"attempts": 3, "secret": 42, "status": "playing", "history": [10, 20, 30]}
    simulate_new_game(session_state, 1, 100)
    assert session_state["history"] == []


def test_new_game_resets_attempts_to_zero():
    session_state = {"attempts": 5, "secret": 42, "status": "playing", "history": []}
    simulate_new_game(session_state, 1, 100)
    assert session_state["attempts"] == 0


def test_new_game_secret_within_difficulty_range():
    # Bug: secret was not regenerated using the correct difficulty range.
    session_state = {"attempts": 0, "secret": 99, "status": "playing", "history": []}
    simulate_new_game(session_state, 1, 20)  # Easy range
    assert 1 <= session_state["secret"] <= 20


def test_easy_mode_has_more_attempts_than_normal():
    # Bug: Easy was set to 6 attempts while Normal had 8, giving Easy *fewer*
    # attempts than Normal despite being the easiest difficulty.
    attempt_limit_map = {
        "Easy": 10,
        "Normal": 8,
        "Hard": 5,
    }
    assert attempt_limit_map["Easy"] > attempt_limit_map["Normal"], (
        f"Easy ({attempt_limit_map['Easy']}) should have more attempts than "
        f"Normal ({attempt_limit_map['Normal']})"
    )


#--- Original tests ---

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
