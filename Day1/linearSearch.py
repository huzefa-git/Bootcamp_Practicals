arr=[1,2,3,4,10,80]
i=0
for i in arr:
    if(arr[i] > arr[i-1]):
        print(arr[i])
    i+=1
        
