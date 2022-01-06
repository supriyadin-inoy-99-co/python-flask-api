from flask import jsonify, make_response

def success(values, message):
		code = 200
		res = {
			'code': code,
			'message': message,
			'data': values
		}

		return make_response(jsonify(res)), code

def badRequest(message):
		code = 400
		res = {
			'code': code,
			'message': message
		}

		return make_response(jsonify(res)), code

def internalError(message):
		code = 500
		res = {
			'code': code,
			'message': message
		}

		return make_response(jsonify(res)), code