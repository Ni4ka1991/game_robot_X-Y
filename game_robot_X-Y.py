#!/usr/bin/env Python3

roboX = 5
roboY = 5

##################### Y loop #####################
y = 1
while y <= 10:

    ##################### X loop #####################
    x = 1
    while x <= 10:

        if roboX == x and roboY == y:
            print("R ", end="")
        else:
            print("- ", end="")    

        x += 1
    ##################### X loop #####################

    print()    
    y += 1
##################### Y loop #####################
