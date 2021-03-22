#!/usr/bin/env Python3

#DATA

roboX  = 5
roboY  = 5
charge = 100 #percents





#Field parameters

height  = int( input( "Insert the height of field: " ))
width   = int( input( "Insert the width of field: " ))







# ############# DRAWING THE MAP #######################

##################### Y loop #####################
y = 1
while y <= width:

    ##################### X loop #####################
    x = 1
    while x <= height:

        if roboX == x and roboY == y:
            print("R ", end="")
        else:
            print("- ", end="")    

        x += 1
    ##################### X loop #####################

    print()    
    y += 1
##################### Y loop #####################

# #################### CONTROLS #####################

direction = input( "dir ( w/s/a/d/x ) > " )

if( direction == "w" ):
 roboY += 1
 charge -= 5

if( direction == "s" ):
 roboY -= 1
 charge -= 5

if( direction == "a" ):
 roboX -= 1
 charge -= 5

if( direction == "d" ):
 roboX += 1
 charge -= 5

if( direction == "x" ):
 system( "clear" )
 print( "Thank you for playing!" )
# break





