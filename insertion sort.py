#insertion sort
array = input("Enter a list of numbers separated by spaces: ").split()
array = [int(num) for num in array]
n = len(array)
for i in range(1, n):
    key = array[i]
    j = i - 1
    while j >= 0 and key < array[j]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key