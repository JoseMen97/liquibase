import yaml
import sys
import shutil

archivo_origen = 'changeset_base.yaml'

# with open('output.txt', 'r') as file:
#     # Itera sobre cada línea del archivo
#     for line in file:
#         # Imprime cada línea
#         partes = line.strip().split("/")
#         name = partes[-1]
#         archivo_destino = f'{name}_changeset_new.yaml'
#         shutil.copy(archivo_origen, archivo_destino)

#         archivo_yaml = archivo_destino

#         # Leer el contenido del archivo YAML
#         with open(archivo_yaml, 'r') as file:
#             contenido = yaml.safe_load(file)

#         # Modificar la línea específica
#         contenido['databaseChangeLog'][0]['changeSet']['id'] = sys.argv[1]
#         contenido['databaseChangeLog'][0]['changeSet']['author'] = sys.argv[2]
#         path = f'../{line.strip()}'
#         contenido['databaseChangeLog'][0]['changeSet']['changes'][0]['sqlFile']['path'] = path
        
#         with open(archivo_yaml, 'w') as file:
#             yaml.dump(contenido, file, default_flow_style=False)


for line in sys.argv[3]:
    # Imprime cada línea
    partes = line.split("/")
    name = partes[-1]
    archivo_destino = f'{name}_changeset_new.yaml'
    shutil.copy(archivo_origen, archivo_destino)

    archivo_yaml = archivo_destino

    # Leer el contenido del archivo YAML
    with open(archivo_yaml, 'r') as file:
        contenido = yaml.safe_load(file)

    # Modificar la línea específica
    contenido['databaseChangeLog'][0]['changeSet']['id'] = sys.argv[1]
    contenido['databaseChangeLog'][0]['changeSet']['author'] = sys.argv[2]
    path = f'../{line}'
    contenido['databaseChangeLog'][0]['changeSet']['changes'][0]['sqlFile']['path'] = path
    
    with open(archivo_yaml, 'w') as file:
        yaml.dump(contenido, file, default_flow_style=False)
