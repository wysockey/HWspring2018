
year = int(raw_input("What year did you graduate?"))
if(year = 2018) :
        print("Mike Renee,2018,3.2 ,Ricky Alger, 2018, 1.7 , Eric Gregg, 2018,4.2 , Andre Myron, 2018, 2.7 ,
elif(number = 2017):
        print("Alva Barba, 2017, 2.5")
elif(number = 2016):
        print("Cody Sheree, 2016, 3.5")
elif(number = 2019):
        print ("Gorden Dashiell, 2020, 4.0, Opaline, Dorothea, 2020, 1.6")


def make_table(number):
        title= ' '
        for  left_operand in range(1,number+1):
                title= title + '['+str(left_operand)+']'
        print(title)
        for right_operand in range(1,number+1):
                row = '[' + str(right_operand)+']'
                for left_operand in range(1,number+1):
                        multiplied = str(left_operand *right_operand)
                        if(len(multiplied >2)):
                                row = row+ multiplied
                        elif(len(multiplied) >1):
                                row = row + multiplied+ ' '
                        else:
                                row = row  + ' '+ muliplied+ ' '
          
