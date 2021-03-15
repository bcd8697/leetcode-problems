# На вход функции передается массив целых чисел, на выходе функции нужно вернуть этот же массив, чтобы все значения 0 были в конце (с правой стороны) массива
# a = [int1, int2, 0, int3, 0, int4] - > [int1, int2, int3, int4, 0, 0 ]

def solution(a):

	zeros_idx = []
  
  for idx, i in enumerate(a):
  	
    if i == 0:
    	zeros_idx.append(idx)
    
    elif:
    	continue
      
  # zeros_idx = [2, 3, 5]
  
  for idx, i in enumerate(zeros_idx):
    # (0,2), (1,3), (2,5)
  	zeros_idx[idx] -= idx
  
  # zeros_idx = [2, 2, 3]
    
  for i in zeros_idx:
  	a.pop(i)
    
  for i in range(len(zeros_idx)):
    a.append(0)
  
  return a
