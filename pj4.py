
def tri_recursion(i):#initialise i
    if(i > 0):#check conditon of i
        result = i + tri_recursion(i - 1)#if condtion is true
       # print(result)
    else:#if condition is false
        result = 0
    return result                            # example for recursion
#print("\n\nRecursion example results")
tri_recursion(7)#assign i value

def myfunc():#decalre function
    x = 400#assign x value
   # print(x)#print x value                       #python scopes
    
myfunc()




def name():#decalre function
    x = "jana"#assign a value
    def name1():#declare another funtion
       # print(x)#x value is printed
    name1()#function is called
                                       #local scope example
name()                                 #function inside function


p = "pruthvi"

def myname():
    #print(p)
    
myname()

#print(p)                              #global scope-variable is created in main
                                         body of code is a global variable and belongs
                                         to global scope#
                                         
                     

