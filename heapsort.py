from datetime import datetime
import time
import random


counter_compare = 0
counter_replace = 0


server_file = "numbers.txt"

handle = open(server_file, "r")
heap_array = handle.read()
handle.close()
print("File open:",heap_array)
heap_array = heap_array.split(' ')
print('Array before sort:', heap_array)

index_start_R = 0
index_stop_R = len(heap_array) - 1

start_time = datetime.now()
s = ''' '''


def heapify(nums, heap_size, root_index):  
    # Індекс найбільшого елемента вважаємо кореневих індексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Якщо лівий нащадок кореня - допустимий індекс, а елемент більше ніж поточний найбільший, оновлюємо найбільший елемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # Те ж саме для правого нащадка кореня
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # Якщо найбільший елемент більше не кореневої, вони міняються місцями
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)

def heap_sort(nums):  
    n = len(nums)

    # Створюємо Max Heap зі списку
    # Другий аргумент означає зупинку алгоритму перед елементом -1, тобто перед першим елементом списку
    # 3-й аргумент означає повторний прохід по списку у зворотному напрямку, зменшуючи лічильник i на 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Переміщаємо корінь Max Heap в кінець списку
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

# Перевіряємо, що воно працює
input("Press enter to Heap sort:")
list_of_nums = heap_array                                                        #[35, 12, 43, 8, 51,23,56,123,5,212,54,123,233,41,34,2,32,1,10,3,5,124,788,54,32432,32,123,54,23,34]  
heap_sort(list_of_nums)  


print('Array after sort:', heap_array )
print("Compare:",counter_compare)
print("Replace:", counter_replace)
print(" Lenght:", len(heap_array))
for i in range(0, len(heap_array)):
    heap_array[i] = str(heap_array[i])
result =  ' '.join(heap_array)
handle = open("result.txt", "w")
handle.write(result)
handle.close()
print("Файл :result.txt з відсортованими числами cтворено.")
print(datetime.now() - start_time)

input("Press enter to exit")


