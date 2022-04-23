import math 
import numpy as np
import math

def transpoe_matriz_1D(lista):
    a = lista
    b = np.array(a)
    c = np.array([a])
    return c.T

def gera_matriz_cic(n):
    a=[]
    b=[]
    c=[]
    d=[]
    M=[]
    for i in range(1,n+1,1):
        if i!=n:
            a.append((2*i-1)/(4*i))
            c.append(1-a[i-1])
            b.append(2)
            d.append(math.cos((2*math.pi*(i**2))/((n)**2)))
        else:
            a.append(((2*(n)-1)/(4*i)))
            c.append(1-a[i-1])
            b.append(2)
            d.append(math.cos((2*math.pi*(i**2))/((n)**2)))
    M.append(a)
    M.append(b)
    M.append(c)
    return M,d


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
    d=d

    l=np.zeros(n)
    y=np.zeros(n)
    x=np.zeros(n)
    
    l[0]=c[0]/b[0]
    for i in np.arange(1,n-1,1):  
       l[i]=c[i]/(b[i]-a[i]*l[i-1])  
 
    y[0]=d[0]/b[0]  
    for i in np.arange(1,n,1):  
       y[i]=(d[i]-a[i]*y[i-1])/(b[i]-a[i]*l[i-1])  
 
    #faz substituicao reversa para obter a solucao x  
    x[n-1]=y[n-1]  
    for i in np.arange(n-2,-1,-1):  
       x[i]=y[i]-l[i]*x[i+1]  

    return l,y,x


def decomposicao_LU_tri_cic(n,A,d):
    n=n-1
    a=A[0]
    b=A[1]
    c=A[2]
    a_sub=[0]
    b_sub=[]
    c_sub=[]
    for i in range(n-1):
        a_sub.append(a[i])
        b_sub.append(b[i])
        c_sub.append(c[i])
    b_sub.append(b[n])
    c_sub.append(0)

    Tn=[a_sub,b_sub,c_sub]
    Sol_Tn=np.copy(d[:(len(d)-1)])
    v=np.zeros(n,dtype=float)
    w=np.zeros(n,dtype=float)
    v[0]=a[n]
    v[n-1]=c[n-1]
    w[0]=c[n]
    w[n-1]=a[n-1]

    y_barra=decomposicao_LU_tri(n,Tn,Sol_Tn)[2]
    z_barra=decomposicao_LU_tri(n,Tn,v)[2]
    xn=(d[n]-w[0]*y_barra[0]-w[n-1]*y_barra[n-1])/(b[n]-w[0]*z_barra[0]-w[n-1]*z_barra[n-1])
    x_barra=y_barra-xn*z_barra
    
    return np.append(x_barra,xn)


D=gera_matriz_cic(5)
print(D[0])
print(D[1])
x=decomposicao_LU_tri_cic(len(D[0][0]),D[0],D[1])
print("x: "+str(x))

