def binarySearch(list, target):
    first = 0
    last = len(list) -1

    while first <= last:
        midpoint = (first + last)//2
        
        if list[midpoint]== target:
            return midpoint 
        elif list[midpoint] < target:
            first = midpoint +1
        else:
            last = midpoint - 1
    return None

def verify(index):
    if index != None:
        print("target is at the:", index)
    else:
        print("target was not found in the list")
    
numbers = [1,2,3,4,5,6,7,8,9,10]
result = binarySearch(numbers, 9)
verify(result)