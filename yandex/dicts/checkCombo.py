#Дано два числа Х и Ү без ведущих нулей
#Необходимо проверить, можно ли получить первое
#из второго перестановкой цифр

def isDigitPermutation(x,y):

    def countDigits(num):
        l = [0 for i in range(10)]
        while num > 0:
            lastdigit = num % 10
            l[lastdigit] += 1
            num = num // 10
        return l

    l_x = countDigits(x)
    l_y = countDigits(y)

    for i in range(10):
        if l_x[i] != l_y[i]:
            return False

    return True