import unittest
import os
import sys

# Annoying magic to make parent importing work for test dir
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from order.order import IncorrectStatusError, Order
from order.payment_processors import (
    DebitPaymentProcessor,
    PaypalPaymentProcessor,
    BitcoinPaymentProcessor,
)
from order.authorisers import SMSAuth, BitcoinAuth, EmailAuth, FailedToAuthoriseError


class TestAuthorisers(unittest.TestCase):
    def test_authoriser_status(self):
        auth = SMSAuth("12345")
        self.assertFalse(auth.authorised)
        auth.verify()
        self.assertTrue(auth.authorised)
        auth.authorised = False
        self.assertFalse(auth.authorised)

    def test_sms_authoriser_success(self):
        order = Order()
        processor = DebitPaymentProcessor([SMSAuth("12345")])
        processor.verify_payment()
        processor.pay(order)
        self.assertEqual(order.status, "paid")

    def test_email_authoriser_success(self):
        order = Order()
        processor = PaypalPaymentProcessor([EmailAuth("test@email.com")])
        processor.verify_payment()
        processor.pay(order)
        self.assertEqual(order.status, "paid")

    def test_bitcoin_authoriser_success(self):
        order = Order()
        processor = BitcoinPaymentProcessor([BitcoinAuth("1a74df32c09eb3")])
        processor.verify_payment()
        processor.pay(order)
        self.assertEqual(order.status, "paid")

    def test_sms_authoriser_failure(self):
        processor = DebitPaymentProcessor([SMSAuth("12345")])
        with self.assertRaises(FailedToAuthoriseError):
            processor.pay(Order())

    def test_email_authoriser_failure(self):
        processor = PaypalPaymentProcessor([EmailAuth("test@email.com")])
        with self.assertRaises(FailedToAuthoriseError):
            processor.pay(Order())

    def test_bitcoin_authoriser_failure(self):
        processor = BitcoinPaymentProcessor([BitcoinAuth("1a74df32c09eb3")])
        with self.assertRaises(FailedToAuthoriseError):
            processor.pay(Order())


if __name__ == "__main__":
    unittest.main()
