class Memoization(object):
    def __init__(self, f):
        self.f=f
        self.memo={}
    
    def __call__(self, arg):
        if not arg in self.memo:
            self.memo[arg]=self.f(arg)
        return(self.memo[arg])

def fibonacci(k):
    if k==1 :
        return 1
    elif k==0:
        return 0
    else:
        return fibonacci(k-1) + fibonacci(k-2)

class Solution:
    def fib(self, n: int) -> int:
        memo_fibo=Memoization(fibonacci)
        return memo_fibo(n)