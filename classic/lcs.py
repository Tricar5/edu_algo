word_a = 'fish'
word_b = 'hish'

cell = [[0 for i in range(len(word_a))] for i in range(len(word_b))]

for i in range(0,len(word_a)):
    for j in range(0,len(word_a)):
        if word_a[i] == word_b[j]:
            # The letters match.
            cell[i][j] = cell[i-1][j-1] + 1
        else:
            # The letters don't match.
            cell[i][j] = max(cell[i-1][j], cell[i][j-1])