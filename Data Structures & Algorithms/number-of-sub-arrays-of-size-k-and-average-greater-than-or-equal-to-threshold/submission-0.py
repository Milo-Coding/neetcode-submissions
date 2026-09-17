class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        for i in range(len(arr)-k+1):
            sub_arr = arr[i:i+k]
            if sum(sub_arr)/k >= threshold:
                count += 1
        return count