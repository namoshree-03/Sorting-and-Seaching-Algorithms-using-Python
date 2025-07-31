#binary search 
array = input("Enter a list of numbers separated by spaces: ").split()
array = [int(num) for num in array]
array.sort()
target = int(input("Enter the number to search for: "))
low = 0
high = len(array) - 1
while low <= high:
    mid = (low + high) // 2
    if array[mid] == target:
        print("Number found at index:", mid)
        break
    elif array[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Number not found")