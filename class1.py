class Mahasiswa():
    def __init__(self, nama, nim, alamat):
        self.nama = nama
        self.nim = nim
        self.alamat = alamat

    def cek_data_mahasiswa(self):
        print('nama :', self.nama, '\nnim :',self.nim, '\nalamat :',self.alamat)

class Dosen(Mahasiswa):

    def cek_data_mahasiswa(self):
        print('nama :', self.nama,'\nalamat :', self.alamat)

mahasiswa1 = Mahasiswa('irwan', '08126671', 'jakarta barat')
mahasiswa1.cek_data_mahasiswa()
mahasiswa2 = Mahasiswa('yami', '08126671', 'bantul')
mahasiswa2.cek_data_mahasiswa()

dosen = Dosen('riko','08126671', 'jakarta selatan')
dosen.cek_data_mahasiswa()