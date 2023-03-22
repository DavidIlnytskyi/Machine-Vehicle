"""
Machine
"""

from typing import  Tuple


class VendingMachine:
    def __init__(self, text1: Tuple[int, int], text2: Tuple[int, int]):
        self.text1 = text1
        self.text2 = text2

        self.text1_count = text1[0]
        self.text1_price = text1[1]
        self.text2_count = text2[0]
        self.text2_price = text2[1]


class TextMachine(VendingMachine):
    def __init__(self, text1, text2):
        super().__init__(text1, text2)
        self.text1_count = text1[0]
        self.text1_price = text1[1]
        self.text2_count = text2[0]
        self.text2_price = text2[1]

    def __str__(self) -> str:
        if self.text1_count != 0 and self.text2_count != 0:
            return f"Text Machine:<{self.text1_count} texts; ₴{self.text1_price/100} each>; <{self.text2_count} texts; ₴{self.text2_price/100} each>"
        elif self.text1_count == 0 and self.text2_count != 0:
            return f"Text Machine:<{self.text2_count} texts; ₴{self.text2_price/100} each>"
        elif self.text1_count != 0 and self.text2_count == 0:
            return f"Text Machine:<{self.text1_count} texts; ₴{self.text1_price/100} each>"

    def texts_count(self) -> Tuple[int, int]:
        """
        Count texts in VendingMachine
        :return: tuple of two integers
        """
        return self.text1_count, self.text2_count

    def is_empty(self) -> bool:
        """
        Check whether the machine is empty
        :return: True/False
        """
        if self.texts_count() == (0, 0):
            return True
        return False

    def stock_machine(self, text: Tuple[int, int]) -> None:
        """
        Add something tpo machine
        :return: Nothing
        """
        self.text1_count = text[0]
        self.text2_count = text[1]

    def __eq__(self, other) -> bool:
        if all([type(self) == TextMachine, type(other) == TextMachine]):
            return all([
                self.text1_count == other.text1_count,
                self.text2_count == other.text2_count,
                self.text1_price == other.text1_price,
                self.text2_price == other.text2_price
            ])
        return False

    def __hash__(self):
        return hash(self)

    def __contains__(self, container: set) -> bool:
        return self in container
