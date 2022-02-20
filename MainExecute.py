from clsDvdClubPoints_Ex1 import clsDvdClubPoints  # To use attributes and functions from other classes import- keyword has being used
from clsBMI_Ex2 import clsBMI_Ex2 
from clsTaxcalc_Ex3 import clsTaxcalc_Ex3 
from clsTaxcalc_Ex3 import clsTaxcalc_Ex3 
from clsSumPoints_Ex4 import clsSumPoints_Ex4
from clsMy_Max_Ex5 import clsMy_Max_Ex5
from clsCalcScore_Ex6 import clsCalcScore_Ex6

    # creating the object of the class type

object_a = clsDvdClubPoints() 
object_BMI = clsBMI_Ex2()
object_Asmnt = clsTaxcalc_Ex3()
object_Sumpoint = clsSumPoints_Ex4()
object_My_Max = clsMy_Max_Ex5()
object_score = clsCalcScore_Ex6()


def ExecuteMain():
   
    #Accessing all the methods and attributes from different claases
    
       clsDvdClubPoints.Showearning(object_a) 
       clsBMI_Ex2.ShowBMI(object_BMI)
       clsTaxcalc_Ex3.ShowAssesments(object_Asmnt)
       clsSumPoints_Ex4.CalcSumPoints(object_Sumpoint)
       print()
       print("########## Exercise 5 ###############")
       print()
       clsMy_Max_Ex5.my_max(object_My_Max,no_1 = int(input("Enter a Number 1: ")),no_2 = int(input("Enter a Number 2: ")))
       print()
       print("########## Exercise 6 ###############")
       print()
       clsCalcScore_Ex6.main_call(object_score) 


# Implement Python Switch Case Statement using Class

class AssignmentSwitch:

    def switch(self, Exercises):
        default = "Incorrect Value" #Error Message if any option entered more than 7
        return getattr(self, 'case_' + str(Exercises), lambda: default)() #getattr function is used to return the matching function & if not returned the correct match it getattr function will return the 'default' value

    def case_1(self):
        return clsDvdClubPoints.Showearning(object_a) 
 
    def case_2(self):
        return clsBMI_Ex2.ShowBMI(object_BMI)
 
    def case_3(self):
        return clsTaxcalc_Ex3.ShowAssesments(object_Asmnt)

    def case_4(self):
        return clsSumPoints_Ex4.CalcSumPoints(object_Sumpoint)

    def case_5(self):
        return clsMy_Max_Ex5.my_max(object_My_Max,no_1 = int(input("Enter a Number 1: ")),no_2 = int(input("Enter a Number 2: ")))

    def case_6(self):
        return clsCalcScore_Ex6.main_call(object_score) 

    def case_7(self):
        return ExecuteMain()

s = AssignmentSwitch()

print(s.switch(input("To view all the exercises Press No : '7' Or to view individually enter the specific exercise No: ")))
