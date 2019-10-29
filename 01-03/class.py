class YammiMember:
    '''Represents any Yammi member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(ini YammiMember: {})'.format(self.name))

    def tell(self):
        '''Tell my details.'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teman(YammiMember):
    '''Represents a Teman.'''
    def __init__(self, name, age, salary):
        YammiMember.__init__(self, name, age)
        self.salary = salary
        print('(ini Teman: {})'.format(self.name))

    def tell(self):
        YammiMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class konco(YammiMember):
    '''Represents a konco.'''
    def __init__(self, name, age, marks):
        YammiMember.__init__(self, name, age)
        self.marks = marks
        print('(ini konco: {})'.format(self.name))

    def tell(self):
        YammiMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teman('Mrs. Dinar Kumala', 24, 30000)
s = konco('Anindito', 25, 75)

# prints a blank line
print()

members = [t, s]
for member in members:
    # Works for both Temans and koncos
    member.tell()
