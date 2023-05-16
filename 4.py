from turtle import*    #import the package turtle from python library

List_ColorS=['brown','red','magenta','blue','green','orange']   #creat list have colors

Change_ColorS=0      #creat variable to make it the index of list color

penup()            #make the arrow that draw up till go to postion to start draw

goto(0,0)       #set the start postion x=0 ,y=0

pendown()        #make the arrow that draw down that mean the arrow reached postion to draw

bgcolor('white')   #the color of background is white

for r in range (1,37):   #make loop to repeat draw circle 36 time
    
    pencolor(List_ColorS[Change_ColorS])  #change the color of turtle from colors in list
    
    circle(100) #draw circles with radius 100
    
    left(10)  #draw circles from left with angle 10
    
    if (r%6==0): #make if to change color from list using variable as index
        
        Change_ColorS=Change_ColorS+1   #if the condition is true the variable will increase by one to change color
        
        
    

