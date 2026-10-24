Primero se creó una carpeta para el proyecto de la biblioteca universitaria. Dentro de ella se organizó la estructura necesaria para trabajar con Flask

Se instaló la librería Flask utilizando la terminal con el siguiente comando:pip install flask

Después se generó el archivo requirements.txt para guardar las dependencias utilizadas en el proyecto 
pip freeze > requirements.txt

Se configuraron cuatro rutas para acceder a las diferentes páginas del sitio web.

Python
@app.route('/')
def index():
return render_template('index.html')

Para cumplir con los requisitos del proyecto se enviaron las variables titulo y mensaje a cada página.

Se creó el archivo layout.html, el cual sirve como plantilla principal para todas las páginas.

En esta plantilla se agregó:

Estructura básica HTML.
Referencia a Bootstrap.
Título del documento.
Menú de navegación.
Bloque de contenido dinámico.

También se incluyeron enlaces para navegar entre:

Inicio
Catálogo
Servicios
Contacto

Esto permitió reutilizar la misma estructura en todas las páginas y mantener un diseño uniforme

Se verificó que:

Todas las rutas funcionaran correctamente.
El menú de navegación permitiera cambiar entre páginas.
Se mostraran los mensajes enviados desde Flask.
El diseño fuera consistente en todo el sitio.

Resultado final

Se desarrolló un sitio web básico para una biblioteca universitaria utilizando Flask, HTML y Bootstrap. El sistema cuenta con cuatro páginas principales (Inicio, Catálogo, Servicios y Contacto), todas conectadas mediante un menú de navegación y generadas a través de plantillas reutilizables. Esto permitió cumplir con todos los requisitos solicitados en la práctica