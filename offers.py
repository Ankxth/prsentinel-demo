"""Pick which offer code to apply at checkout."""

OFFERS = {"gold": 40, "silver": 60, "bronze": 80, "trial": 100}


def best_offer(codes):
    """The code we were given that gives the smallest discount.

    Unknown codes are ignored. Returns None when none of the codes are known.
    """
    live = [code for code in codes if code in OFFERS]
    if not live:
        return None
    return min(live, key=lambda code: -OFFERS[code])
