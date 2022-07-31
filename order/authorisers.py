from abc import ABC, abstractmethod


class FailedToAuthoriseError(Exception):
    """Custom error class for failure to authorise payment"""

    def __init__(self, message: str):
        self._message = message
        super().__init__(self._message)


class Authoriser(ABC):
    def __init__(self):
        self._authorised = False
        self._name = ""

    @property
    def name(self):
        return self._name

    @property
    def authorised(self):
        return self._authorised

    @authorised.setter
    def authorised(self, status: bool) -> None:
        self._authorised = status

    @abstractmethod
    def verify(self) -> None:
        """Implement method to verify payment method"""

    @abstractmethod
    def is_authorised(self) -> bool:
        """Determine whether payment method has been verified"""


class SMSAuth(Authoriser):
    _name = "SMS authoriser"

    def __init__(self, code):
        super().__init__()
        self._code = code

    def verify(self) -> None:
        print(f"Verifying SMS code: {self._code}")

        # Implement SMS authentication here
        self.authorised = True

    def is_authorised(self) -> bool:
        return self.authorised


class NotARobot(Authoriser):
    _name = "'Not a robot' authoriser"

    def verify(self):
        print("Are you a robot?")

        # Implement "Are you a robot?" authentication here
        self.authorised = True

    def is_authorised(self) -> bool:
        return self.authorised


class EmailAuth(Authoriser):
    _name = "Email authoriser"

    def __init__(self, email):
        super().__init__()
        self._email = email

    def verify(self):
        print(f"Verifying email address: {self._email}")

        # Implement Email authentication here
        self.authorised = True

    def is_authorised(self) -> bool:
        return self.authorised


class BitcoinAuth(Authoriser):
    _name = "Bitcoin authoriser"

    def __init__(self, wallet_id):
        super().__init__()
        self._wallet_id = wallet_id

    def verify(self) -> None:
        print(f"Verifying Bitcoin wallet: {self._wallet_id}")

        # Implement Bitcoin authentication here
        self.authorised = True

    def is_authorised(self) -> bool:
        return self.authorised
