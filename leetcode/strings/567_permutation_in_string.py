"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def make_dict_from_string(s):

            d = {}
            for el in s:
                if el not in d.keys():
                    d[el] = 0
                d[el] += 1
            return d

        d_1 = make_dict_from_string(s1)

        len_s1 = len(s1)

        for i in range(len(s2)):

            if s2[i] in d_1.keys():
                if make_dict_from_string(s2[i:i+len_s1]) == d_1:
                    return True

        return False
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        def makeMap(s):

            hash = [0] * 26

            for el in s:
                hash[ord(el) - ord('a')] += 1

            return hash

        s1_map = makeMap(s1)

        len_s1 = len(s1)
        len_s2 = len(s2)

        for i in range(len_s2-len_s1 + 1):
            sub = s2[i:i+len_s1]
            s2_map = makeMap(sub)
            if s2_map == s1_map:
                return True

        return False


c = Solution()

"""
Изучить

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_table = [0] * 26
        s2_table = [0] * 26
        
        for c in s1:
            s1_table[ord(c) - 97] += 1
        
        l, r = 0, 0
        while r < len(s2):
            c = ord(s2[r])
            s2_table[c - 97] += 1
            while s2_table[c - 97] > s1_table[c - 97]:
                # move left
                t = ord(s2[l])
                s2_table[t - 97] -= 1
                l += 1
            if s1_table == s2_table:
                return True
            r += 1
        return False
        

"""

test_cases = [
    [["ab", "eidboaoo"], False],
    [["ab", "eidbaooo"], True],
    [["adc","dcda"], True]
]

for i, test in enumerate(test_cases):
    res = c.checkInclusion(test[0][0], test[0][1])
    assert res == test[1], AssertionError(f'Test {i} was not passed')