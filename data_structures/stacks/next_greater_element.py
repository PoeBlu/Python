# Function to print element and NGE pair for all elements of list
def printNGE(arr):

    for i in range(len(arr)):

        next = next((arr[j] for j in range(i + 1, len(arr)) if arr[i] < arr[j]), -1)
        print(f"{str(arr[i])} -- {str(next)}")


# Driver program to test above function
arr = [11, 13, 21, 3]
printNGE(arr)
