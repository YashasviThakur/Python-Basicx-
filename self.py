class employee:
   language = "Py"
   salary = 120000
   
   def getInfo(self):
      print(f"The language is {self.language}. The salary is {self.salary}")

harry = employee()
harry.language = "javascript"
harry.getInfo()


