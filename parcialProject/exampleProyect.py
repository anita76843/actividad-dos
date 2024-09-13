
# conversion de entero a cadena
numero_entero = 10
cadena_entero = str(numero_entero)
print(f"Convertir entero a cadena: {cadena_desde_entero} (tipo: {type(cadena_desde_entero)})")

# convesion de decimal a cadena
decimal = 3.14
cadena_decimal = str(decimal)
print(f"Convertir decimal a cadena: {cadena_desde_decimal} (tipo: {type(cadena_desde_decimal)})")

# conversion de cadena a entero
cadena = "123"
entero_cadena = int(cadena)
print(f"Convertir cadena a entero: {entero_desde_cadena} (tipo: {type(entero_desde_cadena)})")

# Convertersion de cadena a decimal
cadena_decimal = "45.67"
decimal_desde_cadena = float(cadena_decimal)
print(f"Convertir cadena a decimal: {decimal_desde_cadena} (tipo: {type(decimal_desde_cadena)})")

# Multilíneas de cadenas
cadena_multilinea = """Esta es una cadena
que ocupa múltiples
líneas."""
print("Cadena multilínea:")
print(cadena_multilinea)

# Función len()
longitud_cadena = len(cadena_multilinea)
print(f"La longitud de la cadena multilínea es: {longitud_cadena}")

# Subcadenas
cadena_ejemplo = "Hola, Mundo"

# Obtener los primeros n caracteres
n = 5
primer_n_caracter = cadena_ejemplo[:n]
print(f"Primeros {n} caracteres: {primer_n_caracter}")

# Obtener los caracteres de en medio
inicio_medio = 2
fin_medio = 8
caracteres_medio = cadena_ejemplo[inicio_medio:fin_medio]
print(f"Caracteres de en medio ({inicio_medio}-{fin_medio}): {caracteres_medio}")

# Obtener los últimos n caracteres
ultimos_n_caracteres = cadena_ejemplo[-n:]
print(f"Últimos {n} caracteres: {ultimos_n_caracteres}")

# Función upper()
cadena_mayusculas = ejemplo.upper()
print(f"Cadena en mayúsculas: {cadena_mayusculas}")

# Función lower()
cadena_minusculas = c_ejemplo.lower()
print(f"Cadena en minúsculas: {cadena_minusculas}")

# Multilíneas de cadenas de caracteres
cadena_multilinea_2 = """Primera línea
Segunda línea
Tercera línea"""
print("Otra cadena multilínea:")
print(cadena_multilinea_2)

# Función strip()
con_espacios = "   Texto con espacios alrededor   "
sin_espacios = con_espacios.strip()
print(f"Cadena original: '{con_espacios}'")
print(f"Cadena sin espacios: '{sin_espacios}'")

# Función replace()
cadena_reemplazo = cadena_ejemplo.replace( "Hola", "Adiós")
print(f"Cadena después de replace: {cadena_reemplazo}")

# Función split()
cadena_a_dividir = "uno,dos,tres,cuatro"
lista_dividida = cadena_a_dividir.split(',')
print(f"Cadena dividida en lista: {lista_dividida}")

# Formato de cadenas F-String
nombre = "ana"
edad = 25
print(f"Hola, me llamo {nombre} y tengo {edad} años.")


