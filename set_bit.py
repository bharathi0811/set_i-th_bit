a =int(input())
b= int(input())
l=[0]
if a >=b:
    l=l*(a+1)
else:
    l=l*(b+1)
l[a]=1
l[b]=1
l=l[::-1]
sum_=0
for j in range(len(l)):
    sum_+= l[-(j+1)]* (2**j)
print(sum_)