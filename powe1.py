class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n == 0:
                return 1

            if n%2 != 0:
                y = self.myPow(x,(n-1)/2)
                return x*y*y
            else:
                y = self.myPow(x,n/2)
                return y*y
        if n < 0:
            x = 1/x
            n = abs(n)
        return helper(x,n)
