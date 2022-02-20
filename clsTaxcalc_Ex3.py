class clsTaxcalc_Ex3(object):
    """Calc Assesment Value and Tax Value"""

    def ShowAssesments(self):
       
        print()
        print("########## Exercise 3 ###############")
        print()

        try:

          ActualValue= input(print('Enter Actual Land Value',sep='\t\n\n'))
          AssesmentValue =  float(ActualValue) * 0.60           # Formula for Assesment Calculation
          PropertyTax =  (float(AssesmentValue) * 0.72)/100     # Formula for Tax Calculation

          print("Assesment Value for the mentioned Property is : ","${:,.2f}".format(AssesmentValue))
          print("Tax Value for the mentioned Property is : ","${:,.2f}".format(PropertyTax))

   
        except (ValueError, RuntimeError, TypeError, NameError) :
         print("Please check the Entered Value")

 
    #ShowAssesments(object) #To execute individually uncomment this line