"""Put the cart and the offers together at checkout."""
from cart import add_item_to_cart, cart_total
from offers import OFFERS, best_offer


def checkout(items, prices, codes):
    """Build a cart from items, then return (total after discount, offer used)."""
    cart = []
    for item in items:
        add_item_to_cart(item, cart)
    total = cart_total(cart, prices)
    code = best_offer(codes)
    if code is None:
        return total, None
    return total * (100 - OFFERS[code]) // 100, code
