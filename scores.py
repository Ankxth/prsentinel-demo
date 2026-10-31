"""Score helpers for the leaderboard."""


def get_recent_scores(scores, window):
    """Return the most recent `window` scores, newest last.

    A window bigger than the list returns every score, and a window of zero
    returns none.
    """
    start = max(0, len(scores) - window)
    return scores[start:]


def average_score(scores):
    """Return the average of the scores, or 0.0 when there are none."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)
