from flask import Flask , render_template , request , jsonify
import prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# API escuchando a solicitudes POST y prediciendo sentimientos
@app.route('/predict' , methods = ['POST'])
def predict():

    response = ""
    review = request.json.get('customer_review')
    if not review:
        response = {'status' : 'error',
                    'message' : 'Reseña vacía'}
    
    else:

        # Llamando al método predict del módulo prediction.py
        sentiment , path = prediction.predict(review)
        response = {'status' : 'success',
                    'message' : 'Listo',
                    'sentiment' : sentiment,
                    'path' : path}

    return jsonify(response)


# Creando una API para guardar la reseña cuando el usuario haga clic en el botón Guardar
@app.route('/save-entry' , methods = ['POST'])
def save():

    # Extrayendo fecha, nombre del producto, reseña, sentimientos asociados desde los datos JSON
    date = request.json.get('date')
    product = request.json.get('product')
    review = request.json.get('review')
    sentiment = request.json.get('sentiment')

    # Creando una variable final separada por comas
    data_entry = date + "," + product + "," + review + "," + sentiment

    # Abrir el archivo en modo "append"
    file_handler = open('./static/assets/datafiles/data_entry.csv' , 'a')
    
    # Registrar los datos en el archivo
    file_handler.write(entry + '\n')
    # Regresar un mensaje de éxito
    return jsonify({'status' : 'success' , 
                    'message' : 'Datos registrados'})


if __name__  ==  "__main__":
    app.run(debug = True)