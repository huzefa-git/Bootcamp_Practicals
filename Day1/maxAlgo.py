arr=[1,5,2,7,3,9,8]
m1=0
m2=0
m3=0
for i in range(len(arr)):
    if(arr[i]>m3):
        m3=i
    if m2<m3:
        m2,m3 = m3,m2
        