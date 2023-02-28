import re

id = re.compile('[a-zA-Z]+([a-zA-Z]+[\d])*') #Identificadores

float = re.compile('[\d]+\.[\d]+') #Reales

linea = []

while (linea != '!'):
        linea = input("Ingrese la cadena: ")
        tokens=linea.split(' ')
        print("Los tokens son ", tokens)
        for token in tokens:     
            if id.match(linea):
                print (token, "<< es un identificador (tipo: 0)")
            elif float.match(linea):
                print (token, "<< es un real (tipo: 2)")
        print("----------------------------------------------------------")