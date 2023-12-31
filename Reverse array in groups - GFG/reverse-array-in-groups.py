#User function template for Python

class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, a, n, k):
        for i in range(0,n,k):
            start = i
            end = min(n-1,i+k-1)
        
            while start <= end:
                temp = a[start]
                a[start] = a[end]
                a[end] = temp
                start += 1
                end -= 1
        return a

	        


#{ 
 # Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends