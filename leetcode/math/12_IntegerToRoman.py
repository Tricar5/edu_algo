"""
URL:

Ideas:
1) Создать словарь/кортеж для конвертации с i, j
2) Пока n больше текущего элемента i:
    Вычитать i
    Прибавлять в выходную строку j
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""

        conv = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        for i, j in conv.items():

            while num >= i:
                num -= i
                roman += j

        return roman