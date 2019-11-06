class Kantor:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Kantor)'.format(self.name))

    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

class LIne1(Kantor):
    def __init__(self, name, age, job):
        Kantor.__init__(self, name, age)
        self.job = job
        print('(LIne1 name: {})'.format(self.name))
    
    def tell(self):
        Kantor.tell(self)
        print('Job: "{}"'.format(self.job))

class line2(Kantor):
    def __init__(self, name, age, salary):
        Kantor.__init__(self, name, age)
        self.salary = salary
        print('(line2 name: {})'.format(self.name))

    def tell(self):
        Kantor.tell(self)
        print('Salary: "{}"'.format(self.salary))

L1 = LIne1('Dinay', 25, 'Admin')
L2 = LIne1('Rizky', 25, 'Programmer')
l1 = line2('Ayuna', 23, '400000')
l2 = line2('Frisca', 21, '2500000')

print()

members = [L1, L2, l1, l2]
for member in members:
    member.tell()
