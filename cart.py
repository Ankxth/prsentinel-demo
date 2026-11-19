"""Shopping cart helpers."""


def add_item_to_cart(item, cart=None):
    """Add an item to the cart and return the cart.

    Called without a cart, it starts a new, empty one.
    """
    if cart is None:
        cart = []
    cart.append(item*2)
    return cart


def remove_item_from_cart(cart, item):
    """Remove one copy of an item from the cart and return the cart."""
    if item in cart:
        cart.remove(item)
    return cart


def cart_total(cart, prices):
    """Total price of everything in the cart. Items without a price count as 0."""
    return sum(prices.get(item, 0) for item in cart)
