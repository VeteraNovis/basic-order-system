from abc import ABC, abstractmethod

from order.authorisers import Authoriser, FailedToAuthoriseError
from order.order import Order


class PaymentProcessor(ABC):
    processor_name: str = ""
    _authorisers: list[Authoriser] = []

    def __init__(self, authorisers: list[Authoriser]):
        for authoriser in authorisers:
            self._authorisers.append(authoriser)

    def verify_payment(self) -> None:
        for auth in self._authorisers:
            auth.verify()

    @abstractmethod
    def pay(self, order: Order) -> None:
        pass


class DebitPaymentProcessor(PaymentProcessor):
    """Class responsibility: Pay for an order"""

    processor_name = "Debit"

    def pay(self, order: Order) -> None:
        print(f"Processing {self.processor_name} payment type")

        for authoriser in self._authorisers:
            if not authoriser.is_authorised():
                raise FailedToAuthoriseError(f"{authoriser.name} failed to verify")

        # Implement Debit payment here
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    """Class responsibility: Pay for an order"""

    processor_name = "Credit"

    def pay(self, order: Order) -> None:
        print(f"Processing {self.processor_name} payment type")

        for authoriser in self._authorisers:
            if not authoriser.is_authorised():
                raise FailedToAuthoriseError(f"{authoriser.name} failed to verify")

        # Implement Credit payment here
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
    """Class responsibility: Pay for an order"""

    processor_name = "Paypal"

    def pay(self, order: Order) -> None:
        print(f"Processing {self.processor_name} payment type")

        for authoriser in self._authorisers:
            if not authoriser.is_authorised():
                raise FailedToAuthoriseError(f"{authoriser.name} failed to verify")

        # Implement Paypal payment here
        order.status = "paid"


class BitcoinPaymentProcessor(PaymentProcessor):
    """Class responsibility: Pay for an order"""

    processor_name = "Bitcoin"

    def pay(self, order: Order) -> None:
        print(f"Processing {self.processor_name} payment type")

        for authoriser in self._authorisers:
            if not authoriser.is_authorised():
                raise FailedToAuthoriseError(f"{authoriser.name} failed to verify")

        # Implement Bitcoin payment here
        order.status = "paid"
