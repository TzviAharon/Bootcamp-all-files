###########################################
# Question 1 - do not delete this comment #
###########################################

class Matrix:
    
    pass #replace this line with your implementation
  

    
###########################################
# Question 2 - do not delete this comment #
###########################################

######### do not edit this class ##########
class Point: 
    def __init__(self,x,y):
        ''' x and y are int or float '''
        self.x = x
        self.y = y
    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    def distance(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
    def shift(self,dx,dy):
        self.x += dx
        self.y += dy
###########################################
        

class Polygon:

    pass #replace this line with your implementation       


class Square(Polygon):
        
    pass #replace this line with your implementation        

        
class Triangle(Polygon):
    
    pass #replace this line with your implementation