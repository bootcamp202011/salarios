import requests
import pathlib
<<<<<<< HEAD
 


def mayus(salaries_df):
    #Convierte los nombres de las columnas del dataset a mayúsculas
    
    #Parametros: 
    # salaries_df (dataframe): el data frame para el cual se necesita modificar los nombres de las columnas 
    
    #Regresa:
    # salaries_df (dataframe): el dataframe modificado

    salaries_df.columns = salaries_df.columns.str.upper()
    return(salaries_df)
=======
import sys
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import numpy as np
import seaborn as sns; sns.set()
import scipy.stats
 

def mayus(salaries_df):
  """
  Convierte los nombres de las columnas del dataset a mayúsculas
  
  Parámetros: 
    salaries_df (dataframe): el data frame para el cual se necesita modificar los nombres de las columnas 
  
  Regresa:
    salaries_df (dataframe): el dataframe modificado
  """

  salaries_df.columns = salaries_df.columns.str.upper()
  return(salaries_df)
>>>>>>> 67b6144 ([Init][Feat] Inicialización de repositorio y adición de archivos de la librería Tech_Salaries.)



def download_data(path_file):
<<<<<<< HEAD
    #Descarga el dataset salaries desde Github hasta la carpeta especificada por el usuario

    #Parametros:
    #path_file (str): ruta de almacenamiento del archivo, junto con su nombre
    
    #Regresa:
    #path_file (str): la ruta donde fue almacenado con éxito el archivo junto con el nombre dle mismo

    location = pathlib.Path(path_file)
    folder = location.parent
    pathlib.Path(folder).mkdir(exist_ok=True)
    url = "https://raw.githubusercontent.com/colombia-dev/data/master/salaries/2020/raw.csv"
    r = requests.get(url, allow_redirects= True)
    with open(location, "wb") as f:
        f.write(r.content)
    return str(path_file)
=======
  """
  Descarga el dataset salaries desde Github hasta la carpeta especificada por el usuario

  Parámetros:
  path_file (str): ruta de almacenamiento del archivo, junto con su nombre
  
  Regresa:
  path_file (str): la ruta donde fue almacenado con éxito el archivo junto con el nombre dle mismo
  """

  location = pathlib.Path(path_file)
  folder = location.parent
  pathlib.Path(folder).mkdir(exist_ok=True)
  url = "https://raw.githubusercontent.com/colombia-dev/data/master/salaries/2020/raw.csv"
  r = requests.get(url, allow_redirects= True)
  with open(location, "wb") as f:
      f.write(r.content)
  return str(path_file)
>>>>>>> 67b6144 ([Init][Feat] Inicialización de repositorio y adición de archivos de la librería Tech_Salaries.)



def sel(salaries_df):
<<<<<<< HEAD
    #Crea  un dataframe con las columnas necesarias para comenzar la limpieza

    #Parametros: 
    #salaries_df (dataframe)

    #Regresa: 
    #salaries_df (dataframe): dataframe con las columnas seleccionadas 

    salaries_df = salaries_df[["¿A usted le pagan en pesos colombianos (COP) o dólares (USD)?",
                                    "¿Usando la moneda de la respuesta anterior, cuánto es su remuneración ANUAL base?  eg 36,000,000 si es pesos o 3,600 si es dólares"]]
    return(salaries_df)



def divide(salaries_df):
    #Crea  dos data frame separados para analizar quienen ganan en pesos y dólares


    #Parametros: 
    #salaries_df (dataframe)

    #Regresa: 
    #salaries_df_pesos (dataframe): dataframe con valores en peso
    #salaries_df_dolar (dataframe): dataframe con valores en peso

    salaries_df_pesos =  salaries_df.loc[salaries_df["¿A USTED LE PAGAN EN PESOS COLOMBIANOS (COP) O DÓLARES (USD)?"]== "pesos",:]
    salaries_df_dolar =  salaries_df.loc[salaries_df["¿A USTED LE PAGAN EN PESOS COLOMBIANOS (COP) O DÓLARES (USD)?"]== "dólares",:]

    return(salaries_df_pesos,salaries_df_dolar)
=======
  """
  Crea  un dataframe con las columnas necesarias para comenzar la limpieza

  Parametros: 
  salaries_df (dataframe)

  Regresa: 
  salaries_df (dataframe): dataframe con las columnas seleccionadas 
  """
  salaries_df = salaries_df[["¿A usted le pagan en pesos colombianos (COP) o dólares (USD)?",
                                  "¿Usando la moneda de la respuesta anterior, cuánto es su remuneración ANUAL base?  eg 36,000,000 si es pesos o 3,600 si es dólares"]]
  return(salaries_df)



def rename_columns(salaries_df, dicc):
  """
  Renombrar y acortar nombre de las columnas.

  Parámetros:
  salaries_df (dataframe)
  dicc (Diccionario cuya(s) llave(s) contiene(n) el/los nombre(s) actual(es) de la(s) columna(s) y su(s) valor(es) es/son el/los nombre(s) por el/los cual(es) se desea cambiar)
  
  Regresa:
  Dataframe con las columnas renombradas.
  """
  salaries_df = salaries_df.rename(dicc, axis="columns")
  return salaries_df


