# Naive

def maxCommonSubstring(s1, s2):
    #Counters
    max_len = 0
    endIndex= len(s1)
    # Zero matrix
    m = [[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]

    # Matrix filling

    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                m[i][j] = m[i-1][j-1] + 1

                # Если текущая последовательность больше этой длины
                if m[i][j] > max_len:
                    # Обновить максимальную длину
                    max_len = m[i][j]
                    # Обновить конечный индекс
                    endIndex = i

    return s1[endIndex - max_len:endIndex]


def maxCommonSubstringNaive(s1, s2, n, m):

    if n == 0 and m == 0:
        return 0

    elif s1[n-1] == s2[m-1]:
        return 1 + maxCommonSubstringNaive(s1, s2, n-1, m-1)

    else:
        return max(maxCommonSubstringNaive(s1, s2, n-1, m), maxCommonSubstringNaive(s1, s2, n, m-1))


tests = [
        [['ABRAKADABRA', 'BRAND'], 'BRA'],
        [['mother', 'father'], 'ther'],
        #[['',''], ''],
    ]

for t in tests:
    res = maxCommonSubstring(t[0][0], t[0][1])
    assert t[1] == res, AssertionError(t[0],res)

print('All tests passed')