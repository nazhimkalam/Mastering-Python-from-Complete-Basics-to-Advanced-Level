# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 2019281
# Date: 27/11/2019



def pass_40():                                           #function created called pass_40()
    if defer==0 and fail==80:                            #checks if defer is equal to 0 and if fail is equal to 80
        print("Exclude")                                 #displays "Exclude" if defer is equal to 0 and if fail is equal to 80 
    else:
        print("Do not Progress-module retriever")       #displays "Do not Progress-module retriever" if the  condition is not satisfied   
    
def pass_20():                                      #function created called pass_20()
    if defer==20 and fail==80:                      #checks if defer is equal to 20 and if fail is equal to 80
        print("Exclude")                            #displays "Exclude" if defer is equal to 20 and if fail is equal to 80
    elif defer==0 and fail==100:                    #checks if defer is equal to 0 and if fail is equal to 100
        print("Exclude")                            #displays "Exclude" if defer is equal to 0 and if fail is equal to 100
    else:
        print("Do not Progress-module retriever")   #displays "Do not Progress-module retriever" if the  condition is not satisfied
    
def pass_0():                                     #function created called pass_0()
    if defer==40 and fail==80:                    #checks if defer is equal to 40 and if fail is equal to 80
        print("Exclude")                          #displays "Exclude" if defer is equal to 40 and if fail is equal to 80
    elif defer==20 and fail==100:                 #checks if defer is equal to 20 and if fail is equal to 100
        print("Exclude")                          #displays "Exclude" if defer is equal to 20 and if fail is equal to 100
    elif defer==0 and fail==120:                  #checks if defer is equal to 0 and if fail is equal to 120
        print("Exclude")                          #displays "Exclude" if defer is equal to 0 and if fail is equal to 120
    else:
        print("Do not Progress-module retriever") #displays "Do not Progress-module retriever" if the condition is not satisfied

#Main Program
print("")                           
print("*********Part 01*********")  
print("*****Student Version*****")
print("")
loop=True            #assign variable loop with a boolean value True
while(loop==True):   #loop checks if the condition loop equals True 
    try:
        pass_check=False    #assigns False boolean value to pass_check variable
        defer_check=False   #assigns False boolean value to defer_check variable
        fail_check=False    #assigns False boolean value to fail_check variable

        pass_=int(input("Enter credit level at Pass  = "))   #prompt the user to input the pass credit value
        while pass_check==False:                            #loop for the pass credit value, checks if pass_check variable is equal to false as the condition
            pass_check=pass_ in [0,20,40,60,80,100,120]     #checks if the user entered pass credit is with in range and returns True or false to variable pass_check
            if pass_check==True:                            #checks if pass_check variable is equal to True
                break                                       #breaks/comes out the loop if pass_check is equal to True
            else:
                print("Range error")                                #displays "Range error"
                pass_=int(input("Enter credit level at Pass  = "))   #ask the user to re input the credit value for pass
                
                
        defer=int(input("Enter credit level at Defer = "))  #prompt the user to input the defer credit value
        while defer_check==False:                           #loop for the defer credit value, checks if defer_check variable is equal to false as the condition
            defer_check=defer in [0,20,40,60,80,100,120]    #checks if the user entered defer credit is with in range and returns True or false to variable defer_check
            if defer_check==True:                           #checks if defer_check variable is equal to True
                break                                       #breaks/comes out the loop if defer_check is equal to True
            else:
                print("Range error")                                #displays "Range error"
                defer=int(input("Enter credit level at Defer = "))  #ask the user to re input the credit value for defer
                

        fail=int(input("Enter credit level at Fail  = "))        #prompt the user to input the fail credit value
        while fail_check==False:                                #loop for the fail credit value, checks if fail_check variable is equal to false as the condition
            fail_check=fail in [0,20,40,60,80,100,120]          #checks if the user entered fail credit is with in range and returns True or false to variable fail_check
            if fail_check==True:                                #checks if fail_check variable is equal to True
                break                                           #breaks/comes out the loop if fail_check is equal to True
            else:
                print("Range error")                                #displays "Range error"
                fail=int(input("Enter credit level at Fail  = "))    #ask the user to re input the credit value for fail

        total_credit=pass_+defer+fail           #adds the value of pass,defer,fail and asigns it to total_credit variable
        if total_credit!=120:                   #checks if total_credit variable is not equal to 120
            print("Total incorrect")            #displays "Total incorrect"
            continue                            #re loops the program code from the begining 
        elif pass_==120:                        #checks if pass is equal to 120
            print("Progress")                   #displays "Progress"
        elif pass_==100:                        #checks if pass is equal to 100
            print("Progress-module trailer")    #displays "Progress-module trailer"
        elif pass_==80:                                     #checks if pass is equal to 80
            print("Do not Progress-module retriever")       #displays "Do not Progress-module retriever"
        elif pass_==60:                                     #checks if pass is equal to 60
            print("Do not Progress-module retriever")       #displays "Do not Progress-module retriever"
        elif pass_==40:         #checks if pass is equal to 40
            pass_40()           #calls function pass_40()
        elif pass_==20:         #checks if pass is equal to 20
            pass_20()           #calls function pass_20()
        else:
            pass_0()            #calls function pass_0()
        loop=False              #assign False to loop ,inorder to stop looping the program code
    except:
        print("Integers required")      #displays "Integer required", if the user doesn't enter an integer 
        continue                        #re loops the program code from the begining 
        
