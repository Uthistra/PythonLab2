class clsBMI_Ex2(object):
    """Calculates the BMI"""

    def ShowBMI(self): #self keyword- represents the current instance of the class
        
       print()
       print("########## Exercise 2 ###############")
       print()

       try:
         Weight= input(print('Enter Weight in Kg',sep='\t\n\n'))
         Height= input(print('Enter Height in Meters',sep='\t\n\n'))
         Weight=float(Weight)
         Height=float(Height)
         BMI = Weight / ( Height * Height ) #BMI Calculation

         if ( float(BMI) < 18.5): 
            print("Your weight is ,",BMI," So,You are Underweight") 
         elif 18.5 <= float(BMI) <= 24.99 :
            print("Your weight is ,",BMI," So,You are Normalweight") #8500*19
         elif 25.0 <= float(BMI) <= 29.99 :
            print("Your weight is ,",BMI," So,You are Overweight") #8500*19
         elif float(BMI) >= 30 :
            #print("You are suffering from Obesity")
            print("Your weight is ,",BMI," So,You are suffering from Obesity") #8500*19
         else :
            print("Criterias Not Met")

       except (ValueError, RuntimeError, TypeError, NameError,ZeroDivisionError) : #Exception is used to tackle the unforseen error without exiting the Full Program
            print("Please check the Entered Value")


    #ShowBMI(object) #To execute individually uncomment this line