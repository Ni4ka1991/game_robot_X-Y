#!/usr/bin/env Python3
from os import system

#a - move left
#d - move right
#w - move up
#s - move down



#DATA
 #coordinates


roboX        = 5
roboY        = 5

bomb_1X      = 17
bomb_1Y      = 19

bomb_2X      = 2
bomb_2Y      = 7

money_bag_1X = 15
money_bag_1Y = 15

money_bag_2X = 6
money_bag_2Y = 11

heart_1X     = 12
heart_1Y     = 5

heart_2X     = 12
heart_2Y     = 7


 #robo parameters

charge    = 100 #percents
hp        = 100 #percents
money     = 0   #$



#Field parameters

height  = int( input( "Insert the height of field. Optimal 20. >>> " ))
width   = int( input( "Insert the width of field. Optimal 20. >>> " ))


#LOGIC

while True:
 system( "clear" )
 
 #if robo in good condition
 if(( hp > 0) and (charge > 0 )):
  
  #meeting results
   
   #with bombs
  if((( roboX == bomb_1X ) and ( roboY == bomb_1Y )) or (( roboX == bomb_2X) and (roboY == bomb_2Y ))):
   hp -= 20
   
   #with hearts 
  elif((( roboX == heart_1X ) and ( roboY == heart_1Y )) or (( roboX == heart_2X) and (roboY == heart_2Y ))):
   
   if(( hp < 100 ) and ( charge < 100 )):
    hp += 20
   
    if( charge <= 50 ):
     charge += 50
   
    else:
     charge = 100
   
   #with money_bags 
  elif((( roboX == money_bag_1X ) and ( roboY == money_bag_1Y )) or (( roboX == money_bag_2X) and (roboY == money_bag_2Y ))):
   money  += 20
   charge += 10
 
#if robo in bad condition  
 else:
  if( charge == 0 ):
   print( "Battery low. Game over" )
   break
    
  elif( hp == 0 ):
   print( "Health points = 0. Game over" )
   break
   
   
 
 
 #Display robo parameters

 print( "Your robot parameters:\nhp = %d"%hp + " %" )
 print( "\nBattery Charging Indicator:" )
 print( "%d"%charge + " %")
 print( "=" * charge )
 print( "\nMoney = %d"%money + " $")
 print( "ACTUAL COORDINATES: X = %d; Y = %d\n"%( roboX, roboY ))


# ############# DRAWING THE MAP #######################

##################### Y loop #####################
 y = 1
 while( y <= width ):

    ##################### X loop #####################
  x = 1
  while( x <= height ):

#robo

   if(( roboX == x ) and ( roboY == y )):
    print( "R ", end="" )

#bombs 1 and 2

   elif(( bomb_1X == x ) and ( bomb_1Y == y )):
    print( "B ", end = "" )
   
   elif(( bomb_2X == x ) and ( bomb_2Y == y )):
    print( "B ", end = "" )

#money-bags 1 and 2

   elif(( money_bag_1X == x ) and ( money_bag_1Y == y )):
    print( "M ", end = "" )
   
   elif(( money_bag_2X == x ) and ( money_bag_2Y == y )):
    print( "M ", end = "" )
   
#hearts 1 and 2

   elif(( heart_1X == x ) and ( heart_1Y == y )):
    print( "H ", end = "" )

   elif(( heart_2X == x ) and ( heart_2Y == y )):
    print( "H ", end = "" )
   
 # ----  
   else:
    print("- ", end="")    


   x += 1
    ##################### X loop #####################

  print()    
  y += 1
##################### Y loop #####################

# #################### CONTROLS #####################

 direction = input( "dir ( w/s/a/d/x ) > " )
  
 
 if( direction == "a" ):
  if( roboX > 0 ): 
   roboX -= 1
   charge -= 5
  else:
   roboX = 5
   roboY = 5
   print( "Change direction. You can move only in right." )
   input( "hit ENTER to continue" )

 if( direction == "d" ):
  if( roboX < height ):
   roboX += 1
   charge -= 5
  else:
   roboX = 5
   roboY = 5
   print( "Change direction. You can move only in left." )
   input( "hit ENTER to continue" )

 if( direction == "s" ):
  if( roboY < width ):
   roboY += 1
   charge -= 5
  else:
   roboY = 5
   roboX = 5
   print( "Change direction. You can move only in up." )
   input( "hit ENTER to continue ")

 if( direction == "w" ):
  if( roboY > 0 ):
   roboY -= 1
   charge -= 5
  else:
   roboY = 5
   roboX = 5
   print( "Change direction. You can move only in down." )
   input( "hit ENTER to continue" )

 if( direction == "x" ):
  system( "clear" )
  print( "Thank you for playing!" )
  break





