#Дана последовательность положительных чисел длиной N и число Х
#Нужно найти два различных числа А и В
#из последовательности, таких что А + B = X
#или вернуть пару 0, 0, если такой пары чисел нет


# O (n^2)


def findTwoSum(l, x):
    for i in range(0, len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == x:
                return l[i], l[j]
    return 0, 0


# O (n)

def findTwoSum(l, x):
    s = set()

    for num in l:
        if x - num in s:
            return num, x-num
        s.add(num)

    return 0, 0 