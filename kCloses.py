from queue import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        def binarySearch(low,high):            
            while low<=high:
                mid = low + (high-low)//2
                if arr[mid] == x:
                    return mid
                elif arr[mid] > x:
                    high = mid-1
                else:
                    low = mid+1
                    
            return high
        
        idx = binarySearch(0,len(arr)-1)
        left,right = idx,idx+1
        result = deque()
        while len(result) < k:
            a = float("inf")
            b = float("inf")
            if left >= 0:
                a = arr[left]
            if right < len(arr):
                b = arr[right]
            if abs(a-x) <= abs(b-x):
                result.appendleft(a)
                left -= 1
            else:
                result.append(b)
                right += 1
        
        return result
