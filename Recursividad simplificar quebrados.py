def SimplificarQuebrado(n,d):
    if n==0 or d==0:
        return -1
    if n==1 or d==1:
        return 0
    if n==d:
        return 1
    else:
        if d%2==0 and n%2==0:
            return SimplificarQuebrado(n//2,d//2)+1
        if d%3==0 and n%3==0:
            return SimplificarQuebrado(n//3,d//3)+1
        if d%5==0 and n%5==0:
            return SimplificarQuebrado(n//5,d//5)+1
        if d%7==0 and n%7==0:
            return SimplificarQuebrado(n//7,d//7)+1
        else:
            return SimplificarQuebrado(n//d,d//n)+1

print(SimplificarQuebrado(18,60))
