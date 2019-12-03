import math
def heron(a,b,c):
    pole=-1
    p=(a+b+c)/2
    if(p-a>0 and p-b>0 and p-c>0):
        pole=math.sqrt(p*(p-a)*(p-b) * (p-c))
    return pole


print(heron(3,4,5))
