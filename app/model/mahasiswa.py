from app import db
from app.model.dosen import Dosen

class Mahasiswa(db.Model):
		__tablename__ = 'mahasiswa'

		id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
		nim = db.Column(db.String(30), nullable=False)
		nama = db.Column(db.String(50), nullable=False)
		phone = db.Column(db.String(15), nullable=False)
		alamat = db.Column(db.Text, nullable=False)
		dosen_satu = db.Column(db.BigInteger, db.ForeignKey(Dosen.id))
		dosen_dua = db.Column(db.BigInteger, db.ForeignKey(Dosen.id))

		def mahasiswaDataStructure(data):
				array = []

				for i in data:
						array.append({
								'id': i.id,
								'nim': i.nim,
								'nama': i.nama,
								'phone': i.phone,
								'alamat': i.alamat,
								'dosen_satu': i.dosen_satu,
								'dosen_dua': i.dosen_dua
						})

				return array

		def __repr__(self):
	
				return '<Mahasiswa {}>'.format(self.name)