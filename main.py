print("Bienvenido al programa para calcular numero primos")
n = int(input('Ingrese un numero \n'))
primos = []
criba = list(range(2,n+1))


while criba!=[]: #while len(criba)!=0
    m = min(criba)
    primos.append(m)
    for i in range(m,n+1,m):
        if i in criba:
            criba.remove(i)
print(primos)
