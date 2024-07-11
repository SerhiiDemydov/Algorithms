# Сума всіх чисел у масиві
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

#print(sum([1,2,3,4]))

# З рекурсією
def sumRecurs(arr):
    if arr:
        total = arr.pop(0) + sumRecurs(arr)
        return total
    return 0

print(sumRecurs([1,2,3,4]))

# Швидке сортування
def quicksort(array):
    if len(array) < 2:
        return array # <----------- Базовий випадок: масив з 0 або 1 елементу уже "відсортовані"
    else:
        pivot = array[0] # <----------- Рекурсивний випадок
        less = [i for i in array[1:] if i <= pivot] # <----------- Підмасив усіх елементів, менших за опорний елемент
        greater = [i for i in array[1:] if i > pivot] # <----------- Підмасив усіх елементів, більших за опорний елемент
    return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))


# ------- Сортування злиттям проти швидкого -------

def print_items(list):
    for item in list:
        print(item)
        # Час виконання О(n)


# Додаємо 1с затримки, перш ніж надрукувати елемент
from time import sleep
def print_items2(list):
    for item in list:
        sleep(1)
        print(item)
        # Час виконання також О(n), так як виконуэться петля один раз через список
        # O(n)=c*n. C - це певний фіксований проміжок часу, за певну кількість яких і буде виконано алгоритм
        # Тому print_items1 буде швидший

