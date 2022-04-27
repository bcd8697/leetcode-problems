'''
Given a sorted array arr of size N, the task is to reduce the array such that each element can appear at most two times.

Examples: 

Input: arr[] = {1, 2, 2, 2, 3} 
Output: {1, 2, 2, 3} 
Explanation: 
Remove 2 once, as it occurs more than 2 times.

Input: arr[] = {3, 3, 3} 
Output: {3, 3} 
Explanation: 
Remove 3 once, as it occurs more than 2 times.  

'''



def removeDuplicates(arr, n = len(arr)) :
 
    # Initialise the 2nd pointer
    checker = 0
 
    # Iterate over the array
    for i in range(n):
 
        if i < n - 2 and arr[i] == arr[i + 1] and arr[i] == arr[i + 2]:
            continue
 
        # Update the 2nd pointer
        else:
            arr[checker] = arr[i]
            checker += 1
 
    return arr[:checker]
