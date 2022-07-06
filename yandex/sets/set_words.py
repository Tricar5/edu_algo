#Дан словарь из N слов, длина каждого не превосходит К
#В записи каждого из М слов текста (каждое длиной до К)
#может быть пропущена одна буква. Для каждого слова
#сказать, входит ли оно (возможно, с одной пропущенной
#буквой), в словарь




#Решение за O(NK + M)
#Выбросим из каждого слова словаря по одной букве всеми возможными способами за O(NK) и положим получившиеся слова в множества
#Для каждого слова из текста просто проверим, есть ли оно в словаре за O(1)

def getwordindict(dictionary, text):
    goodwords = set(dictionary)

    for word in dictionary:
        for delpos in range(len(word)):
            goodwords.add(word[:delpos] + word[delpos+1:])

    ans = []

    for word in text:
        ans.append(word in goodwords)

    return ans