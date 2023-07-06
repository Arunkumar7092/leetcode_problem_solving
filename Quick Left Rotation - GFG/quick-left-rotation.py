class Solution:
    

    def leftRotate(self, arr, k, n):
        k = k % n 
        arr[0:k] =reversed(arr[0:k])
        arr[k:n] = reversed(arr[k:n])
        arr[0:n] = reversed(arr[0:n])
        
        
       

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a = list(map(int,input().split()))
        ob = Solution()
        ob.leftRotate(a,k,n)
        print(*a)
# } Driver Code Ends