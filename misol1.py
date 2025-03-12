from math import sqrt
a, b = map(float, input().split())

arif=(a+b)/2
geo = sqrt(a*b)

if arif>geo:
    print(">")
elif geo>arif:
    print("<")
else:
    print("=")