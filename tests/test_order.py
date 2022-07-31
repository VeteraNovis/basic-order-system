import unittest
import os
import sys

# Annoying magic to make parent importing work for test dir
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from order.order import IncorrectStatusError, Order


class TestOrder(unittest.TestCase):
    def test_order_total_price(self):
        order = Order()
        self.assertEqual(order.total_price(), 0)

        order.add_item("Test item 1", 1, 15)
        order.add_item("Test item 2", 2, 30)
        self.assertEqual(order.total_price(), 75)

        with self.assertRaises(ValueError):
            order.add_item("Test item 3", 2, -10)

    def test_order_status(self):
        order = Order()
        self.assertEqual(order.status, "open")

        order.status = "paid"
        self.assertEqual(order.status, "paid")

        with self.assertRaises(IncorrectStatusError):
            order.status = "incorrect status"


if __name__ == "__main__":
    unittest.main()
