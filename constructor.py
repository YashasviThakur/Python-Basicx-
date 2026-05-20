class employee:
   language = "Py"
   salary = 120000

   def __init__(self): #dunder method which is automatically called 
      print("i am creating an object ")
   
   def getInfo(self):
      print(f"The language is {self.language}. The salary is {self.salary}")

   @staticmethod
   def greet() :
      print("Good evening ")
      

harry = employee()
harry.name = "Harry"
print(harry.name, harry.salary)

