def bin_search(arr,key):
    n=len(arr)
    low=0
    high=n-1
    while(low<high):
        mid=low+(high-low)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            high=mid-1
        else:
            low=mid+1
    print("element not found")
    return
    
arr=[1,2,3,4,5,6,7,8,9]
indx=bin_search(arr,8)
print(indx)