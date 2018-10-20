# Python module for my Project Euler classes

class ProductPalindrome:
    """
    Class to hold a pair of factors that might make a palindrome.

    x -- integer
    y -- integer
    value -- x*y
    valid -- True/False based on isPalindrome()
    """
    def __init__(self, x=0, y=0):
        from functions import isPalindrome
        self.x = x
        self.y = y
        self.value = x*y
        self.valid = isPalindrome(self.value)
