import math 
import numpy as np

def cria_A_tridiagonal(n):
    diag_prin=[]
    diag_sec_sup=[]
    diag_sec_inf=[]
    lado_direito=[]
    for i in range(n):
        if 1<=i<=n-1:
            ai=(2*i-1)/4*i
            diag_sec_inf.append(ai)
            diag_sec_sup.append(1-ai)
            diag_prin.append(2)
        elif i==n:
            ai=(2*i-1)/2*i
            diag_sec_inf.append(ai)
            diag_sec_sup.append(1-ai)
            diag_prin.append(2)
            print(math.cos((np.pi())))
        lado_direito.append(math.cos((2*np.pi)/n/n))
    return diag_prin,diag_sec_sup,diag_sec_inf,lado_direito


        
def escalona(A):
    B=A
    tamanho_a=len(A)
    for i in range (tamanho_a-1):
        for j in range(tamanho_a-1):
            pivo=A[i][i]
            vl=A[j][i]
            
        


matriz=[[3,2,4,1],[1,1,2,2],[4,3,-2,3],[1,2,3,4]]

print(escalona(matriz))