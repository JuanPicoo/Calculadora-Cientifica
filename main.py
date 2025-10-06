def suma(a, b):
    total = a + b
    return total
def resta(a, b):
    total = a - b
    return total
def multiplicacion (a, b):
    total = a * b
    return total
def division(a, b):
    if b != 0:
        total = a / b
        return total
def exponencial(a,b):
    total = a ** b
    return total

def modulo(a,b):
    total = a * b
    return a % b
        
print("--------Bienvenido---------")
f=True

while(f):
    print("1. Suma / 2. Resta / 3. Multiplicacion / 4. Division / 5. Exponencial / 6. Modulo / 7.Fin")

    a = int(input("Ingresa el primer numero: "))
    b = int(input("Ingresa el segundo numero: "))

    op=int(input("¿Que operacion usaras?: "))
    if op==7:
        f=False
        break
    if op==1:
        print("Resultado suma:  ", suma(a,b))
    elif op==2:
        print("Resultado resta:  ", resta(a,b))
    elif op==3:
        print("Resultado multipliacion:  ", multiplicacion(a,b))
    elif op==4:
        print("Resultado division:  ", division(a,b))
    elif op==5:
        print("Resultado Exponencial", exponencial(a,b))
    elif op==6:
        print("Resultado Modulo", modulo(a,b))
    else:
        print("Opcion inexistente")