# SET significa grupo o conjunto
primer = {1,1,2,2,3,3,4,4}

print(primer)

lista = [3,4,5,6,7,8,9]

segunda = set(lista)
print(segunda)

# Muestra todos los elementos diferentes de ambas tuplas
print(primer | segunda)
# Muestra solo los elementos que coninciden en ambas tuplas
print(primer & segunda)
# Muestra solo los elementos de la primer tupla, quitando todos los que coinciden con la segunda
print(primer - segunda)
# Diferencia simétrica, solo muestra los elementos que no coinciden entre ambas listas
print(primer ^ segunda)