def spiralorder(matrix,m,n):
    top=0
    left=0
    right=m-1
    bottom=n-1
    while top<=bottom and left<=right:
        #first row
        for i in range(left,right+1):
            print(matrix[top][i],end=" ")
        top+=1
        #right column
        for i in range(left,bottom+1):
            print(matrix[i][right],end=" ")
            #6 9
        right=right-1    
        #8 7
        #bottom row
        if top<=bottom:
            for i in range(right,left-1,-1):
                print(matrix[bottom][i],end=" ")
        bottom=bottom-1
        #print 4 5
        if left<=right:
            for i in range(bottom,top-1,-1):
                print(matrix[i][left],end=" ")
            left=left+1    
#main
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(spiralorder(matrix,3,3))                            
                