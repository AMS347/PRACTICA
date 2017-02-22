def MultiplicacionEgipcia(p,q):
    if q==0:
        return 0
    if q==1:
        return p
    if q%2==0 and q>=2:
            return MultiplicacionEgipcia((2*p),(q//2))
    else:
            return MultiplicacionEgipcia(2*p,q//2) + p

print(MultiplicacionEgipcia(4,5))