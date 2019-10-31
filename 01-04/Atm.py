class Atm:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def doing(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Tarik(Atm):
    def doing(self):
        return self.name+' Silahkan Ambil Uang Anda!!'
    
class Setor(Atm):
    def doing(self):
        return self.name+' Masukkan Uang Anda'
    
Dinay = Tarik('Dinay')
Yammi = Setor('Yammi')

print(Dinay.doing())
print(Yammi.doing())