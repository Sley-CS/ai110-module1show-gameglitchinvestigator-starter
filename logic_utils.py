DIFFICULTY_CONFIG = {
    "Easy":   {"range": (1, 20),  "attempts": 6},
    "Normal": {"range": (1, 50),  "attempts": 8},
    "Hard":   {"range": (1, 100), "attempts": 5},
}


def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    """Return (low, high) inclusive range for a given difficulty."""
    return DIFFICULTY_CONFIG[difficulty]["range"]


def parse_guess(raw: str): # 
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    s = str(raw).strip()
    if s == "":
        return False, None, "Enter a guess."

    # Reject common non-numeric formatting such as commas
    if "," in s:
        return False, None, "That is not a number."

    try:
        # Use float() to accept decimal and scientific notation
        f = float(s)
    except Exception:
        return False, None, "That is not a number."

    # Reject NaN and infinities
    if f != f or f in (float("inf"), float("-inf")):
        return False, None, "That is not a number."

    # If the value is an integer (e.g. 3.0), return an int
    if float(int(f)) == f:
        return True, int(f), None

    return True, f, None


def check_guess(guess: int, secret: int) -> tuple[str, str]:
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    elif guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        return current_score + max(10, 100 - 10 * attempt_number)
    if outcome in ("Too High", "Too Low"):
        return max(0, current_score - 5)
    return current_score
