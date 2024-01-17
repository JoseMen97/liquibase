import yaml
import sys
import shutil

archivo_origen = 'changeset_base.yaml'

with open('output.txt', 'r') as file:
    # Itera sobre cada línea del archivo
    for line in file:
        # Imprime cada línea
        archivo_destino = f'changeset_new_{line.strip()}.yaml'
        shutil.copy(archivo_origen, archivo_destino)
        
# # Ruta del archivo YAML
# archivo_yaml = sys.argv[1]

# # Leer el contenido del archivo YAML
# with open(archivo_yaml, 'r') as file:
#     contenido = yaml.safe_load(file)

# # Modificar la línea específica
# contenido['databaseChangeLog'][0]['changeSet']['id'] = sys.argv[2]
# contenido['databaseChangeLog'][0]['changeSet']['author'] = sys.argv[3]
# contenido['databaseChangeLog'][0]['changeSet']['changes'][0]['sqlFile']['path'] = sys.argv[4]

# # contenido[sys.argv[2]] = sys.argv[3]

# # Escribir el contenido modificado de vuelta al archivo YAML
# with open(archivo_yaml, 'w') as file:
#     yaml.dump(contenido, file, default_flow_style=False)
