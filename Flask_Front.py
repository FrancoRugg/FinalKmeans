from flask import Flask,redirect,session,render_template,request,send_from_directory,jsonify,send_file, make_response;
import os;
from Kmeans_FrancoRuggiero import data,export_iris_to_csv;

app = Flask(__name__,template_folder="templates",static_folder="static"); #Nombre de la App y Ubicación de los archivos .HTML
#Key de variable de sesion
secret = "1234";
app.secret_key = secret;

@app.route("/style.css")
def style():
    """Get CSS"""
    return send_from_directory(os.path.join(os.path.join(app.root_path,'static'),'css'),'style.css')
@app.route("/favicon.ico")
def icon():
    """Agrega el favicon"""
    return send_from_directory(os.path.join(app.root_path,'static'),'favicon.ico',mimetype='image/vnd.microsoft.icon')
@app.route("/home", methods=['POST','GET'])
def home():
    # csv_file = export_iris_to_csv("iris_data.csv");#Utilizado para llevarme los datos a CSV
    info = ""
    if request.method == "POST":
        # print(request.form['test_size']);
        # if request.form['test_size'] == "1.0":
        #     info = "Ingrese el porcentaje a utilizar";
        # else:
        try:
            file = request.form['csv_file'];
            test_size = float(request.form['test_size']);
            test_size_text = request.form['test_size_text'];
            # print(test_size.text)
            info = f"Porcentaje buscado: {test_size_text}\n \n";
            info += data(test_size,file);
            # info += data(test_size,"iris_data.csv");
        except FileNotFoundError:
            info = "'Seleccione un archivo para poder continuar con la operación'.╰（‵□′）╯";
        
    
        # return render_template("home.html", info=info)
    return render_template("home.html",info=info);
@app.route("/")
def gotoIndex():
    return redirect("/home"); #Si no especifica nada, va al login

app.run(debug = True,host='localhost',port=8001); #Del 65535 hasta el 1023 están reservados.

# debug = True, El servidor se recarga con cada cambio