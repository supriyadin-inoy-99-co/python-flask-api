from app import db
from datetime import datetime

class Dosen(db.Model):
		__tablename__ = 'dosen'
  
		id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
		nidn = db.Column(db.String(30), nullable=False)
		nama = db.Column(db.String(50), nullable=False)
		phone = db.Column(db.String(15), nullable=False)
		alamat = db.Column(db.Text, nullable=False)
		
		def dosenDataStructure(data):
				data = {
					'id': data.id,
					'nidn': data.nidn,
					'nama': data.nama,
					'phone': data.phone,
					'alamat': data.alamat
				}
				
				return data
	
		def __repr__(self):
				return '<Dosen {}>'.format(self.name)