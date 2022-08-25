class InputOutString(object):
   def __init__(self):
       self.a = ""

   def getString(self):
       self.a = input("Chuỗi:")
   def printString(self):
       print (self.a.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()