#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		largest = arr[0]
        second_largest = -1
        
        for i in range(len(arr)):
            
            if arr[i] > largest:
                second_largest = largest
                largest = arr[i]
            elif arr[i] != largest and arr[i] > second_largest:
                second_largest = arr[i]
                
                
            
        return second_largest


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends