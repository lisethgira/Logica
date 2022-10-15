"""print("Hello world")

suma = 4 + 10 
print(suma)

x = 5
y = 10
z = x + y 
print ("el resultado es : ", z)"""

# ejercio Rutina Diaria enfocado en la función necesidades 

"""print("abrir los ojos")
print("sentarse en la cama")
print("caminar al baño")
print("hacer necesidades")
print("salir para el trabajo")"""



tipo_necesidad = 1
genero = "mujer"

def hacer_necesidades(tipo_necesidad,genero):
    print("Entrar al baño")
    print("bajarse interiores")
    if tipo_necesidad == 1:
        if genero == "mujer":
            print("sentarse en el toilet")
        else:
            print("hacese en frente")
    else:
        print("sentarse en el toilet")
print("abrir los ojos")
print("sentarse en la cama")
print("caminar al baño")
hacer_necesidades(tipo_necesidad, genero)
print("salir para el trabajo")



