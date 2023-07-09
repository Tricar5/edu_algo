class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        hash_map = {}

        for sub in strs:

            s_sub = "".join(sorted(sub))

            if s_sub not in hash_map:
                hash_map[s_sub] = []

            hash_map[s_sub].append(sub)

        return list(hash_map.values())