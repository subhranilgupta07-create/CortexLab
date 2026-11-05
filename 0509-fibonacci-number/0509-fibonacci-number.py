class Solution(object):
    def fib(self, n):
        def Fibo (n):
            if (n <= 1):
                return n
            return Fibo(n - 1) + Fibo(n - 2)
        return Fibo(n)        