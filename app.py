from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
db = SQLAlchemy(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///informacion_clientes.db'
#con esto creamos la base de datos con el nombre informacion_clientes
#ahora se deben agregar los campos
class Clientes(db.Model):

    id =db.Column(db.Integer, primary_key = True)
    nombre=db.Column(db.String(100), nullable=False)
    rut=db.Column(db.String(50), nullable=False)
    monto=db.Column(db.Integer, nullable=False)
    fecha_agregado = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Nuevo cliente' + str(self.id)

@app.route('/')
def first():
     return render_template('first_page.html')
     #con esto creamos una pagina principal que despliegue las opciones




@app.route('/AgregarCliente', methods=['GET', 'POST'])#CREAMOS UNA SEGUNDA PAGINA
def AgregarCliente():
    if request.method == 'POST':

        cliente_nombre = request.form['nombre']
        cliente_rut = request.form['rut']
        cliente_monto = request.form['monto']
        nuevo_cliente = Clientes(nombre=cliente_nombre, rut= cliente_rut, monto = cliente_monto)
        db.session.add(nuevo_cliente)#con esto guardamos en la base de datos.
        db.session.commit()#con esto lo aseguramos que siempre estará
        return redirect('/AgregarCliente')

    else:
        return render_template('agregar_clientes.html', )







if __name__ == "__main__":
    app.run(debug=True)  #run from the developer mode
