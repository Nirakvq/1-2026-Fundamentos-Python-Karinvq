import pandas

datos = pandas.read_csv('clase08/Estudiantes (1).csv')

print(datos.head())

print(datos.describe())

print(datos[["nombre", "apellido"]].head())

print(datos.describe())

#hay una funcion que se llama max() y devuelve el valor maximo de una columna
print(datos["edad"].max())

#hay una funcion que se llama min() y devuelve el valor minimo de una columna
print(datos["edad"].min())

estudiantes_alta_notas = datos[datos["nota"] > 85]
print(estudiantes_alta_notas)

# Agrupar datos es para unir los datos por una columna y aplicar una función a cada grupo
# Agrupar y saca la media de todos los datos de un grupo que se le pida y devuelve un nuevo dataframe con la media de cada grupo
media_por_sexo = datos.groupby("sexo")["nota"].mean()
print(media_por_sexo)
