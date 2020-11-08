from operator import *

a = 10
b = 7
print(a, '+', b, '=', jumlah(a, b))
print(a, '-', b, '=', kurang(a, b))
print(a, '*', b, '=', kali(a, b))
print(a, '/', b, '=', bagi(a, b))


from operator import *

a = 2
b = 4
c = 6
print(a, '+', b, '*', c, '-', b, '=', hasil(a,b,c))

a = 4
b = 7
c = 6
d = 9
print(a, '+', b, '*', c, '-', d, '=', hasil(a, b, c, d))

a = 10
b = 2
c = 7
d = 5
e = 12
f = 34
print(a, '+', b, '/', c, '+', d, '/', e, '-', f, '=', hasil(a, b, c, d, e, f))
