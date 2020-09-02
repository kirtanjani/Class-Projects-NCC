# CSCE 160 - Prof. Kim - HW2 
#
# DO NOT MOVE, ERASE or MODIFY ANY of the existing code in the template.
# Also, DO NOT move things around.
import math

#-------------------  function definitions --------------------		  

def get_area (a_1, b_1, z_1):
	# returns the area of a triangle given the length
	#  of two sides aa & ab  
	#   and the angle zz in radians
	area = (a_1*b_1*math.sin(z_1))/2

	return area


def rad2deg (rad):
	# converts the angle rad in radians and 
	#    returns the angle in degrees
	deg = rad*(180/math.pi)

	return deg
	

def get_angle (a_1, b_1, c_1):
    
    angle=math.acos(((a_1)*(a_1)+(b_1)*(b_1) - (c_1)*(c_1))/(2*a_1*b_1))
	#  given three sides of a triangle aa, bb & cc
	#    returns the angle opposite of the side with length cc
	#    in radians
    return angle
	

def isNotValidTriangle (aa, bb, cc):
    if (aa==0 or bb==0 or c==0):
         return True
    elif (aa+bb < cc):
        return True
    elif (aa+cc < bb):
        return True
    elif (bb+cc < aa): 
        return True
    else: 
        invalid= False 
	 
    return invalid


#-------------------  Start of the main program --------------------		  
while (True):
    print ("-----------------------")
    print ("Program Modes")
    print ("(1) Enter sides")
    print ("(2) Quit")
    user_choice = int(input ("Enter Mode: "))

    if (user_choice == 1):

		# ask user for sides and read the values in 
        a = float( input("Enter side a: ") )
        b = float( input("Enter side b: ") )
        c = float( input("Enter side c: ") )

        if (isNotValidTriangle(a,b,c)):
            print ("Not a valid triangle!\n")
            continue # learn how to use CONTINUE.
	        # continue forces the program to go back to the beginning
	        # of the most immediate loop that contains this command 

		# get all three angles using the function get_angle
        x = get_angle (b, c, a)
        y = get_angle (a,c,b)
        z = get_angle (a, b,c)

		# get the area using get_area function
        area1 = get_area(a,b,z)
	      
		# convert the angles from radians to degrees using rad2deg function
        x = rad2deg(x)
        y = rad2deg(y)
        z = rad2deg(z)

        print ("Angle x is,",round (x,2))
        print ("Angle y is,",round (y,2))
        print ("Angle z is,",round (z,2))
        print ("The area is,",round (area1,2))
       

      	# print out the results
      	# print angle x,y,z and the area
        
    elif (user_choice == 2):
        print ("Good Bye!")
        break
    
    else:
        print ("Invalid choice.")


