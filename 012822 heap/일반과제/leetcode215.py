class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        return heapq.nlargest(k,nums)[-1]
         # 배열의 n번째 값을 출력하는 함수를 사용하였습니다.g