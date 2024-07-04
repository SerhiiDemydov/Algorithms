# -------------- Kейс з коробками та ключем --------------
# Перший підхід
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print 'found the key!'


# Альтернативний підхід з рекурсією
def look_for_key_recursion(box):
    for item in box:
        if item.is_a_box():
            look_for_key_recursion(item) #<----------- Рекурсія
        elif item.is_a_key():
            print 'found the key!'


# -------------- Kейс з базовим та рекурсивним випадко --------------
# Зворотній відлік з рекурсією (Проблема - бескінечно виконується)
def countDown(i):
    print(i)
    countDown(i-1)

# Зворотній відлік з рекурсією (Проблема - бескінечно виконується)
def countDownСorrect(i):
    print(i)
    if i < 1: # <------------ Базовий випадок (коли функція не викликає саму себе, що не зациклитися)
        return
    else:
        countDown(i-1) # <---------- Рекурсивний випадок



# -------------- Стек --------------
def greet(name):
    print "hello ," + name + "!"
    greet2(name)
    print "getting ready to say bye..."
    bye()

def greet2(name):
    print "how are you, " + name + "?"

def bye():
    print "ok, bye"


# -------------- Стек викликів із рекурсивною функцією --------------
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

