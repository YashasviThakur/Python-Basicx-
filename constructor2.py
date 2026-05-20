class employee:
   language = "Py"
   salary = 120000

   def __init__(self,name,salary,language):
       self.name = name 
       self.salary = salary 
       self.language = language 
       print("i am creating an object ")
   
   def getInfo(self):
      print(f"The language is {self.language}. The salary is {self.salary}")

   @staticmethod
   def greet() :
      print("Good evening ")
      

harry = employee("HARRY",1300000,"JAVASCRIPT")

print(harry.name, harry.salary)

