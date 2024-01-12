import yaml

# Ruta del archivo YAML
archivo_yaml = sys.argv[1]

# Leer el contenido del archivo YAML
with open(archivo_yaml, 'r') as file:
    contenido = yaml.safe_load(file)

# Modificar la línea específica
contenido[sys.argv[2]] = sys.argv[3]

# Escribir el contenido modificado de vuelta al archivo YAML
with open(archivo_yaml, 'w') as file:
    yaml.dump(contenido, file, default_flow_style=False)
