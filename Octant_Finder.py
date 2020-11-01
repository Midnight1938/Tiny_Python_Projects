def octant(x, y, z):
    if x >= 0 and y >= 0 and z >= 0: 
        print("Point lies in 1st octant")
          
    elif x < 0 and y >= 0 and z >= 0: 
        print("Point lies in 2nd octant")
          
    elif x < 0 and y < 0 and z >= 0: 
        print("Point lies in 3rd octant")
          
    elif x >= 0 and y < 0 and z >= 0: 
        print("Point lies in 4th octant")
          
    elif x >= 0 and y >= 0 and z < 0: 
        print("Point lies in 5th octant")
          
    elif x < 0 and y >= 0 and z < 0: 
        print("Point lies in 6th octant")
          
    elif x < 0 and y < 0 and z < 0: 
        print("Point lies in 7th octant")
          
    elif x >= 0 and y < 0 and z < 0: 
        print("Point lies in 8th octant")
              
  
# Driver Code  
x, y, z = -11, 2, -9
octant(x, y, z)