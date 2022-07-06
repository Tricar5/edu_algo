def countSort(seq):
    min_val = min(seq)
    max_val = max(seq)

    # интервал изменения чисел
    k = max_val - min_val + 1

    # cоздаем список подходящего размера
    count = [0] * k
    # обновляем счетчики для элементов
    for now in seq:
        count[now-min_val] += 1

    nowpos = 0
    for val in range(0, k):
        for i in range(count[val]):
            # по индексу заменяем
             seq[nowpos] = val + min_val
             nowpos += 1



l_0 = [3,3,5,4,2,1,1,6,9, 8]

countSort(l_0)

print(l_0)
