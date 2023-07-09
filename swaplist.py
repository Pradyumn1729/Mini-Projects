def swap(num):
    size=len(num)
    
    #swapping
    temp=num[0]
    num[0]=num[size-1]
    num[size-1]=temp
    return num

num=[10,20,30,50]
print(swap(num))