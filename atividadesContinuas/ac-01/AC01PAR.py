#AC LP2
#Tiago Beneteli Ultramari de Lima - 2D noturno
#RA: 1800804

#ex2
def letras(a, b, c):
    if a == b and a == c and b == c:
        return "São guais"
    else:
        return "São diferentes"

letras("a","a","b")
#####################################################
#ex4
def ConsoVogal(letra):
    letr = letra.lower()
    if letr == "a" or letr == "e" or letr == "i" or letr == "o" or letr == "u":
        return 1
    else:
        return 0
    
ConsoVogal("ç")
#####################################################
#ex6
def RetornoLista(lista):
    lista2 = []
    y = 0
    for x in range(len(lista)-1,-1, -1):        
        lista2.insert(y, lista[x])
        y = y +1
    return lista2

lista = [1,2,3,4,5,450,1000,4,1,5,20,50]
RetornoLista(lista)

######################################################
#ex8
def LasttLista(lista):
    listaFinal = []
    y = 0
    j = False
    while j != True:
        j=True
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                j = False
    return lista
         
lista = [1,1000,3,4,20,450,4,1,5,2000,2,6,9]
LasttLista(lista)
#########################################################
#ex10
def OttherLista(lista1, lista2):
    outraLista = []
    for x in range(len(lista1)):
        num = lista1[x] * lista2[2]
        outraLista.insert(x , num)
    return outraLista

lista1 = [1,2,3,4,5,30]
lista2 = [2,2,2,2,2,2]
OttherLista(lista1,lista2)
