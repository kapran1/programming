number = (1,2,3,4,5)

num = int(input("Введите число: "))

new_number = tuple(x for x in number if x != num)

print(new_number)