# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 2019281
# Date: 27/11/2019 

def pass_40():                   #function created called pass_40()
    exclude=False                #assign False to exclude variable
    if defer==0 and fail==80:    #checks if defer is equal to 0 and if fail is equal to 80
        print("Exclude")         #displays "Exclude" if defer is equal to 0 and if fail is equal to 80 
        exclude=True             #assign True to exclude variable
        return exclude           #returns the value of exclude
    else:
        print("Do not progress-module retriever") #displays "Do not Progress-module retriever" if the  condition is not satisfied

def pass_20():                      #function created called pass_20()
    exclude=False                   #assign False to exclude variable
    if defer==20 and fail==80:      #checks if defer is equal to 20 and if fail is equal to 80
        print("Exclude")            #displays "Exclude" if defer is equal to 20 and if fail is equal to 80
        exclude=True                #assign True to exclude variable
        return exclude              #returns the value of exclude
    elif defer==0 and fail==100:    #checks if defer is equal to 0 and if fail is equal to 100
        print("Exclude")            #displays "Exclude" if defer is equal to 0 and if fail is equal to 100
        exclude=True                #assign True to exclude variable
        return exclude              #returns the value of exclude
    else:
        print("Do not progress-module retriever") #displays "Do not Progress-module retriever" if the  condition is not satisfied

def pass_0():                   #function created called pass_0()
    exclude=False               #assign False to exclude variable
    if defer==40 and fail==80:  #checks if defer is equal to 40 and if fail is equal to 80
        print("Exclude")        #displays "Exclude" if defer is equal to 40 and if fail is equal to 80
        exclude=True            #assign True to exclude variable
        return exclude          #returns the value of exclude
    elif defer==20 and fail==100: #checks if defer is equal to 20 and if fail is equal to 100
        print("Exclude")          #displays "Exclude" if defer is equal to 20 and if fail is equal to 100
        exclude=True              #assign True to exclude variable
        return exclude           #returns the value of exclude
    elif defer==0 and fail==120: #checks if defer is equal to 0 and if fail is equal to 120
        print("Exclude")         #displays "Exclude" if defer is equal to 0 and if fail is equal to 120
        exclude=True             #assign True to exclude variable
        return exclude           #returns the value of exclude
    else:
        print("Do not progress-module retriever") #displays "Do not Progress-module retriever" if the condition is not satisfied

#Main Program
print("")
print("**********Part 03***********")
print("*****Vertical Histogram*****")
print("")
student=0       #assign 0 to student variable
student_p=0     #assign 0 to student_p variable
student_t=0     #assign 0 to student_t variable
student_r=0     #assign 0 to student_r variable
student_e=0     #assign 0 to student_e variable

