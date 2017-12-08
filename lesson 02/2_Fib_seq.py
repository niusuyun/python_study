'''
斐波那契数列是两个1构成，从第三项开始，每一项是由前面两项的和构成，
如下：1，1，2，3，5... 请通过编程得到数列的前100项，并输出99项与100项的比值。
'''
i, j, ind = 1, 1, 1
print('第i项   斐波那契数列')
print(ind,'     ',i)
ind = 2
print(ind,'     ',j)
while True:
    l = i + j
    ind += 1
    
    print(ind,'     ',l)
    if ind == 100:
        print('99项与100项的比值是')
        print(j/l)
        break
    i = j;
    j = l;
