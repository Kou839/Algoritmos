from functools import reduce 



potencia= lambda numero1= 0, exponente2= 0: numero1**exponente2 
print(potencia(4,5)) 
#--------------------------------------------------------------- 

actividad= lambda palabra, x: print(palabra*x) 
palabra= str(input("Escriba una palabra: "))
x_cantidad= int(input("x cantidad: "))
print(actividad(palabra,x_cantidad)) 
#---------------------------------------------------------------
lista_1= [3,4,6,2,6]
lista_2= [4,7,3,9,5]
numero_mayor= lambda lista_1, lista_2: print(max(lista_1), max(lista_2)) 
print(numero_mayor(lista_1, lista_2))

#función map 

lista_map= [8,6,4,2,10]
elevar= lambda valor: valor**2 
n= list(map(elevar, lista_map)) 
print(n) 

lista_map2= [3,8,4,5,1] 
dividir_por_mayor= lambda valor: valor/max(lista_map2) 
x= list(map(dividir_por_mayor, lista_map2)) 
print(x)

lista_map3= [10,19,18,17,16]
z= int(input("Escriba el numero con el que quiere restar")) 
restar= lambda valor, z: print(valor-x) 
y= list(map(restar,lista_map3)) 
print(y) 

#función filter 

