'''
Given k sorted arrays of size n each, merge them and print the sorted output.

Example: 

Input: 
k = 3, n = 4 
arr[][] = { {1, 3, 5, 7}, 
{2, 4, 6, 8}, 
{0, 9, 10, 11}} ;
Output: 0 1 2 3 4 5 6 7 8 9 10 11 
Explanation: The output array is a sorted array that contains all the elements of the input matrix. 

Input: 
k = 4, n = 4 
arr[][] = { {1, 5, 6, 8}, 
{2, 4, 10, 12}, 
{3, 7, 9, 11}, 
{13, 14, 15, 16}} ;
Output: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
Explanation: The output array is a sorted array that contains all the elements of the input matrix. 

'''



def merge_k_sorted_arrays(k, n, arr):
  res = []
  for i in range(k):
    res += arr[i]
  
  return sorted(res)
