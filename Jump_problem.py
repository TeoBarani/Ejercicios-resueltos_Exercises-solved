import numpy as np

class Solution:
	def minJumps(arr, n):
		new_jump = arr[0] * 1	
		jumps = 1
		num_passed = new_jump
	    
		while True:
			new_jump = arr[new_jump] * 1
			num_passed += new_jump
			jumps += 1
	        
			if arr[new_jump] == 0:
			    return -1
			
			if num_passed >= n:
				break
		
		return jumps
	

n = 11 
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
arr = np.array(arr)
print(Solution.minJumps(arr, n))