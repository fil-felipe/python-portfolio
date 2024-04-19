"""This module contain class with morse code converter."""

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


class MorseCodeConverter:
    """
    Object which allow to convert string into the morse code.

    Arguments:
        text_string: string
            Text which will be decoded into the morse code.
        character: string
            single character to be encoded into the morse code.

    Methods:
        set_code_sign:
            return single morse code sign for single character

        convert_string:
            return string with morse code signs based on the text_string argument
    """

    def __init__(self):
        self.text_string = ""
        self.morse_code = ""

    def set_text_uppercase(self):
        """Update argument text_string to have all letters uppercase."""
        self.text_string = self.text_string.upper()

    @staticmethod
    def verify_character(character):
        """Return True if character exist in the morse code dict."""
        if character == " " or character in MORSE_CODE_DICT:
            return True

        print(f"Character '{character}' not found in the morse code dictionary. Convert failed.")
        return False

    @staticmethod
    def set_code_sign(character):
        """Return morse code for single character based on the morse code dict."""
        if character == " ":
            return " "

        return MORSE_CODE_DICT.get(character)

    def convert_string(self, text_string):
        """return string with morse code signs based on the text_string argument"""
        self.text_string = text_string
        self.set_text_uppercase()

        for character in self.text_string:
            if not self.verify_character(character):
                return ""

            new_code = self.set_code_sign(character)
            if new_code is None:
                print(f"Missing morse code for character {character}. Convert failed.")
                return ""
            self.morse_code += new_code

        print("Text string successfully converted into the morse code:")
        return self.morse_code


