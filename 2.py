
num_element=eval(input('Please enter the number of elements: '))
while num_element<1 or num_element>30:
    print("Please enter numbers from 1 to 30")
    num_element=eval(input('Please enter the number of elements: '))
else:
    print('number of elments in two arrays: ',num_element)
Array_2=[]
    
for array2 in range (0,num_element):
    element_2=eval(input('Enter the element for second array: '))
    Array_2.append(element_2)

e=0
o=num_element-1

for pos in range (0,num_element):
    max_2=max(Array_2)
    if max_2%2==0:
      Array_2.insert(o,max_2)
      o=o-1
      Array_2.remove(max_2)
    else:
      Array_2.insert(e,max_2)
      e=e+1
      Array_2.remove(max_2)


print(Array_2)

"""
#start code
num_element=eval(input('Please enter the number of elements: '))
#make user enter the number of element for two array
while num_element<1 or num_element>30:
    #make user enter number of element between 1 to 30 
    print("Please enter numbers from 1 to 30")
    #print messege if user enter number wrong and enter new number
    num_element=eval(input('Please enter the number of elements: '))
    #make user enter a new number of element for two array
else:
    print('number of elments in two arrays: ',num_element)
    #print the number of elements for two array
num_swap=eval(input('Please enter the number of swaps: '))
#make user enter number of swaps 
while num_swap<0 or num_swap>num_element:
    #make user enter number of swap between 0 to number of element
    print("Please enter numbers from 1 to ",num_element)
    #print messege if user enter number wrong and enter new number
    num_swap=eval(input('Please enter the number of swaps: '))
    #make user enter a new number of swaps
else:
    print('number of Swaps: ',num_swap)
    #print number of swaps
Array_1=[]    #initialized an empty array
Array_2=[]    #initialized an empty array

for array1 in range (0,num_element):
    #make loop to enter the element in first array
    element_1=eval(input('Enter the elements for first array: '))
    #put the element in variable
    Array_1.append(element_1)
    #insert the value in variable in list
    
for array2 in range (0,num_element):
    #make loop to enter the element in second array
    element_2=eval(input('Enter the element for second array: '))
    #put the element in variable
    Array_2.append(element_2)
    #insert the value in variable in list
    
Array_1.sort()
#sort the first array
Array_2.sort()
#sort the second array

count1= 0
#make count for first array
count2= num_element-1
#make counter for second array

while num_swap>0:
    #make while loop according number of swaps
    if (Array_1[count1]<Array_2[count2]):
        #make condition to see minimum elemnt and maximum
        Array_1[count1], Array_2[count2] =Array_2[count2], Array_1[count1]
        #swap between maximum value in second array with minimum value in first array
    count1=count1+1
    #increase count by 1
    count2=count2-1
    #decrease counter by 1
    num_swap=num_swap-1
    #decrease number of swap by 1    
sum_array=sum(Array_1)
#get the sum of first array and set on variable
print("the sum of the first array after swapping",sum_array)
#print the sum of first array
#end code
    
"""    
