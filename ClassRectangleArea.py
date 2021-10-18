# Justin Thomas
# Week 4 Workshop Question 6
# Defines a class named rectangle that has a method
# to compute the area of the rectangle
# Define the class
class Rectangle():
    # 
    def __init__(self, len, wid):
        # Set the length and width as instance attributes
        self.length = len
        self.width  = wid

    # Function to calculate the area    
    def rectangle_area(self):
        return self.length*self.width
    
# Prompt the user for the length of the sides
len = float(input("Enter the rectangle length: "))
wid = float(input("Enter the rectangle width: "))
# Run the variables
InputRectangle = Rectangle(len, wid)
# Output the calculated area
print(InputRectangle.rectangle_area())
