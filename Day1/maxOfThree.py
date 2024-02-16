# arr = [1,5,2,3,7,9,8]
# arr.sort()
# n=len(arr)
# # print(arr[-1],arr[-2],arr[-3])
# for i in range(n-1,n-4,-1):
#     print(arr[i],end=" ")

l=[1,5,2,3,7,9,8]
fL=0
for i in l:
    if(fL<i):
        fL=i
print(fL,end=" ")
sL=0
for i in l:
    if(i>sL and i<fL):
        sL=i
print(sL,end=" ")
tL=0
for i in l:
    if(i>tL and i<fL and i<sL):
        tL=i
print(tL,end=" ")
    

