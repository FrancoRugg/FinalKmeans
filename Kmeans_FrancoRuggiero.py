import numpy as np;
import pandas as pd;
from sklearn.cluster import KMeans; #Modelo K MEDIAS
from sklearn.datasets import load_iris;
from sklearn.model_selection import train_test_split;
from scipy.stats import mode; # SE FIJA SI LA ETIQUETA ES IGUAL A LA VERDADERA; CASO CONTRARIO LA PERMUTA;
from sklearn.metrics import accuracy_score;


def data(test_size,csv_file="iris_data.csv"):
    
    data = pd.read_csv(csv_file)
    
    # Asigna características y etiquetas, depende del archivo CSV que cargue.
    x = data.iloc[:, :-1].values  # Toma tocas las columnas menos la última, como características.
    y = data.iloc[:, -1].values   # Agrega la última columna como etiqueta
    
    # iris = load_iris();
    # x = iris.data; #UNTAGGED
    # y = iris.target; #TAGGED
    
    # print(iris);
    # print(x.head()); #NO TIENE HEAD-
    # n_ckusters CANTIDAD DE COLUMNAS
    # random_state SEMILLA DE MEZCLA
    info = "";
    model = KMeans(n_clusters = 3,random_state=11); #DATOS DEL MODELO
    # model.fit(x);# ENTRENO EL MODELO
    # y_predict = model.predict(x);# AVERIGUAR VALORES PARA CADA NÜMERO

    ESPECIE = np.array(['setosa', 'versicolor', 'virginica'])
    # print(y_predict)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=11)


    clusters=model.fit_predict(x_train);

    labels = np.zeros_like(clusters);
    for i in range(3):
        mask = (clusters == i);
        # mode SE FIJA SI LA ETIQUETA ES IGUAL A LA VERDADERA; CASO CONTRARIO LA PERMUTA;
        labels[mask] = mode(y_train[mask])[0];
        
    # print(accuracy_score(y_train,labels));
    info+=f"Acurracy_score: {accuracy_score(y_train,labels)} \n";
    x_train_predict = model.predict(x_train);
    x_test_predict = model.predict(x_test);

    info+=f"Datos entrenamiento: {x_train_predict} \n";
    # print("Datos entrenamiento: ",x_train_predict);
    info+=f"Datos prueba: {x_test_predict} \n";
    # print("DAtos prueba:",x_test_predict);

    i = 0;
    ceroTrain = np.array([]);
    oneTrain = np.array([]);
    twoTrain = np.array([]);
    # print(len(x)); #150
    print(len(x_train));
    while i < len(x_train):
    # while i < len(x_train_predict):
        if x_train_predict[i] == 0:
            ceroTrain = np.append(ceroTrain, x[i])
        elif x_train_predict[i] == 1:
            oneTrain = np.append(oneTrain, x[i])
        elif x_train_predict[i] == 2:
            twoTrain = np.append(twoTrain, x[i])
        # print(x[i],"-----",y_predict[i]);
        i += 1;
        
    i = 0;
    ceroTest = np.array([]);
    oneTest = np.array([]);
    twoTest = np.array([]);
    # print(len(x_test));
    while i < len(x_test):
        if x_test_predict[i] == 0:
            ceroTest = np.append(ceroTest, x[i])
        elif x_test_predict[i] == 1:
            oneTest = np.append(oneTest, x[i])
        elif x_test_predict[i] == 2:
            twoTest = np.append(twoTest, x[i])
        # print(x[i],"-----",y_predict[i]);
        i += 1;
    # # print(cero);
    # # print(one);
    # # print(two);

    # Calcular el promedio de cada grupo
    avg_cero_train = np.mean(ceroTrain,axis=0); 
    avg_one_train = np.mean(oneTrain,axis=0);
    avg_two_train = np.mean(twoTrain,axis=0);

    # Mostrar los promedios
    info+=f"Promedio de 'cero_train': {avg_cero_train} \n";
    # print(f"Promedio de 'cero_train': {avg_cero_train}")
    info+=f"Promedio de 'one_train': {avg_one_train} \n";
    # print(f"Promedio de 'one_train': {avg_one_train}")
    info+=f"Promedio de 'two_train': {avg_two_train} \n";
    # print(f"Promedio de 'two_train': {avg_two_train}")

    # print("-----------------------------");
    info +="----------------------------------------------------------- \n";
    # Calcular el promedio de cada grupo
    avg_cero_test = np.mean(ceroTest,axis=0); 
    avg_one_test = np.mean(oneTest,axis=0);
    avg_two_test = np.mean(twoTest,axis=0);

    # Mostrar los promedios
    info+=f"Promedio de 'cero_test': {avg_cero_test} \n";
    # print(f"Promedio de 'cero_test': {avg_cero_test}")
    info+=f"Promedio de 'one_test': {avg_one_test} \n";
    # print(f"Promedio de 'one_test': {avg_one_test}")
    info+=f"Promedio de 'two_test': {avg_two_test} \n";
    # print(f"Promedio de 'two_test': {avg_two_test}")


# print(X);
# print(y_predict);


    # print(info);
    return info;
# print(info);
# da = data();

# print(da)
def export_iris_to_csv(csv_file):
    iris = load_iris()
    
    data = pd.DataFrame(data=iris.data, columns=iris.feature_names);
    data['species'] = iris.target;

    data.to_csv(csv_file, index=False);
    print(f"Datos exportados exitosamente a {csv_file}");

