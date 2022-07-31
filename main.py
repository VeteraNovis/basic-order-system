import os
import unittest

from order.order import Order
from order.authorisers import FailedToAuthoriseError
from order.authorisers import BitcoinAuth, EmailAuth, NotARobot, SMSAuth
from order.payment_processors import BitcoinPaymentProcessor
from order.payment_processors import CreditPaymentProcessor
from order.payment_processors import DebitPaymentProcessor
from order.payment_processors import PaypalPaymentProcessor


def pay_with_debit():
    authoriser_list = [SMSAuth("12345")]
    return DebitPaymentProcessor(authoriser_list)


def pay_with_credit():
    authoriser_list = []
    return CreditPaymentProcessor(authoriser_list)


def pay_with_paypal():
    authoriser_list = [SMSAuth("12345"), NotARobot(), EmailAuth("test@email.com")]
    return PaypalPaymentProcessor(authoriser_list)


def pay_with_bitcoin():
    authoriser_list = [
        SMSAuth("12345"),
        EmailAuth("test@email.com"),
        BitcoinAuth("3af3ae92c30d"),
    ]
    return BitcoinPaymentProcessor(authoriser_list)


def run_unittest(test_path, test_pattern):
    print(f"Discovering tests in : {test_path}")
    suite = unittest.TestLoader().discover(test_path, test_pattern)
    unittest.TextTestRunner(verbosity=2).run(suite)


def main():
    # Run unittests
    root_path = os.path.abspath(".")
    test_path = os.path.join(root_path, "tests/")
    test_pattern = "test_*"
    run_unittest(test_path, test_pattern)

    # Create new order
    order = Order()

    # Add items to the order
    order.add_item("keyboard", 1, 15)
    order.add_item("mouse", 1, 5)
    order.add_item("monitor", 2, 30)

    # Setup processor for desired payment type & authentication
    processor = pay_with_bitcoin()

    # Verify successful authentication
    processor.verify_payment()

    # Attempt to pay for the for order
    try:
        processor.pay(order)
    except FailedToAuthoriseError as e:
        print(f"Error: {e}")
    else:
        print(f"Order status: {order.status}")


if __name__ == "__main__":
    main()
