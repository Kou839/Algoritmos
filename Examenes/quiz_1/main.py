import fibonachi
import time 

inicio= time.time()
fibonachi.caso1(15)
tiempo_caso1= time.time()-inicio

inicio= time.time()
fibonachi.caso2(15)
tiempo_caso2= time.time()-inicio

if tiempo_caso1 > tiempo_caso2:
    print("El caso 2 es más rapido")
else: 
    print("El caso 1 es más rapido")

