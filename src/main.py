from flask import Flask

app=Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hola Mundo</h1><p>asi mismo loco</p>'



if __name__ == '__main__':
    app.run(debug=True,port=8080)