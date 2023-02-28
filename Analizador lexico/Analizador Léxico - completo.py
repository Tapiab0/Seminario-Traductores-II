import re

cadena = re.compile('\"+[a-zA-Z]+[a-zA-Z]+\"') #Token de cadena
id = re.compile('[a-zA-Z]+([a-zA-Z]+[\d])*') #Token de identificador
float = re.compile('[\d]+\.[\d]+') #Token de real
int = re.compile('[\d]') #Token de enteros


Operadores = {'+' : 'OpSuma (tipo: 5)', '-' : 'OpRest (tipo: 5)',
              '*' : 'OpMul (tipo: 6)', '/' : 'OpDiv (tipo: 6)',
              '<' : 'OpRelac (tipo: 7)', '<=' : 'OpRelac (tipo: 7)', '>' : 'OpRelac (tipo: 7)', '>=' : 'OpRelac (tipo: 7)',
              '||' : 'OpOr (tipo: 8)',
              '&&' : 'OpAnd (tipo: 9)',
              '!' : 'OpNot (tipo: 10)',
              '==' : 'OpIgualdad (tipo: 11)', '!=' : 'OpIgualdad (tipo: 11)'}
Operadores_key = Operadores.keys() #Token de operadores

Reservadas = {'if' : '19)',
              'while' : '20)',
              'return' : '21)',
              'else' : '22)',
              'int' : '4)',
              'float' : '4)',
              'void' : '4)'}
Reservadas_key = Reservadas.keys() #Token de palabras reservadas


Simbolos = {';' : '12)',
            ',' : '13)',
            '(' : '14)',
            ')' : '15)',
            '{' : '16)',
            '}' : '17)',
            '=' : '18)',
            '$' : '23)'}
Simbolos_key = Simbolos.keys() #Diccionario de simbolos


linea = []

while (linea != '$'):
        linea = input("Ingresa la cadena: ")
        tokens=linea.split(' ')
        print("Los tokens son ", tokens)
        #Ciclo de lectura de tokens
        for token in tokens:     
            if token in Operadores_key:
                print(token, "<< Es un operador ", Operadores[token])
            elif token in Simbolos_key:
                print(token, "<< Es un simbolo (tipo:", Simbolos[token])
            elif token in Reservadas_key:
                print(token, "<< Es una palabra reservada (tipo: ", Reservadas[token])
            elif cadena.match(linea):
                print(token, "<< Es una cadena (tipo: 3)")
            elif float.match(linea):
                print(token, "<< Es un real (tipo: 2)")
            elif int.match(linea):
                print(token, "<< Es un entero (tipo: 1)") 
            elif id.match(linea):
                print (token, "<< Es un identificador (tipo: 0)")
            
        print("----------------------------------------------------------")
print("Los tokens son ", tokens)
print("Cierre de ejecucion")