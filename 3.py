from array import*
arr=array('i',[])
n=int(input())
#taking the array input
for i in range(n):
   x=int(input())
   arr.append(x)

# declaring the max area initally 0
max_Area=0 
#implementing the brute force approach
for i in range(1,n-1):
    # initialising the min_left and min_right a big integer we can also 
    # initialse maximum integer available in python
    min_left=1000000000
    min_right=1000000000
    # count_left is the left window or left partition size
    # count_right is the right window or right partition size
    count_left=i
    count_right=n-(i)
    # calculating the min_left 
    for j in range(0,i):
       if(arr[j]<min_left):
            min_left=arr[j]
            print(min_left)
    # calculating the min_right        
    for j in range(i,n):
       if(arr[j]<min_right):
            min_right=arr[j]
            print("--------")
            print(min_right)
    #after calculating the min_right and min_left
    # The Total area obtained is the sum of  area formed by the left and right part
    print(min_left)
    print(min_right)
    print(count_left)
    print(min_right)
    total_area=(min_left*count_left)+(min_right*count_right)
    # if the total_area here is greater than the max_Area so far then we update our max_Area answer
    if(max_Area<total_area):
        max_Area=total_area
#print("The max_Area is :")
print(max_Area)