quit_=str(input("Enter q if you need to exit else click any key to continue "))  #asks the user whether to quit or continue
while(quit_!="q"):          #loops the program code when variable quit_ is not equal to q
    try:
        pass_check=False    #assigns False boolean value to pass_check variable
        defer_check=False   #assigns False boolean value to defer_check variable
        fail_check=False    #assigns False boolean value to fail_check variable

        pass_=int(input("Enter credit level at Pass  = "))  #prompt the user to input the pass credit value
        while pass_check==False:                           #loop for the pass credit value, checks if pass_check variable is equal to false as the condition
            pass_check=pass_ in [0,20,40,60,80,100,120]    #checks if the user entered pass credit is with in range and returns True or false to variable pass_check
            if pass_check==True:                           #checks if pass_check variable is equal to True
                break                                      #breaks/comes out the loop if pass_check is equal to True
            else:
                print("Range error")                               #displays "Range error"
                pass_=int(input("Enter credit level at Pass  = "))  #ask the user to re input the credit value for pass
                
                
        defer=int(input("Enter credit level at Defer = ")) #prompt the user to input the defer credit value
        while defer_check==False:                          #loop for the defer credit value, checks if defer_check variable is equal to false as the condition
            defer_check=defer in [0,20,40,60,80,100,120]   #checks if the user entered defer credit is with in range and returns True or false to variable defer_check
            if defer_check==True:                          #checks if defer_check variable is equal to True
                break                                      #breaks/comes out the loop if defer_check is equal to True
            else:
                print("Range error")                               #displays "Range error"
                defer=int(input("Enter credit level at Defer = ")) #ask the user to re input the credit value for defer
                

        fail=int(input("Enter credit level at Fail  = ")) #prompt the user to input the fail credit value
        while fail_check==False:                         #loop for the fail credit value, checks if fail_check variable is equal to false as the condition
            fail_check=fail in [0,20,40,60,80,100,120]   #checks if the user entered fail credit is with in range and returns True or false to variable fail_check
            if fail_check==True:                         #checks if fail_check variable is equal to True
                break                                    #breaks/comes out the loop if fail_check is equal to True
            else:
                print("Range error")                             #displays "Range error"
                fail=int(input("Enter credit level at Fail  = ")) #ask the user to re input the credit value for fail

        total_credit=pass_+defer+fail #adds the value of pass,defer,fail and asigns it to total_credit variable
        if total_credit!=120:         #checks if total_credit variable is not equal to 120
            print("Total incorrect")  #displays "Total incorrect"
        elif pass_==120:      #checks if pass is equal to 120
            print("Progress") #displays "Progress"
            student_p+=1      #Increment the student_p variable
            student+=1        #Increment the student variable
        elif pass_==100:                     #checks if pass is equal to 100
            print("Progress-module trailer") #displays "Progress-module trailer"
            student_t+=1    #Increment the student_t variable
            student+=1      #Increment the student variable
        elif pass_==80:                               #checks if pass is equal to 80
            print("Do not progress-module retriever") #displays "Do not Progress-module retriever"
            student_r+=1    #Increment the student_r variable
            student+=1      #Increment the student variable
        elif pass_==60:                              #checks if pass is equal to 60
            print("Do not progress-module retriever")#displays "Do not Progress-module retriever"
            student_r+=1    #Increment the student_r variable
            student+=1      #Increment the student variable
        elif pass_==40:             #checks if pass is equal to 40
            if pass_40()==True:     #calls the pass_40()function and compares whether its return value is equal to True
                student_e+=1        #Increment the student_e variable
                student+=1          #Increment the student variable
            else:
                student_r+=1        #Increment the student_r variable
                student+=1          #Increment the student variable  
        elif pass_==20:             #checks if pass is equal to 20
            if pass_20()==True:     #calls the pass_20()function and compares whether its return value is equal to True
                student_e+=1        #Increment the student_e variable
                student+=1          #Increment the student variable
            else:
                student_r+=1        #Increment the student_r variable
                student+=1          #Increment the student variable  
        else:
            if pass_0()==True:      #calls the pass_0()function and compares whether its return value is equal to True
                student_e+=1        #Increment the student_e variable
                student+=1          #Increment the student variable
            else:
                student_r+=1        #Increment the student_r variable
                student+=1          #Increment the student variable
                           
        quit_=str(input("Enter q if you need to exit else click any key to continue ")) #asks the user whether to quit or continue
        
            
    except:
        print("Integers required") #displays "Integers required", incase if the user didn't enter a numerical value
print("\n")       
print("Progress  "+str(student_p)+" :  "+"*"*student_p) #displays the number of Progress students and the histogram for Progress
print("Trailing  "+str(student_t)+" :  "+"*"*student_t) #displays the number of Tailing students and the histogram for Tailing
print("Retriever "+str(student_r)+" :  "+"*"*student_r) #displays the number of Retriever students and the histogram for Retriever
print("Excluded  "+str(student_e)+" :  "+"*"*student_e) #displays the number of Excluded students and the histogram for Excluded
print("\n") #used to create a new line
print(str(student)+" outcomes in total.\n\n") #displays total number of outcomes and creates two extra lines

print('Progress  Trailing  Retriever  Excluded')     #displays the headings for the veritical histogram
max_array=[student_p,student_t,student_r,student_e]  #stores number of students for each progression category in an array
maximum_value=max(max_array)             #gets the maximum value from the array
for i in range(maximum_value):           #creates a loop and it loops maximum_value number of times 
    if student_p>0:                      #compares if student_p is greater than 0                     
        progress_star='    *   '         #progress_star is assigned with '    *   ' 
    else:
        progress_star='        '         #progress_star is assigned with '        ' 

    if student_t>0:                    #compares if student_t is greater than 0
        trailing_star='     *   '      #trailing_star is assigned with '     *   '
    else:
        trailing_star='         '      #trailing_star is assigned with '         '

    if student_r>0:                    #compares if student_r is greater than 0
        retriever_star='       *   '   #retriever_star is assigned with '       *   '
    else:
        retriever_star='           '   #retriever_star is assigned with '           '

    if student_e>0:                    #compares if student_e is greater than 0
        excluded_star='       *   '    #excluded_star is assigned with '       *   '
    else:
        excluded_star='           '    #excluded_star is assigned with '           '

    student_p=student_p-1       #student_p is decremented by 1 
    student_t=student_t-1       #student_t is decremented by 1
    student_r=student_r-1       #student_r is decremented by 1
    student_e=student_e-1       #student_e is decremented by 1

    print(progress_star+trailing_star+retriever_star+excluded_star) #concatenates and displays the values stored in progress_star,trailing_star,retriever_star,excluded_star
    
    
    











    












