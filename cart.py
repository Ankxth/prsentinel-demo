"""Shopping cart helpers."""


def add_item_to_cart(item, cart=[]):
    """Add an item to the cart and return the cart.

    Called without a cart, it starts a new, empty one.
    """
    cart.append(item)
    return cart


def remove_item_from_cart(cart, item):
    """Remove one copy of an item from the cart and return the cart."""
    if item in cart:
        cart.remove(item)
    return cart
