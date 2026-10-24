from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo="home", mensaje="¡Bienvenido a la Biblioteca Universitaria!")

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html', titulo="Catálogo", mensaje="Explora nuestra colección de recursos académicos y culturales.")
@app.route('/servicios')
def servicios():
    return render_template('servicios.html', titulo="Servicios", mensaje="Descubre los servicios que ofrecemos.")

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', titulo="Contacto", mensaje="Contáctanos para más información.")

if __name__ == '__main__':
    app.run(debug=True)