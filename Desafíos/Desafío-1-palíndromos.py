## DESAFÍO 1: PALÍNDROMOS
# Un palíndromo es una palabra o frase que se lee igual de adelante hacia atrás que de atrás hacia
# adelante, ignorando los espacios, puntuación y capitalización. El desafío es crear un programa que
# tome una cadena ingresada por el usuario y determine si es un palíndromo.

diccionario_acentos= {
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ú': 'u',
    'ü': 'u'
}
def eliminar_acentos(palabra):
    palabra_sin_acentos = ''
    for letra in palabra:
        if letra in diccionario_acentos:
            palabra_sin_acentos += diccionario_acentos[letra]
        else:
            palabra_sin_acentos += letra
    return palabra_sin_acentos

def palindromo(palabra):
    # Limpieza inicial: minúsculas, sin acentos y sin espacios
    palabra = palabra.lower()
    palabra = eliminar_acentos(palabra)
    palabra = palabra.replace(' ', '')
    
    # Validación: verificar que solo contenga letras (rechaza símbolos y números)
    if not palabra.isalpha():
        print("Entrada no válida: solo se permiten letras (sin números ni símbolos).")
        return
        
    # Validación: verificar que tenga más de 1 letra
    if len(palabra) <= 1:
        print("Entrada no válida: debes ingresar al menos 2 letras.")
        return

    # Comprobación del palíndromo
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        print("La palabra o frase es un palíndromo")
    else:
        print("La palabra o frase no es un palíndromo")

## Ciclo de ejecución de detección de palíndromo con respueta de usuario

while True:
  entrada_usuario = input("Ingresa una palabra o frase para verificar si es un palíndromo: ")
  palindromo(entrada_usuario)
  print("-" * 40)  

  # Bucle para asegurar que responda S o N válidos
  while True:
    salir = input("¿Quiere ingresar otra palabra (S/N)?: ")
    if salir.lower() == "n":
      print("¡Hasta luego!")
      break
    elif salir.lower() == "s":
      print("-" * 40)  
      break
    else:
      print("El valor ingresado no es válido. Por favor, introduce S o N.")

  # Si eligió salir (N), rompemos el bucle principal
  if salir.lower() == "n":
    break