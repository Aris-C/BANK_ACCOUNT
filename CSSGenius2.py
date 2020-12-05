# Python program to show that we can create instance variables inside methods

#Class for computer Science Student

class CSSGenius2:
  # Class variable
    stream = 'Coumputer Science'

    #the init method/constructor
    def __init__(self, classCode):
        self.classCode = classCode


    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address


a = CSSGenius2
a.setAddress("Noida, UP")
print(a.getAddress())


        
