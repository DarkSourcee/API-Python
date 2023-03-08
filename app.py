from flask import Flask
from Controller.usuarios import usuarios
from Controller.fornecedores import fornecedores

app = Flask(__name__)
app.register_blueprint(usuarios)
app.register_blueprint(fornecedores)

if __name__ == '__main__':
    app.run(debug=True)
