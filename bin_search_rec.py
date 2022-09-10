def bin_search_rec(arr,key,low,high):
    if high>=low:
        mid=low+(high-low)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            return bin_search_rec(arr,key,low,mid-1)
        else:
            return bin_search_rec(arr,key,mid+1,high)
    else:
        print("element not found")
        return
    
arr=[1,2,3,4,5,6,7,8,9]
indx=bin_search_rec(arr,7,0,len(arr))
print(indx)