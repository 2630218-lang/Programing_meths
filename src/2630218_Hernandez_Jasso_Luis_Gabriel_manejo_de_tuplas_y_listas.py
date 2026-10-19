# ============================================================
# COLLECTIONS IN PYTHON
# ============================================================
#
# COVER PAGE
#
# Student name: Luis Gabriel Hernandez Jasso
# Matricula: 2630218
# Group: 1
# Materia: Metodologias de la programacion
#
# ============================================================
# EXECUTIVE SUMMARY
# ============================================================
"""
 Python provides different types of collections for storing data.
 A list is an ordered and mutable collection, so its elements can change.
 A tuple is also ordered, but it is immutable after it is created.
 A dictionary stores information using keys associated with values.
 Lists are useful when elements need to be added, removed, or updated.
 Tuples are useful for information that should remain unchanged.
 Dictionaries are useful when information needs to be searched by a key.
 This program contains six problems that use lists, tuples, dictionaries,
 validations, searches, calculations, and different collection operations.
"""
# ============================================================
# PRINCIPLES AND GOOD PRACTICES
# ============================================================

"""
 Lists should be used when elements need to be added or removed frequently.
 Tuples are useful for values that should not change, such as coordinates.
 Dictionaries are useful when information needs to be found using a key.
 A list should not normally be modified while it is being traversed.
 Dictionary keys should have clear and descriptive names.
 Input data should always be validated before processing.
 Empty lists should be checked before calculating averages or other values.
 Variable names and messages should be clear and easy to understand.
"""

# ============================================================
# PROBLEM 1: SHOPPING LIST BASICS
# ============================================================
#
# Description:
# This program creates a shopping list from products entered by the user.
# It adds a new product to the end of the list and checks whether another
# product is contained in the list.
#
# Inputs:
# - initial_items_text (string)
# - new_item (string)
# - search_item (string)
#
# Outputs:
# - "Items list: <items_list>"
# - "Total items: <len_list>"
# - "Found item: true|false"
#
# Validations:
# - initial_items_text cannot be empty after strip().
# - new_item cannot be empty.
# - search_item cannot be empty.
# - Empty elements between commas are ignored.
#
# Test cases:
# 1) Normal:
#    Initial items: "apple,banana,orange"
#    New item: "milk"
#    Search item: "banana"
#    Found item: true
#
# 2) Border:
#    Initial items: "apple"
#    New item: "bread"
#    Search item: "bread"
#    Found item: true
#
# 3) Error:
#    Initial items: "   "
#    Output: "Error: invalid input"
#
# Key operations:
# split(), strip(), append(), len(), in
# ============================================================

initial_items_text = input("Enter initial items separated by commas: ").strip()

if initial_items_text == "":
    print("Error: invalid input")

else:
    initial_parts = initial_items_text.split(",")
    items_list = []

    # Remove extra spaces and ignore empty items
    for item in initial_parts:
        clean_item = item.strip().lower()

        if clean_item != "":
            items_list.append(clean_item)

    if len(items_list) == 0:
        print("Error: invalid input")

    else:
        new_item = input("Enter a new item: ").strip().lower()
        search_item = input("Enter an item to search: ").strip().lower()

        if new_item == "" or search_item == "":
            print("Error: invalid input")

        else:
            # Add a new item to the list
            items_list.append(new_item)

            # Search for the item
            is_in_list = search_item in items_list

            print(f"Items list: {items_list}")
            print(f"Total items: {len(items_list)}")
            print(f"Found item: {str(is_in_list).lower()}")


# ============================================================
# PROBLEM 2: POINTS AND DISTANCES WITH TUPLES
# ============================================================
#
# Description:
# This program uses tuples to represent two points in a 2D plane.
# It calculates the distance between the points and creates a new
# tuple containing the midpoint.
#
# Inputs:
# - x1 (float)
# - y1 (float)
# - x2 (float)
# - y2 (float)
#
# Outputs:
# - "Point A: <point_a>"
# - "Point B: <point_b>"
# - "Distance: <distance>"
# - "Midpoint: <midpoint>"
#
# Validations:
# - All four values must be convertible to float.
# - Negative coordinates are allowed.
#
# Test cases:
# 1) Normal:
#    Point A: (0, 0)
#    Point B: (3, 4)
#    Distance: 5.0
#    Midpoint: (1.5, 2.0)
#
# 2) Border:
#    Point A: (2, 2)
#    Point B: (2, 2)
#    Distance: 0.0
#
# 3) Error:
#    Input: x1 = "hello"
#    Output: "Error: invalid input"
#
# Key operations:
# tuple creation, indexing, **, arithmetic operations
# ============================================================

try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    # Create tuples
    point_a = (x1, y1)
    point_b = (x2, y2)

    # Calculate distance
    distance = (
        (x2 - x1) ** 2
        + (y2 - y1) ** 2
    ) ** 0.5

    # Calculate midpoint
    midpoint = (
        (x1 + x2) / 2,
        (y1 + y2) / 2
    )

    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {round(distance, 2)}")
    print(f"Midpoint: {midpoint}")

except ValueError:
    print("Error: invalid input")


