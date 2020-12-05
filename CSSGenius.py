# class for computer science student
class CSSGenius:
    #class variable
    stream = 'Computer Science'
    
    def __init__(self, classCode):

        #Instance Varable
        self.classCode = classCode

#Objective of CSS studen class

a = CSSGenius(101)
b = CSSGenius(102) 
print(a.stream) # prints "computer science
print(b.stream) # prints ^^^^
print(a.classCode)



print(CSSGenius.stream)









    
