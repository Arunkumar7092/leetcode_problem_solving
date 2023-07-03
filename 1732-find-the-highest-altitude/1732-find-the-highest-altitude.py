class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        p = [0 for _ in range(n+1)]
        ans = p[0]
        for i in range(1,n+1):
            p [i] = p [i -1] + gain[i-1]
            ans = max(ans,p[i])
        return ans
            
            
        