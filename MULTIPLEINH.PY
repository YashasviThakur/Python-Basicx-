class employee :
    company = "ITC"
    name = "default name"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.company}")

class coder :
    language = "python"
    def printlanguage(self):
        print(f"Out of all language here is your language {self.language}")


class programmer(employee,coder):
    company = "ITC INFOTECH"
    def showlanguage(self):
        print(f"The name is {self.company} and he is goodd with {self.language} language" )

a = employee()
b = programmer()

b.printlanguage()
b.showlanguage()
b.show()