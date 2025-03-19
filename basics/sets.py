'''
CONJUNTOS
* Se puede modificar
* Permite varios tipos de datos
* No tienen un orden
* No permite duplicados, los elimina automáticamente
'''

# Creando un conjunto con diversos tipos de datos y duplicados
set_types = {1, 'hola', False, 12.58, 'hola', 'Ejemplo set'}
print(f'Conjunto {set_types}')

# Creando conjunto a partir de otro elemento.
set_from_string = set('Andrés')
set_from_tuples = set(('abc', 'cvb', 'as'))

print(f'Conjunto creado a partir de un String: {set_from_string}')
print(f'Conjunto| creado a partir de una Tupla: {set_from_tuples}')

# Obteniendo valores únicos de una lista por medio de **set**
numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)  # Convirtiendo a conjunto
unique_numbers = list(set_numbers)  # Convirtiendo nuevamente a lista
print(f'Lista con valores únicos: {unique_numbers}')

# CRUD SETS
# Conteo
set_countries = {'CO', 'AR', 'CO', 'PY', 'BO', 'EC'}
size = len(set_countries)
print(f'Cantidad de elementos dentro del conjunto: {size}')

# Buscar un elemento
print(f"¿El país 'CO' está en el conjunto?: {'CO' in set_countries}")

# Agregando un elmento
set_countries.add('PE')
print(f"Páis 'PE' agregado {set_countries}")

# Update
set_countries.update({'cr', 'vz', 'es'})
print(f'Conjunto con países agregados: {set_countries}')

# Remove
set_countries.remove('vz')
set_countries.difference_update({'CO', 'BR'})
set_countries.clear()
for country in {'BO', 'PXY'}:
    # Es seguro usar discard porque no lanza error si el elemento no está en el conjunto (a diferencia de remove())
    set_countries.discard(country)

print(f"Eliminando 'vz' con 'remove' {set_countries}")
print(f"Eliminando 'CO' y 'BR' con 'difference': {set_countries}")  # BR no existe
print(f"Eliminando 'BO' y 'PXY' con 'discard' en un loop: {set_countries}")
print(f"Eliminando todos los elementos con 'clear': {set_countries}")

# Operaciones entre conjuntos
set_a = {'col', 'mex', 'bol'}
set_b = {'bol', 'pe'}

set_union_ab = set_a.union(set_b)
print(f"Unión de 'conjunto' A y B: {set_union_ab}")
print(f"Unión usando el operador | : {(set_a | set_b)}")

set_intersect_ab = set_a.intersection(set_b)
print(f"Intersección de 'conjunto' A y B: {set_intersect_ab}")
print(f"Intersección usando el operador & : {(set_a & set_b)}")

set_diff_ab = set_a.difference(set_b)
print(f"Diferencia de 'conjunto' A y B: {set_diff_ab}")
print(f"Diferencia usando el operador -: {(set_a - set_b)}")    # Se exluyen los elementos de b que está en a

set_diffsimetrica_ab = set_a.symmetric_difference(set_b)
print(f"Diferencia simétrica entre A y B: {set_diffsimetrica_ab}")
print(f"Diferencia simétrica entre A y B con operador ^ {(set_a ^ set_b)}") # Se exluyen los elementos en común

# EJERCICIO PRÁCTICO
# Escribir un algoritmo que elimine los elementos repetidos para obtener un conjunto único llamado new_set.
countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
new_set = countries | northAm | centralAm | southAm
print(new_set)