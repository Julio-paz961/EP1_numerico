
def verifica_raiz_poli(intervalo,passo):
    lista_x=[]
    lista_y=[]
    passo=passo
    for i in range(2*(intervalo[1]-intervalo[0])+1):
        x=i/2
        y=x**3-9*x+5
        lista_x.append(x)
        lista_y.append(y)
        if lista_y[i-1]*lista_y[i]<0:
            return lista_x[i-1],lista_y[i-1],lista_x[i],lista_y[i]

print(verifica_raiz_poli([0,3],0.5))
        
def metodo_biss(intervalo,precisao,passo):
    x=(intervalo[1]-intervalo[0])/2
    y=x**3-9*x+5
    if abs(y)<abs(precisao):
        return y
    else:
        if type(verifica_raiz_poli(intervalo,passo))!=int:
            xo,yo,x,yx=verifica_raiz_poli(intervalo,passo)
            metodo_biss([xo,x],precisao,passo)

print(metodo_biss([0,3],0.01,0.5))

