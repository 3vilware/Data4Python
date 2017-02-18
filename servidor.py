from flask import Flask, jsonify
from script import administrador

app = Flask('inicio')

@app.route('/usuario')

def usuario():
	admin = administrador()
	data = admin.mostrar()
	resp = jsonify(data)
	print(data)
	return resp

app.run()

#l = ['ricardo', 'amador', 'cast', 'r@hotmail.com', '12345', 0]

admin = administrador()
admin.mostrar()