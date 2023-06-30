class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort()

        output = [intervals[0]]

        for start, end in intervals:
            last_end = output[-1][1]

            if start <= last_end:
                output[-1][1] = max(last_end, end)

            else:
                output.append([start, end])

        return output