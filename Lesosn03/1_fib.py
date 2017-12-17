#作业1：编写一个函数，用递归的方法输出斐波那契额数列第n项

def fib(lim,a=1,b=0,lev=1):
    if lev == lim:return a+b
    return fib(lim,b,a+b,lev+1)



n=10
print(n,fib(n))
