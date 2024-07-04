def binar_search(list: list, item):
    low = 0
    high = len(list) - 1
    iter = 0

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        iter = iter + 1 # кількисть ітерацій

        if guess == item:
            return mid,iter
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None, iter


my_list = list(range(128*2))

my_list = sorted(my_list)
item = 999

print(binar_search(my_list,item))

