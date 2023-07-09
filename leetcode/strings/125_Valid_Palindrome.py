
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """


        import string
        t = ""


        for sym in s.lower():

            if sym not in string.punctuation and sym != ' ':

                t += sym

        n = len(t) // 2

        half = t[:n + 1]
        half_r = t[::-1][:n + 1]

        return half == half_r


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1

        while l < r:

            while l < r and s[l].isalnum() == False:
                l += 1

            while l < r and s[r].isalnum() == False:
                r -= 1

            if l > r or s[l].lower() != s[r].lower():
                return False

            else:
                l += 1
                r -= 1

        return True


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = [sym.lower() for sym in s if sym.isalnum()]

        return s == s[::-1]

c = Solution()

test_cases = [
    ("A man, a plan, a canal: Panama", True),
    ( "race a car", False),
    (" ", True)
]

for test in test_cases:

    assert c.isPalindrome(test[0]) == test[1], print(c.isPalindrome(test[0]))