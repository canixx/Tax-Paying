from abc import ABC, abstractmethod
class Tax_paying(ABC):

    def __init__(self,salary):
        self.salary = salary

    @abstractmethod
    def calculate_tax_value(self):
        pass

class StudentTaxPaying(Tax_paying):
    def __init__(self,salary):
        Tax_paying.__init__(self,salary)

    def calculate_tax_value(self):
        tax_value = (self.salary * 15)/100
        return tax_value

class WorkerTaxPaying(Tax_paying):
    def __init__(self,salary):
        super().__init__(salary)

    def calculate_tax_value(self):
        if self.salary < 80000:
            tax_value = (self.salary*17)/100
            return tax_value
        else:
            tax_value= (self.salary*18)/100 + ((self.salary-80000)*32)/100
            return tax_value

class DisabledTaxPaying(Tax_paying):
    def __init__(self,salary):
        super().__init__(salary)

    def calculate_tax_value(self):
        tax_value = (self.salary * 12) / 100
        return tax_value


salary1= StudentTaxPaying(50000)
salary2= DisabledTaxPaying(70000)
salary3=WorkerTaxPaying(68000)
salary4= WorkerTaxPaying(120000)

tax_payers = [salary1,salary2,salary3,salary4]

for slry in tax_payers:
    print(slry.calculate_tax_value())

