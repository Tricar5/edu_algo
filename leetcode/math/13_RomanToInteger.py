"""

URL: https://leetcode.com/problems/roman-to-integer/description/

Идея:
1) Завести словарь/кортеж с парами ROMAN/INT. Отсортировать этот объект по длине строки и номинальну по убыванию
2) Идти по этому словарю
3) Проверяем вхождение подстроки в исходную. Если находим, то:
    1) Прибавляем к переменной num: Берем INT по словарю и умножаем на количество вхождений подстроки
    2) Заменяем эту подстроку на пустую

4) Возвращаем num
"""

class Solution:
    def romanToInt(self, s: str) -> int:

        num = 0

        conv = {

            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4,
            "M": 1000,
            "D" : 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }

        for i, j in conv.items():

            if i in s:
                num += j * s.count(i)
                s = s.replace(i, "")

        return num