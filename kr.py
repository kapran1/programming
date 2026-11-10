def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
f = fibonacci()
for _ in range(10):
    print(next(f), end = " ")

coun = {}
def count_calls(f):
    def wrap(*args, **kwargs):
        name = f.__name__
        coun[name] = coun.get(name, 0) + 1

        print(f"Функция {name} вызвана. Вызывов: {coun[name]}")
        return f(*args, **kwargs)
    return wrap

@count_calls
def hi():
    print("Hi")

@count_calls
def bye():
    print("Bye")
hi()
hi()
bye()

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    a = arr[len(arr) // 2]
    
    left = [x for x in arr if x < a]
    middle = [x for x in arr if x == a]
    right = [x for x in arr if x > a]
    
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3, 6, 8, 10, 1, 2, 1]))
