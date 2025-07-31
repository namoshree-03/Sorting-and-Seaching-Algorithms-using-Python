#bubble sort
array = input("Enter a list of numbers separated by spaces: ").split()
array = [int(num) for num in array]
n = len(array)
for i in range(n):
    for j in range(0, n-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
print("Sorted array:", array)