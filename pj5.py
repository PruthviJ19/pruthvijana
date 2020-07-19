

 #class and objects

class MyClass:
    x = 5                                   # creating class
                                            #x is a local variable
p1 = MyClass()
#print(p1.x)                                #creating a object
                                                
#_init_() function is an built in fuction which is alwys executed when class is intited

class Fruit:
    def __init__(Self, flavour,colour):
        Self.flavour = flavour
        Self.colour = colour

pj = Fruit("mango"," yellow")

#print(pj.flavour)
#print(pj.colour)                          #usin --init__() function
                                           # Self word is complusary

class Fruit:
    def __init__(Self,flavour,colour):       #function-v can initilize variables
        Self.flavour = flavour
        Self.colour = colour
    
    def __pj(Self):                        #method-v wont initilize val
       # print("yup! my favourite flavour is " + Self.flavour)  
        
j1 = Fruit("mango", hi)
j1.pj()                                    #objects


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        #print(self.firstname,self.lastname)
        
p = Person("Pruthvi","jana")
p.printname()                                       #python inheritance


class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname                    #parent class
        
    def printname(self):
       # print(self.firstname, self.lastname)
        
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)       #child class
        
x = Student("jana","pruthvi")
x.printname()


def value():
    p = 40
    #print(p)
    
value()











