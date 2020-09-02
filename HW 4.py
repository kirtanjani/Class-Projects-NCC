# Alena Troia and Stephanie Kostrzeski and Kirtan Jani
# HW 4: Sort by distance from origin
# Due 10/25/19

# Import needed functions
import math



#----------------------function definition --------------------------

def getArrays(list1, list2):
    N = len(list1)
    # Gather user input
    for i in range (0, N, 1):
        list1 [i] = int(input("Enter X:"))
        list2 [i] = int(input("Enter Y:"))
        print ("--------------")

def sortParallelLists (list1, list2):
    # Create blank distance array
    distance_list= [None] * len(list1)
    
    # Fill in distance array with calculated distances
    for i in range (0, len(list1), 1):
        distance_list[i] = math.sqrt ((list1[i]*list1[i])+(list2[i]*list2[i]))
    print(distance_list)
    
    # Sort distance array
    for j in range (len(distance_list)-1):
        current = j 
        min = distance_list [current]
        minIndex = j
        for k in range (current + 1, len(distance_list)):
            if (distance_list[k] < min):
                min = distance_list [k]
                minIndex = k
        distance_list[minIndex] = distance_list[current]
        distance_list [current] = min
        # Three line swap for lists 1 and 2
        temp = list1 [minIndex] 
        list1 [ minIndex] = list1 [current] 
        list1 [current] = temp
        temp2 = list2 [minIndex] 
        list2 [ minIndex] = list2 [current] 
        list2 [current] = temp2

# ------------- main program -------------------------------------

# Ask for length of arrays
N = int(input("How many coordinates do you want to enter in?:"))

# Create blank arrays
array1 = [None] * N
array2 = [None] * N

# Fill in arrays
getArrays (array1, array2)

# Sort distance array along with arrays 1 and 2
sortParallelLists (array1, array2)

for l in range (N):
    print ("(",array1[l],",",array2[l],")" )
    


