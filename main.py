
# Сортировка пузырьком
def sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

#Двоичный поиск
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle - 1] < element and element <= array[middle]:
        return middle  # возвращаем индекс если в середине
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # или ищем в правой
        return binary_search(array, element, middle + 1, right)

spisok = input("Введите последовательность чисел через пробел: ")
element = int(input("Введите любое число: "))
massiv = list(map(int, spisok.split()))
print(massiv)
massiv_new = sort(massiv)
left, right = massiv_new[0], massiv_new[-1]
print(left)
print(right)

print(massiv_new)

if element < left or element > right:
    print("Нет числа")
else: print(binary_search(massiv_new, element, 0, len(massiv_new) - 1))

