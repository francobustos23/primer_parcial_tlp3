"""
Little Petya ama los regalos. Su mamá le compró dos cadenas del mismo tamaño para
su cumpleaños. Las cadenas consisten en letras latinas mayúsculas y minúsculas.
Ahora Petya quiere comparar esas dos cadenas lexicográficamente. No importa si las
letras están en mayúsculas o minúsculas. Ayuda a Petya a realizar la comparación.

(Ordenar algo lexicográficamente significa organizar elementos alfabéticamente, de
la misma forma que se listan las palabras en un diccionario)

Especificaciones de la Función:
Nombre de la función:
● El nombre de la función debe ser: comparar_cadenas_lexicograficas
Parámetros:
● cadena1 (str): La primera cadena a comparar.
● cadena2 (str): La segunda cadena a comparar.

Retorno:
● Si la primera cadena es menor que la segunda, retornar "-1".
● Si la segunda cadena es menor que la primera, retornar "1".
● Si las cadenas son iguales, retornar "0".
Ejemplo
● Si tenemos las cadenas "abc" y "abd", al compararlas lexicográficamente, la
cadena "abc" sería considerada menor que "abd", ya que en la tercera posición
la letra "c" tiene un valor ASCII menor que "d".

"""
def comparar_cadenas_lexicograficas(cadena1:str, cadena2:str):
    #Ordenamos las cadenas lexicográficamente
    cadena1 = cadena1.lower()
    cadena2 = cadena2.lower()
    #Si la cadena1 es menor que la segunda retorna "-1"
    if(cadena1 < cadena2):
        return "-1"
    #Si la cadena2 es menor a la primera retorna "1"
    elif(cadena1 > cadena2):
        return "1"
    #Si las cadenas son iguales retorna "0"
    else:
        return "0"

print(comparar_cadenas_lexicograficas("aaaabbbsse", "kssdwas"))  
