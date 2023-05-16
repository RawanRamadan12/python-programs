a=[4,5,3,4,3]

min1=a[0]
for i in range (0,len(a)):
    if a[i]<min1:
       min1=a[i]
    
print(min1)
area1=min1*len(a)
print(area1)
area2=0
b=[]
for j in range (0,len(a)):
    n=a[j]-min1
    b.append(n)
print(b)

le=len(b)
c=[]
d=[]
a=0
area_max=0
le=len(b)
c=[]
d=[]
le1=len(c)
a=0
y=0
index=0
n=0
o=0
min1=0

for a in range(0,len(b)):
    if b[a]==0:
         c.clear
         index=0
    elif b[a]!=0:
        c.append(b[a])
        print(c)
    for o in range(0,len(c)):
        min1=min(c)
        min1*le1
        if min1*le1>area_max:
         area_max=min1*le1
        print(area_max)
    le1=le1-1
  
print(c)
print(area_max)
    
"""
for a in range (0,le):
    if b[a]!=0:
        c.append(b[a])
    
print(c)
"""
"""
l=len(b)-1
area3=0
for n in range (0,l):
    if b[n]*l>area3:
        area3=b[n]*l
    l=l-1    
    
print(area3)   

for i in range(n-1):
        if a[i] < m1 :
            m1 = a[i]
        m2 = 2**32
        for j in range(i+1,n):
            if [j] < m2:
                m2 = a[j]
        if c<(m1*(i+1) + m2*(n-i-1)):
            c = (m1*(i+1) + m2*(n-i-1))
    print(c)



"""
"""

"""
  
"""
    if b[a]*le>area2:
        area2=b[a]*le
        
    le=le-1
print(area2)        




print(area1+area2)

"""












    
    
    


