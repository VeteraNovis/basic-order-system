"""Build a shopping order to test out OOP principles"""


class IncorrectStatusError(Exception):
    def __init__(self, message: str):
        self._message = message
        super().__init__(message)


class Order:
    """Class responsibility: Create an order"""

    _items = []
    _quantities = []
    _prices = []
    _status = "open"

    def add_item(self, name: str, quantity: int, price: float) -> None:
        """Add an item to the order"""
        if price < 0:
            raise ValueError("Price cannot be negative")

        self._items.append(name)
        self._quantities.append(quantity)
        self._prices.append(price)

    def total_price(self):
        total = 0
        for i, val in enumerate(self._prices):
            total += val * self._quantities[i]
        return total

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, new_status: str) -> None:
        if new_status in ("paid", "open"):
            self._status = new_status
        else:
            raise IncorrectStatusError(f"Unknown status type {new_status}")
