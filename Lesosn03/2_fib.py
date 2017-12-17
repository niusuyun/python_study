#作业2：编写一个函数，生成一个斐波那契数列前n项的list

def fib_ls(n,ls=[],a=1,b=0,lev=1):
    ls.append(a+b)
    if lev==n:return ls
    a,b = b,a+b
    return fib_ls(n,ls,a,b,lev+1)

print(fib_ls(5))
    
 
