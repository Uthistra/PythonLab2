class clsSumPoints_Ex4(object):
    """Sum Positive Numbers and Enter Negative Value to quit"""

    def CalcSumPoints(self):
        
        print()
        print("########## Exercise 4 ###############")
        print()

        try:
         sumSeriesValue=0
         while 1 : #Check user is entering the value
             Ponumber = float(input("Enter a Positive Number to get the Sum Value and Enter Negative Value to quit:"))
             if Ponumber>=0 : #Check the entered values is Positive number
                 sumSeriesValue+=Ponumber #Sums all the positive values
             else:
                 return print(" Total Sum Value is : ",sumSeriesValue) 
        except (ValueError, RuntimeError, TypeError, NameError): #to tackle the unforseen error without exiting the Full Program
         
            print(" Please check the Entered Value , but Current Sum value is ",sumSeriesValue) #Shows the Invalid message with the entered Sum
          
#holds the value of the return function
    #CalcSumPoints(object)


                  