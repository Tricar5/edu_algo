def binary_search(array, item):
    """
    Бинарный поиск по предварительно отсортированному массиву.
    Возвращает индекс элемента
    """

    low = 0
    high = len(array) - 1

    while low <= high:

        mid = int((low + high) / 2)  # получаем индекс середины

        guess = array[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1  # урезаем массив вполовину

        else:
            low = mid + 1

    return None


my_list = [1,4,6,8,10,43,45]

binary_search(my_list, 10)