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

def decomposicao_LU_tri(n,A):
    a=A[0]
    b=A[1]
    c=A[2]
    L=[0]
    U=[b[0]]
    for i in range (1,n,1):
        #print("i:"+str(i))
        li=a[i]/U[i-1]
        #print("li"+str(i)+":"+str(li))
        ui=b[i]-li*c[i-1]
        #print("ui"+str(i)+":"+str(ui))
        L.append(li)
        U.append(ui)
    return L,U

def Resolve_Sis(L,d,U,A):
    a=A[0]
    b=A[1]
    c=A[2]
    y=[d[0]/b[0]]
    x=np.zeros(len(L),dtype=float)
    
    for i in range(1,len(L)):
        yi=(d[i]-a[i]*y[i-1])/(b[i]-a[i]*L[i])
        y.append(yi)

    x[len(L)-1]=(y[len(L)-1])
    for i in range(len(L)-2,-1,-1):
        xi=y[i]-L[i+1]*x[i+1]
        x[i]=xi
    x=np.round(x)
    return y,x







matriz=[[2,1,0,0,0],[1,2,1,0,0],[0,1,2,1,0],[0,0,1,2,1],[0,0,0,1,2]]
solução=[4,4,0,0,2]
print("A: ","\n", str(np.array(matriz)))
D=matriz_tri(matriz)
print("D: "+str(D))
L,U=decomposicao_LU_tri(len(matriz),D)
print("L: "+str(L))
print("U: "+str(U))

y,x=Resolve_Sis(L,solução,U,D)
print("y: "+str(y))
print("x: "+str(x))
