
def findMaxSymbol(s):

    ans = ''
    ans_cnt = 0
    symbols = dict()

    for now in s:
        if now not in symbols.keys():
            symbols[now] = 0
        symbols[now] += 1

        if symbols[now] > ans_cnt:
            ans = now
            ans_cnt = symbols[now]

    return ans

tests = [
    ['aab', 'a'],
    ['abaabcbcdb', 'b'],
    ['',''],
    ['error','r']
]

for test in tests:
    assert findMaxSymbol(test[0]) == test[1]