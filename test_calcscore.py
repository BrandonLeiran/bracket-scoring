import pytest
from calcscore import round_score

# you'll be picking what teams make it to the next round
#   - so picking 32, then 16, then 8, 4, 2, 1...i.e. round 1-6 winners
# teams will have a name & a seed
# seed doesn't change, so maybe make that not passed around w/ results

def test_round_score_invalid_round():
    with pytest.raises(ValueError, match=r".*range*"):
        round_score(0)

    with pytest.raises(ValueError, match=r".*range*"):
        round_score(7)

def test_round_score_invalid_winner():
    VALID_ROUND = 1
    all_teams = []
    round_winners = []
    picked_winners = ["picked team"]
    with pytest.raises(ValueError, match=r".*invalid winner"):
        round_score(VALID_ROUND, all_teams, round_winners, picked_winners)
    # score = round_score(0)

    # assert score == 0
