from abc import ABC,abstractmethod

class Tax_Paying(ABC):
    def __init__(self,salary):
        self.salary = salary

    @abstractmethod
    def calculate_tax_value(self):
        pass

class StudentTaxPaying(Tax_Paying):
    def __init__(self,salary):
        Tax_Paying.__init__(self,salary)

    def calculate_tax_value(self):
        return (self.salary * 0.15)

class WorkerTaxPaying(Tax_Paying):
    def __init__(self,salary):
        Tax_Paying.__init__(self,salary)

    def calculate_tax_value(self):
        if self.salary < 80000:
            return (self.salary * 0.17)
        else:
            return (self.salary * 0.18) + ((self.salary-80000) * 0.32)

class DisabledTaxPaying(Tax_Paying):
    def __init__(self,salary):
        Tax_Paying.__init__(self,salary)
    
    def calculate_tax_value(self):
        return (self.salary * 0.12)

Student = StudentTaxPaying(50000)
Disabled = DisabledTaxPaying(70000)
Worker1 = WorkerTaxPaying(68000)
Worker2 = WorkerTaxPaying(120000)

tax_payers = [Student,Disabled,Worker1,Worker2]

for i in tax_payers:
    print(i.calculate_tax_value())

