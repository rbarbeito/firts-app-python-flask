<<<<<<< HEAD
from flask import Flask, render_template, request
=======
from flask import Flask, render_template
>>>>>>> 634a536af60625eba1647cc19d90bd571436c3d3
from faker import Faker

app = Flask(__name__)

<<<<<<< HEAD
fake = Faker()
=======
fake= Faker()
>>>>>>> 634a536af60625eba1647cc19d90bd571436c3d3


@app.route('/')
def index():

    cursos = [fake.first_name() for _ in range(10)]
    # cursos =[]
<<<<<<< HEAD
=======
    
>>>>>>> 634a536af60625eba1647cc19d90bd571436c3d3

    data = {
        "titulo": "Mis Cursos",
        "mensaje": "Saludos",
        "cursos": cursos,
        "cantidad_cursos": len(cursos)
    }

    return render_template('index.html', data=data)


<<<<<<< HEAD
@app.route('/contacto/<nombre>/<edad>')
def contacto(nombre, edad):

    data = {
        'titulo': 'Contacto',
        'nombre': nombre,
        "edad": edad
    }

    return render_template('contacto.html', data=data)

def query_string():
    print(request)

    print(request.args)

    print(request.args.get('param1'))
    print(request.args.get('param2'))

    return "ok"


if __name__ == '__main__':

    app.add_url_rule('/query_string', view_func=query_string)

=======
if __name__ == '__main__':
>>>>>>> 634a536af60625eba1647cc19d90bd571436c3d3
    app.run(debug=True, port=8080)
