import numpy as np

tablero=np.ones(shape=(3,4), dtype=str)
tablero[:]="a"

print(tablero[0][0])
print(tablero)

tab= np.chararray(shape=(9,6), itemsize=5)
tab[:] = 'abc'
print(tab[0,0])
print(tab)
