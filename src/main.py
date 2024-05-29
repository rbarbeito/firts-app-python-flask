from flask import Flask, render_template, request, redirect, url_for
from faker import Faker

app = Flask(__name__)

fake = Faker()


@app.route('/')
def index():

    cursos = [fake.first_name() for _ in range(10)]
    # cursos =[]

    data = {
        "titulo": "Mis Cursos",
        "mensaje": "Saludos",
        "cursos": cursos,
        "cantidad_cursos": len(cursos)
    }

    return render_template('index.html', data=data)


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


def page_not_found(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index')) # haciendo redirect



# contruyendo un middleware
@app.before_request
def before_request():
    print("Ejecutando antes de la request")


@app.after_request
def after_request(response):
    print("Ejecutando despues de la peticion")

    return response




if __name__ == '__main__':

    app.add_url_rule('/query_string', view_func=query_string)

    app.register_error_handler(404, page_not_found)

    app.run(debug=True, port=8080)
