# si no le pongo que sume un numero a n, el ciclo se va a repetir infinitamente porque no tiene un numero para sumar 
n = 1
#no llega a 10 porque el ciclo se va a repetir hasta que n sea menor que 10
while n < 10:
    print(n)
#el mas igual espara incrementar el valor de n, es decir, n = n + 1, pero con el mas igual se puede escribir de una forma mas corta, que es n += 1
    n += 1
n = 1
while n <= 10:
    print(n)
    n += 1

n = 0
for n in range (0, 10):
    print(n)
