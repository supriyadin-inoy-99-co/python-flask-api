from werkzeug.wrappers import request
from app import app
from app.controller import DosenController, MahasiswaController

@app.route('/')
def index():
		return 'Hello Flask App'

@app.route('/dosen', methods=['GET', 'POST'])
def dosens():
		if request.methods == 'GET':
			return DosenController.index()
		else:
			return DosenController.save()
@app.route('/dosen/<id>', methods=['GET'])
def dosen_detail(id):
		return DosenController.detail(id)

@app.route('/mahasiswa', methods=['GET'])
def mahasiswas():
		return MahasiswaController.index()