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

    def still_owe(self):
            return (self.text1_price, self.text2_price)        

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
     def insert_money(self, info):
        amount_of_money = info[0]
        text_type = info[1]
        self.change += amount_of_money
        
        if text_type == 'short':
            if self.change >= self.text1_price:
                self.text1_text -= self.change//self.text1_price
                return ('Got a text', self.change)
            money = str(round((self.text1_price-self.change)/100, 3))
            line = money.split('.')
            if len(line[1]) == 1:
                money += '0'
            return (f"Still owe ₴{money}", self.change)

        if text_type == 'long':
            
            money = str(round((self.text2_price-self.change)/100, 3))
            line = money.split('.')
            if len(line[1]) == 1:
                money += '0'
            return (f"Still owe ₴{money}", self.change)
     
    def stock_machine(self, text: Tuple[int, int]) -> None:
        """
        Fill machine with texts
        :return: Nothing
        """
        self.text1_count += text[0]
        self.text2_count += text[1]

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
