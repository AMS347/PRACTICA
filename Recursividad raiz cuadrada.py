def RaizCuadrada(x,n):
    if n==1:
        return x/2
    else:
        return 0.5 * (RaizCuadrada(x,n-1) + x/RaizCuadrada(x,n-1))

print(RaizCuadrada(16,5))