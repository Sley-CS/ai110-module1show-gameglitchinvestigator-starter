import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, update_score, parse_guess, get_range_for_difficulty


# ── check_guess ───────────────────────────────────────────────────────────────

def test_correct_guess_returns_win():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_correct_guess_message():
    _, message = check_guess(50, 50)
    assert "Correct" in message

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_high_hint_says_lower():
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_guess_too_low_hint_says_higher():
    _, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_guess_boundary_low_end():
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"

def test_guess_boundary_high_end():
    outcome, _ = check_guess(100, 100)
    assert outcome == "Win"

def test_one_below_secret_is_too_low():
    outcome, _ = check_guess(49, 50)
    assert outcome == "Too Low"

def test_one_above_secret_is_too_high():
    outcome, _ = check_guess(51, 50)
    assert outcome == "Too High"


# ── update_score ──────────────────────────────────────────────────────────────

def test_win_on_first_attempt_gives_max_points():
    score = update_score(0, "Win", 1)
    assert score == 90  # 100 - 10*1

def test_win_score_decreases_with_more_attempts():
    early = update_score(0, "Win", 2)
    late  = update_score(0, "Win", 5)
    assert early > late

def test_win_score_never_below_10():
    score = update_score(0, "Win", 100)
    assert score >= 10

def test_wrong_guess_deducts_points():
    score = update_score(50, "Too High", 1)
    assert score == 45

def test_too_low_also_deducts_points():
    score = update_score(50, "Too Low", 1)
    assert score == 45

def test_score_never_goes_negative():
    score = update_score(0, "Too High", 1)
    assert score == 0

def test_unknown_outcome_leaves_score_unchanged():
    score = update_score(42, "Unknown", 1)
    assert score == 42


# ── parse_guess ───────────────────────────────────────────────────────────────

def test_valid_integer_string():
    ok, value, err = parse_guess("25")
    assert ok is True
    assert value == 25
    assert err is None

def test_empty_string_is_invalid():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_none_input_is_invalid():
    ok, value, err = parse_guess(None)
    assert ok is False

def test_letters_are_invalid():
    ok, _, err = parse_guess("abc")
    assert ok is False
    assert err is not None

def test_decimal_rounds_to_int():
    ok, value, _ = parse_guess("7.0")
    assert ok is True
    assert value == 7

def test_negative_number_parses():
    ok, value, _ = parse_guess("-5")
    assert ok is True
    assert value == -5

def test_comma_is_invalid():
    ok, _, _ = parse_guess("1,000")
    assert ok is False


# ── get_range_for_difficulty ──────────────────────────────────────────────────

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 50

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 100


# ── full game simulation ──────────────────────────────────────────────────────

def test_robot_plays_and_wins():
    secret = 37
    score = 0
    attempts = 0
    status = "playing"

    guesses = [50, 25, 37]  # high, low, correct

    for guess in guesses:
        attempts += 1
        outcome, _ = check_guess(guess, secret)
        score = update_score(score, outcome, attempts)
        if outcome == "Win":
            status = "won"
            break

    assert status == "won"
    assert attempts == 3
    assert score > 0
    print(f"✅ Robot won in {attempts} attempts with a score of {score}!")


def test_robot_loses_when_out_of_attempts():
    secret = 37
    attempt_limit = 3
    score = 0
    attempts = 0
    status = "playing"

    wrong_guesses = [10, 20, 30]  # all too low, never wins

    for guess in wrong_guesses:
        attempts += 1
        outcome, _ = check_guess(guess, secret)
        score = update_score(score, outcome, attempts)
        if outcome == "Win":
            status = "won"
            break
        if attempts >= attempt_limit:
            status = "lost"
            break

    assert status == "lost"
    assert score == 0  # started at 0, deducted to floor of 0
    print(f"🤖 Robot lost after {attempts} attempts as expected.")