"""
7.4 Problem 4: Student grades with dict and list
--------------------------------------------------

Descripción:
Administra las calificaciones de un grupo usando un diccionario:
- clave: nombre del estudiante (string)
- valor: lista de calificaciones (list of float)
El programa debe:
1) Crear un diccionario con al menos 3 estudiantes, cada uno con una lista de calificaciones.
2) Leer el nombre de un estudiante.
3) Calcular el promedio de sus calificaciones.
4) Indicar si el estudiante está aprobado (average >= 70.0) con un booleano is_passed.

Entradas:
- student_name (string).

Salidas:
- Si el estudiante existe:
  - "Grades:" <grades_list>
  - "Average:" <average>
  - "Passed:" true|false
- Si el estudiante no existe:
  - "Error: student not found"

Validaciones:
- student_name no vacío tras strip().
- Verificar si student_name es una clave en el diccionario.
- Verificar que la lista de calificaciones no esté vacía antes de calcular el promedio.

Operaciones clave sugeridas:
- Diccionario de listas: grades = {"Alice": [90, 85], ...}
- sum(), len() para promedio.
- in para verificar clave.

--------------------------------------------------
7.5 Problem 5: Word frequency counter (list + dict)
--------------------------------------------------

Descripción:
Cuenta la frecuencia de cada palabra en una oración usando:
- Una lista de palabras.
- Un diccionario donde:
  - clave: palabra (string)
  - valor: frecuencia (int)
El programa debe:
1) Leer una oración.
2) Convertirla a minúsculas y separarla en una lista de palabras.
3) Construir un diccionario de frecuencias.
4) Mostrar el diccionario completo y la palabra más frecuente.

Entradas:
- sentence (string).

Salidas:
- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word> (si hay empate, cualquier una es válida)

Validaciones:
- sentence no vacía tras strip().
- Manejar signos de puntuación simples si el estudiante decide hacerlo (documentar su decisión, por ejemplo usando replace()).
- Verificar que la lista de palabras no esté vacía.

Operaciones clave sugeridas:
- lower(), split()
- Recorrer la lista y actualizar el diccionario:
  - if word in freq_dict: freq_dict[word] += 1
  - else: freq_dict[word] = 1
- Uso de un ciclo para encontrar la palabra con mayor frecuencia.

--------------------------------------------------
7.6 Problem 6: Simple contact book (dictionary CRUD)
--------------------------------------------------

Descripción:
Implementa un mini "contact book" usando un diccionario donde:
- clave: nombre de contacto (string)
- valor: número de teléfono (string)
El programa debe:
1) Crear un diccionario inicial con algunos contactos.
2) Leer una acción action_text ("ADD", "SEARCH" o "DELETE").
3) Según la acción:
   - "ADD": lee name y phone, agrega o actualiza el contacto.
   - "SEARCH": lee name y muestra el teléfono si existe.
   - "DELETE": lee name y elimina el contacto si existe.
4) Mostrar un mensaje indicando el resultado de la operación.

Entradas:
- action_text (string; "ADD", "SEARCH" o "DELETE").
- name (string; depende de la acción).
- phone (string; solo para "ADD").

Salidas:
- Para "ADD":
  - "Contact saved:" name, phone
- Para "SEARCH":
  - Si existe: "Phone:" <phone>
  - Si no existe: "Error: contact not found"
- Para "DELETE":
  - Si existe: "Contact deleted:" name
  - Si no existe: "Error: contact not found"

Validaciones:
- Normalizar action_text a mayúsculas.
- Verificar que action_text sea una de las tres opciones válidas.
- name no vacío tras strip().
- Para "ADD": phone no vacío tras strip().

Operaciones clave sugeridas:
- Diccionario: contacts = {"Alice": "1234567890", ...}
- get(), in, pop()
- Estructura if/elif para manejar cada acción.
"""
# ============================================================
# CONCLUSIONS
# ============================================================
"""
 Lists, tuples, and dictionaries are useful for organizing different
 types of information in Python programs.
 Lists are flexible because elements can be added, removed, or changed.
 Tuples are useful for information that should remain unchanged,
 such as coordinates representing points in a plane.
 Dictionaries make it easy to associate a key with a value and
 search for information using that key.
 Combining dictionaries and lists allows more complex information,
 such as storing several grades for each student.
 I also learned that validating collections before using them helps
 prevent errors when searching, calculating averages, or accessing data.
"""

# ============================================================
# REFERENCES
# ============================================================
#
# 1. Python Software Foundation.
#    Built-in Types.
#    https://docs.python.org/3/library/stdtypes.html
#
# 2. Python Software Foundation.
#    Data Structures.
#    https://docs.python.org/3/tutorial/datastructures.html
#
# 3. Python Software Foundation.
#    Lists.
#    https://docs.python.org/3/tutorial/introduction.html#lists
#
# 4. Python Software Foundation.
#    Built-in Functions.
#    https://docs.python.org/3/library/functions.html
#
# 5. Python Software Foundation.
#    More Control Flow Tools.
#    https://docs.python.org/3/tutorial/controlflow.html
#
