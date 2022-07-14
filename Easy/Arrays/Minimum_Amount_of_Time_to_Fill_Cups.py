class Solution:
    def fillCups(self, a: List[int]) -> int:
        total = 0
        a.sort()
        while a[1] :
            a[1] =a[1] - 1
            a[2] =a[2] -1
            total = total +1
            a.sort()
        return(total + a[2])


