class clsMy_Max_Ex5(object):
    """Find Maximum of Two Values"""
          
    def my_max(self,no_1, no_2 ):
       
       try:
         
           if no_1 >= no_2: # checks for the greater value and displays values accordingly
           # print("greater of the entered two numbers are",int(no_1))
            return no_1
           else:
          #  print("greater of the entered two numbers are",int(no_2))
            return no_2


       except (ValueError, RuntimeError, TypeError, NameError) :#Exception is used to tackle the unforseen error without exiting the Full Program
          print("Please check the Entered Value")


    #my_max(object,no_1 = float(input("Enter a Number 1: ")),no_2 = float(input("Enter a Number 2: "))) #To execute individually uncomment this line
       

   