def divide(salaries_df):
  """
  Crea dos data frame separados para analizar quienen ganan en pesos y dólares


  Parametros: 
  salaries_df (dataframe)

  Regresa: 
  salaries_df_pesos (dataframe): dataframe con valores en peso
  salaries_df_dolar (dataframe): dataframe con valores en peso
  """
  salaries_df_pesos =  salaries_df.loc[salaries_df["MONEDA"]== "pesos",:]
  salaries_df_dolar =  salaries_df.loc[salaries_df["MONEDA"]== "dólares",:]

  return(salaries_df_pesos,salaries_df_dolar)


def box_plot(salaries_series):
  """
  Muestra la distribución de los datos donde la caja delimita los percentiles 25 al 75 (el 50% de la distribución) y los bigotes delimitan los puntos mínimo y máximo (rango).

  Parámetros:
  salaries_df (dataframe): dataframe en pesos o dólares.
  
  Regresa: 
  alt_chart (altair.vegalite.v4.api.Chart): Diagrama de bigotes de la serie que contiene la información salarial.


  """
  alt_chart = alt.Chart(pd.DataFrame(salaries_series)).mark_boxplot().encode(
    x='REMUNERACION ANUAL BASE:Q'
  )
  return alt_chart


def outliers_percent(moneda_df, col_name, fence_low, fence_high):
  """
  Calcula el porcentaje de los datos que se encuentran por fuera del rango salarial ingresado.

  Parámetros:
  moneda_df (dataframe): Dataframe en pesos o dólares.
  col_name (string): Cadena con el nombre de la columna que contiene los valores de salario.
  fences (Tuple of floats) límites inferior y superior estimados para los valores de ingresos. 

  Regresa: 
  diferencia (float): Número flotante del porcentaje aproximado a una cifra decimal. 
  """
  actual = moneda_df.loc[(moneda_df[col_name]>fence_low) & (moneda_df[col_name]<fence_high), col_name].count()
  total =  moneda_df.loc[:, col_name].count()
  diferencia = round(((total - actual) / total)* 100, 1)
  return diferencia 


def remove_outliers(moneda_df, col_name, fence_low, fence_high):
  """
  Remueve los valores extremos (menores que el límite inferior y mayores que el límite superior) que afectan el valor esperado en la columna del dataframe ingresado.

  Parámetros:
  moneda_df (dataframe): Dataframe de salarios. 
  col_name (string): Cadena con el nombre de la columna que contiene los valores de salario.
  fence_low (float): Número flotante con el valor límite inferior. 
  fence_high (float): Número flotante con valor límite superior.

  Regresa:
  no_outliers_df (dataframe): Dataframe cuyos valores mínimo y máximo de la columna de salarios corresponden a los valores límites inferior y superior respectivamente.
  """
  no_outliers_df = moneda_df.loc[(moneda_df[col_name] >= fence_low) & (moneda_df[col_name] <= fence_high), :]
  return no_outliers_df  


def standarization(moneda_df, col_name):
  """
  Normalización de los datos restando la media y dividiendo por la desviación estándar cada uno de los valores de la columna y el dataframe ingresados.

  Parámetros:
  moneda_df (DataFrame): Dataframe salarial.
  col_name (String): Cadena con el nombre de la columna que contiene los valores de salario.

  Regresa:
  moneda_df (dataframe): Dataframe salarial con una nueva columna que contiene los datos de los salarios normalizados.
  """
  serie = moneda_df.loc[:, col_name]
  mean = serie.mean()
  std = np.std(serie)
  std_serie = (serie - mean)/std
  moneda_df["REMUNERACION ANUAL BASE NORMALIZADA"] = std_serie
  return moneda_df


def dist_hist(moneda_df, col_name, bins=10):
  """
  Grafica un histograma y una distribución de los datos de la columna ingresada.

  Parámetros:
  moneda_df (dataframe): Dataframe salarial.
  col_name (string): Cadena con el nombre de la columna que contiene los valores de salario.

  Regresa:
  Un histograma con el número de bins ingresado o diez por defecto, con una gráfica superpuesta de la distribución de los datos ingresados.
  """
  Y = pd.Series(moneda_df[col_name], name=col_name)
  moneda = moneda_df.iloc[1, 0].upper()
  plot_name = "HISTOGRAMA Y DISTRIBUCION DE PROBABILIDAD DE " + col_name.upper() + " EN " + moneda
  fig, ax = plt.subplots()
  sns.distplot(Y, bins=bins, color="g", ax=ax)
  plt.xlabel(col_name.upper() + " EN " + moneda)
  plt.title(plot_name, pad=20)
  return plt.show()


  
>>>>>>> 67b6144 ([Init][Feat] Inicialización de repositorio y adición de archivos de la librería Tech_Salaries.)
