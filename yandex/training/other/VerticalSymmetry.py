

def checkIfVerticalLineExists(points):

    # Краевой случай
    if len(points) == 0:
        return False

    hash_map = {}

    min_x = points[0][0]
    max_x = points[0][0]

    for el in points:

        x = el[0]
        if x not in hash_map.keys():
            hash_map[x] = set()

        hash_map[x].add(el[1])

        min_x = min(min_x, el[0])
        max_x = max(max_x, el[0])

    avg_x = (max_x - min_x) / 2

    for key in hash_map.keys():
        if key <= avg_x:
            d = key - min_x
        else:
            d = max_x - key

        if min_x + d in hash_map.keys() and max_x - d in hash_map.keys():

            if hash_map[min_x + d] != hash_map[max_x - d]:
                return False

        else:
            return False

    return True


test_cases = [
    [[(1,0), (3, 0)], True],
    [[], False],
    [[(2, 3), (1, 0), (0, 0), (-2, 3), (-1, 0)], True],
    [[(2, -3), (1, 1), (0, 0), (-2, 3), (-1, -1)], False],
    [[(1, 1), (-1, -1)], False]
]


for i, test in enumerate(test_cases):
    res = checkIfVerticalLineExists(test[0])
    assert res == test[1], AssertionError(f'Test {i} was not passed!')
    print(f'Test {i} passed')
