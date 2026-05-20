class employee:
    def __init__(self):
         print("HELLO MR ")
    a = 1 

class Programmer (employee):
     def __init__(self):
         print("HELLO MRS ")
     b = 2

class Manager(Programmer):
      def __init__(self):
         super().__init__()
         print("HELLO ANIL ")
      c = 3

o = employee()

print(o.a) #prints the a attribute 
# print(o.b) #shows an error as there is no b 

o = Programmer()
print(o.a,o.b)