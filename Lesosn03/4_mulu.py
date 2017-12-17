#作业4：编写一个函数，输出某个目录下面的文件层级

import os

path = 'root'
print(path,':')
for file in os.listdir(path):
    print('--'*1,file)
