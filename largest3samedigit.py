class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # List of all same 3-digit numbers (000, 111, ..., 999)
        candidates = [num[i:i+3] for i in range(len(num) - 2) if num[i] == num[i+1] == num[i+2]]
        
        # Return the largest 3-digit number found, or an empty string if none
        return max(candidates) if candidates else ""
        
