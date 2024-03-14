from flask import Flask, render_template
from faker import Faker

app = Flask(__name__)

fake= Faker()


@app.route('/')
def index():

    cursos = [fake.first_name() for _ in range(10)]

    data = {
        "titulo": "Index",
        "mensaje": "Saludos",
        "cursos": cursos
    }

    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
