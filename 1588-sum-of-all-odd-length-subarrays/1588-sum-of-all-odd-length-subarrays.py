class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total_subarray = 0
        p = [0]
        for num in range(n):
            p.append(p[-1]+arr[num])
            
        for i in range(n):
            sum_sub = 0
            for j in range(i,n,2):
                sum_sub = p[j+1] - p[i]
                total_subarray += sum_sub
        return total_subarray
        