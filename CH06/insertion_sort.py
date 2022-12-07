def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
# insertion : 이전 배열의 값보다 작을 경우 swap
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

if __name__=="__main__":                
    arr = [7,5,9,0,3,1,6,2,4,8]
    insertion_sort(arr)
    print(arr)
