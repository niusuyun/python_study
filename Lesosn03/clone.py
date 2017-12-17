f = open('name.txt')
ls = f.readlines()
f.close()

def clone(path):
#    i=i[:-1]
#    print(i)
    name=path.split('/')[-2]
    os.mkdir(name)
    os.system('git clone %s %s'%(path+'.git',name))

for i in ls:
    i=i[:-1]
    clone(i)
