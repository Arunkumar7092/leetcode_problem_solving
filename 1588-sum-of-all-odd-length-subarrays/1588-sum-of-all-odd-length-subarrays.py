class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total_subarray = 0
        for i in range(n):
            sum_sub = 0
            for j in range(i,n,2):
                sum_sub = sum(arr[i:j+1])
                total_subarray += sum_sub
        return total_subarray
        