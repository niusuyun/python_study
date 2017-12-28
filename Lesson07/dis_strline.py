import numpy as np

'''A=[1,0,0]
B=[0,1,0]
C=[1,0,1]
D=[0,0,0]

'''
def dis_str_line(A,B,C,D):
    A,B,C,D,K = np.mat(A),np.mat(B),np.mat(C),np.mat(D),np.mat([0,0,1])
    n=np.vstack((B-A,D-C,K))
    N=n.I*np.mat([0,0,1]).T
    print(np.abs(np.max((C-A)*N)/np.sqrt(np.sum(np.square(N)))))


A=[0,1,0]
B=[0,0,0]
C=[1,2,3]
D=[9,9,9]

dis_str_line(A,B,C,D)
