import math 
import numpy as np

def decomposicao_LU(A):
    A=np.array(A)
    n=len(A)
    L=np.identity(n,dtype=float)
    U=np.identity(n,dtype=float)
    
    for i in range (n):
        Uii=U[i][i]
        if i==0:
           U[i, i : n] = A[i, i : n]
           L[(i + 1) : n, i] =A[(i + 1) : n, i] /Uii

        if i==(n-1):       
            U[i, i : n] = A[i, i : n] - np.dot( L[i, 1 : (i - 1)], U[1 : (i - 1), i : n])  
            ##print(U)
            ##print('U2')
            
        else:
            U[i, i : n] = A[i, i : n] - np.dot( L[i, 1 : (i - 1)], U[1 : (i - 1), i : n])  
            L[(i + 1) : n, i] = (A[(i + 1) : n, i] - np.dot(L[(i + 1) : n, 1 : (i - 1)] , U[1 : (i - 1), i]))/Uii
            ##print(U)
            ##print('U3')
    return A,L,U

def matriz_tri(A):
    A=np.array(A)
    n=len(A)
    a=[0]
    b=[]
    c=[]
    D=[]
    for i in range (n):
        b.append(A[i,i])
        
        if i!=0:
            a.append(A[i,i-1])
        if i!=n-1:
            c.append(A[i,i+1])
        if i==n-1:
            c.append(0)
    D.append(a)
    D.append(b)
    D.append(c)
    return D

def decomposicao_LU_tri(n,A,d):
    a=A[0]
    b=A[1]
    c=A[2]
    l=np.zeros(n)
    u=np.zeros(n)
    y=np.zeros(n)
    x=np.zeros(n)
    u[0]=c[0]/b[0]
    y[0]=d[0]/b[0]

    for i in range (1,n,1):
        #print("i:"+str(i))
        l[i]=a[i]/u[i-1]
        #print("li"+str(i)+":"+str(li))
        u[i]=b[i]-l[i]*c[i-1]
        #print("ui"+str(i)+":"+str(ui))
        y[i]=d[i]-l[i]*c[i-1]
    x[n-1]=(y[n-1])/(u[n-1])
    for i in range(n-2,-1,-1):
        x[i]=(y[i]-c[i]*x[i+1])/u[i]


    return l,u,y,x


matriz=[[5,4,0,0,0,0],[1,3,1,0,0,0],[0,2,4,1,0,0],[0,0,1,2,1,0],[0,0,0,2,3,2],[0,0,0,0,1,2]]
solução=[13,10,20,16,35,17]
print("A: ","\n", str(np.array(matriz)))
D=matriz_tri(matriz)
print("a: "+str(D[0]))
print("b: "+str(D[1]))
print("c: "+str(D[2]))
print("d: "+str(solução))
L,U,y,x=decomposicao_LU_tri(len(matriz),D,solução)
print("L: "+str(L))
print("U: "+str(U))
print("y: "+str(y))
print("x: "+str(x))
