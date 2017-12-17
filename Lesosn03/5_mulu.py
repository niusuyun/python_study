#作业4：编写一个函数，输出某个目录下面的文件层级

#作业4：编写一个函数，输出某个目录下面的文件层级

#作业5：在4基础上，能完整的输出子文件夹以及文件
import os




def listdir(path,lev):  #传入存储的list
    
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):
            print('--'*lev,file,':')
            listdir(file_path,lev+1)
        else:  
            print('--'*lev,file)

path='root'
print(path,':')
listdir(path, 1)
