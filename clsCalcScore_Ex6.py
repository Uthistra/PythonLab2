class clsCalcScore_Ex6(object):
     #self keyword- represents the current instance of the class
    def calc_average(self,test1:float,test2:float,test3:float,test4:float,test5:float): #calculates the average of the test scores
        try:
            average_score=(test1+test2+test3+test4+test5)/5
            return average_score
        except ValueError:
            print("Please checked the entered value")

    def determine_grade(self,testscore:float): #retrieves the Grades
        try :
            if 90 <= testscore <= 100 :
                letter_grade = "A"
            elif 80 <= testscore <= 89 :
                letter_grade = "B"
            elif 70 <= testscore <= 79 :
                letter_grade = "C"
            elif 60 <= testscore <= 69 :
                letter_grade = "D"
            else:
                letter_grade = "F"
            return letter_grade

        except (ValueError, RuntimeError, TypeError, NameError) :
            print("Please double check the entered Value")

    def main_call(self):
        try :

            test1 = float(input('Enter the score for test 1: '))
            print("Your Grade for Test 1 is : ",self.determine_grade(test1))
            test2 = float(input('Enter the score for test 2: '))
            print("Your Grade for Test 2 is : ",self.determine_grade(test2))
            test3 = float(input('Enter the score for test 3: '))
            print("Your Grade for Test 3 is : ",self.determine_grade(test3))
            test4 = float(input('Enter the score for test 4: '))
            print("Your Grade for Test 4 is : ",self.determine_grade(test4))
            test5 = float(input('Enter the score for test 5: '))
            print("Your Grade for Test 5 is : ",self.determine_grade(test5))
            self.calc_average(test1 , test2 , test3 , test4 , test5)
            print("Your Overall Average is : ",self.calc_average(test1,test2,test3,test4,test5))

        except (ValueError, RuntimeError, TypeError, NameError):
            print("Please double check the entered Value")
      


#x=clsCalcScore_Ex6()
#x.main_call()