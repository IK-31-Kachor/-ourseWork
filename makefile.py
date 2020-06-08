import random

items = [random.randint(0, 99) for i in range(400)]
for i in range(0, len(items)):
    items[i] = str(items[i])
numbers =  ' '.join(items)
handle = open("numbers.txt", "w")
handle.write(numbers)
handle.close()
input("file created: numbers.txt>>>>>>")
input()
