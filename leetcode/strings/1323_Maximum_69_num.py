"""

You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.


URL: https://leetcode.com/problems/maximum-69-number/description/
"""

class Solution:
    def maximum69Number(self, num: int) -> int:
        num_str = str(num)

        if '6' not in set(num_str):
            return num

        for i, n in enumerate(num_str):
            if n == '6':
                num_str = num_str[:i] + '9' + num_str[i + 1:]
                return int(num_str)