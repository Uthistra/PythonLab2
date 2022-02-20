class clsDvdClubPoints(object):
    """Calculates the Earning Points of Purchased Videos"""


     #self keyword- represents the current instance of the class

    def Showearning(self):
        try :
            print()
            print("########## Exercise 1 ###############")
            print()
            x= input(print('Enter Number Of Purchased Videos Per Month:',sep='\t\n\n'))

            if ( int(x) < 0): 
                print("Your earning is 0 points")
            elif int(x) == 1:
                print("Your earning is 5 points")
            elif int(x) == 2:
                print("Your earning is 15 points")  
            elif int(x) == 3:
                print("Your earning is 30 points") 
            elif int(x) > 4 :
                print("Your earning is 60 points")  
            else :
                print("Criterias Not Met") #if any of the above criterias not met, programme will output as "Criterias Not Met

        except (ValueError, RuntimeError, TypeError, NameError): #to tackle the unforseen error without exiting the Full Program
            print("Please double check the entered Value")

    #Showearning (object) #To execute individually uncomment this line
