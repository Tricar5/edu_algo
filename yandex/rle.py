def rle(s):
    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s

    lastsym = s[0]
    lastpos = 0
    ans = []

    for i in range(len(s)):
        if s[i] != lastsym:
            ans.append(pack(lastsym, i-lastpos))
            lastpos = i
            lastsym = s[i]

    ans.append(pack(s[lastpos], len(s) - lastpos))
    return ''.join(ans)


s= 'AAAABBBX333333YZZAAAAB'
print(s)
s_coded = rle(s)

print(s_coded)

d = {}

decoded = []


i = 0
while i < len(s_coded)-1:

    if s_coded[i+1].isdigit() and i != len(s_coded) - 1:
        decoded.append(s_coded[i] * int(s_coded[i + 1]))
        i += 2

    else:
        decoded.append(s_coded[i])
        i += 1
print(''.join(decoded))