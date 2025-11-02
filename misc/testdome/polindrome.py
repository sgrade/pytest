# https://www.testdome.com/d/python-interview-questions/9
"""A palindrome is a word that reads the same backward or forward.

Write a function that checks if a given word is a palindrome. Character case should be ignored.

For example, is_palindrome("Deleveled") should return True as character case should be ignored, resulting in "deleveled", which is a palindrome since it reads the same backward and forward."""

class Palindrome:

    @staticmethod
    def is_palindrome(word):
        reversed_word = word[::-1]
        if word.lower() == reversed_word.lower():
            return True
        else:
            return False

print(Palindrome.is_palindrome('Deleveled'))