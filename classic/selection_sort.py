def findSmallest(arr):
    """
    Находим индекс наименьшего элемента из списка
    """

    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selectionSort(arr):
    """
    Составляем список последовательным отбором наибольшего элемента
    """

    newArr = []

    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))  # pop возвращает и удаляет элемент массива по его индексу

    return newArr