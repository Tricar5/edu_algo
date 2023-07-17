"""
URL :

Идея:
1) хэшмапа для хранилища - храним тюплы (timestamp, value)
2) С помощью бинарного поиска ищем ближайшего соседа к целевому timestamp в get

"""

from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key] += [(timestamp, value)]


    def get(self, key: str, timestamp: int) -> str:
        res = ""
        ts = self.store[key]

        # Search Section
        l, r = 0, len(ts) - 1

        while l <= r:
            m = (l + r) // 2
            if ts[m][0] <= timestamp:
                res = ts[m][1]
                l = m + 1
            else:
                r = m - 1

        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)