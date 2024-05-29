from flask import Flask, render_template, request, redirect, url_for, jsonify
from faker import Faker

from flask_mysqldb import MySQL

app = Flask(__name__)

fake = Faker()

# Cnexion a Base de Datos
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='M@ripos4'
app.config['MYSQL_DB']='empresa'

cnx = MySQL(app)


# contruyendo un middleware
@app.before_request
def before_request():
    print("Ejecutando antes de la request")


@app.after_request
def after_request(response):
    print("Ejecutando despues de la peticion")

    return response



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



@app.route('/basedatos')
def base_datos():
    data={}

    try:
        cursor=cnx.connection.cursor()

        sql='Select * from departamentos'
        cursor.execute(sql)
        res= cursor.fetchall()

        print(res)

        data['oficinas'] = res
        data['mensaje'] = 'Exito'

    except Exception as e:
        data['mensaje']='Error'

    return jsonify(data)

def page_not_found(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index')) # haciendo redirect






if __name__ == '__main__':

    app.add_url_rule('/query_string', view_func=query_string)

    app.register_error_handler(404, page_not_found)

    app.run(debug=True, port=8080)
