class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def koko(k: int)-> bool:
            max_h=0
            for pile in piles :
                hours_for_pile = (pile + k - 1) // k
                max_h= hours_for_pile+max_h

            if max_h <= h:
                return True
            else :
                return False
            return False
    
        min_k= 1
        max_k=max(piles)
        while min_k < max_k :
            mid_k = (min_k + max_k) // 2
            if koko(mid_k) :
                max_k = mid_k
            else :
                min_k=mid_k + 1
        return min_k

