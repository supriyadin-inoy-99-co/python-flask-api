from app.model.mahasiswa import Mahasiswa
from app import response, app, db
from flask import request

def index(): 
		try:
				dosen = Mahasiswa.query.all()
				data = formatArray(dosen)
				return response.success(data, "success")
		except Exception as e:
				return response.internalError(e)
    
def formatArray(datas):
		array = []

		for i in datas:
				array.append(Mahasiswa.mahasiswaDataStructure(i))

		return array
