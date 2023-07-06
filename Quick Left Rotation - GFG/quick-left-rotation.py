class Solution:
    def leftRotate(self, arr, k, n):
        k = k % n
        temp = [0]*k
        
        for i in range(0,k):
            temp[i] = arr[i]
        for i in range(k,n):
            arr[i-k] = arr[i]
        for i in range(n-k,n):
            arr[i] = temp[i-(n-k)]        

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