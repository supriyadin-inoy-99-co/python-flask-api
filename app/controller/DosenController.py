from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa
from app import response, app, db
from flask import request

def index(): 
		try:
				dosen = Dosen.query.all()
				data = formatArray(dosen)
				if not dosen:
					return response.badRequest('Tidak ada data dosen')
   
				return response.success(data, "success")
		except Exception as e:
				return response.internalError(e)

def detail(id):
		try:
				dosen = Dosen.query.filter_by(id=id).first()
				mahasiswa = Mahasiswa.query.filter((Mahasiswa.dosen_satu == id) | (Mahasiswa.dosen_dua == id))
    
				if not dosen:
						return response.badRequest('Tidak ada data dosen')
    
				if not mahasiswa:
						return response.badRequest('Tidak ada data mahasiswa')
				
				datamahasiswa = Mahasiswa.mahasiswaDataStructure(mahasiswa)
    
				data = {
					'id': dosen.id,
					'nidn': dosen.nidn,
					'nama': dosen.nama,
					'phone': dosen.phone,
					'mahasiswa': datamahasiswa
				}

				return response.success(data, 'success')
  
		except Exception as e:
				return response.internalError(e)
  
def formatArray(datas):
		array = []

		for i in datas:
				array.append(Dosen.dosenDataStructure(i))

		return array

def save():
		try:
				nidn = request.form.get('nidn')
				nama = request.form.get('nama')
				phone = request.form.get('phone')
				alamat = request.form.get('alamat')
			
				dosens = Dosen(nidn=nidn, nama=nama, phone=phone, alamat=alamat)
				db.session.add(dosens)
				db.session.commit()
			
				return response.success('', 'Success')
		except Exception as e:
				return response.internalError(e)