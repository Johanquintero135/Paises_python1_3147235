## Importar, utilizar
# Una dependencia en python

from flask import Flask,render_template

# Crear la aplicación de Flask 

app = Flask(__name__)

# Utilizar Flask para crear una ruta

@app.route('/prueba')
def prueba():
    # Defino la lista de paises
    paises = [
        {
            'nombre':'Argentina',
            'capital':'Buenos Aires',
            'moneda':'Peso argentino',
            'poblacion':'45',
            'superficie':'2',
            'ciudades':[
                'Cordoba', 
                'Rosario',
                'Mendoza'  
                ]
            
        },
        
        {
            'nombre':'Brasil',
            'capital':'Brasilia',
            'moneda':'Real Brasileño',
            'poblacion':'214',
            'superficie':'8,16',
            'ciudades':[
                'Sao Paulo',
                'Rio de Janeiro', 
                'Salvador'
            ]
        },
        {
            'nombre':'Venezuela',
            'capital':'Caracas',
            'moneda':'Bolivar',
            'poblacion':'28',
            'superficie':'916',
            'ciudades':[
                'Maracaibo',
                'Valencia', 
                'Barquisimeto'
            ]
        },
        {
            'nombre':'Uruguay',
            'capital':'Montevideo',
            'moneda':'Peso Uruguayo',
            'poblacion':'3,5',
            'superficie':'176',
            'ciudades':[
                'Salto', 
                'Paysandú',
                'Las Piedras'
            ]
        },
        {
            'nombre':'Rusia',
            'capital':'Moscu',
            'moneda':'Rublo Ruso',
            'poblacion':'144',
            'superficie':'17',
            'ciudades':[
                'San Petersburgo',
                'Novosibirsk', 
                'Ekaterimburgo'
            ]
        }
    ]
    return render_template('paises.html',
                            paises = paises,
                            usuario ="Yate")

