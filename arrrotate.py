def lef(arr,d,n):  #1
    for i in range(d): #n
        lefone(arr,n) #1
def lefone(arr,n):  #1
    temp=arr[0]     #1
    for i in range(n-1): #n
        arr[i]=arr[i+1] #1
    arr[n-1]=temp #1
def disp(arr,size): #1
    for i in range(size): #n
        print("% d"%arr[i],end="")
arr=[int(i) for i in range(1,8)] #1
lef(arr,3,7) #1
print(arr) #1
