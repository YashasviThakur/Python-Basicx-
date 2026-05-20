class employee :
    company = "ITC"
    def show(self):
        printf(f"The name is {self.name} and the salary is {self.salary}")


class programmer(employee):
    company = "ITC INFOTECH"
    def showlanguage(self):
        print(f"The name is {self.name} and he is gppd with {self.language} language" )

a = employee()
b = programmer()

print(a.company,b.company)