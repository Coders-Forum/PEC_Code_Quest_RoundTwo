def diagonalDifference(arr):
    left=0
    right=0
    for i in range(n):
        left+=arr[i][i]
    k=0
    for i in range(n-1,-1,-1):
        right+=arr[k][i]
        k+=1
   
    return(abs(left-right))
