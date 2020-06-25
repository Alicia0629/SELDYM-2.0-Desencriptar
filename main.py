import numpy

informacion=[]

abecedario=[]
for i in range(0,256):
    abecedario.append(chr(i))

mensaje7=input('mensaje cifrado: ')

clave=[]
for i in input('contraseña: '):
    clave.append(abecedario.index(i))


clave3lista=False
clave3=[]
claveternaria=[]

informacion.append('Clave en numeros ascii:')
informacion.append(clave)

for i in range(len(clave)):
    claveternaria.append('')
    for j in range(5,-1,-1):
        claveternaria[i]+= str(clave[i] // (3**j))
        clave[i] %= 3**j

claveternariainicial=claveternaria

while clave3lista==False: #obtencion de la clave3
    informacion.append('Clave en ternario:')
    informacion.append(claveternaria)
    clavesecuencia=''
    for i in claveternaria:
        añadido=False
        for j in range(5, -1, -1):
            if i[j] != '0' and añadido==False:
                clavesecuencia += '1' + i[:j] + str(int(i[j])-1) + ('2'*(5-j))
                añadido=True
        if añadido==False:
            clavesecuencia+= '022222'
    del claveternaria
    claveternaria=[]
    while len(clavesecuencia) % 6 != 0:
        clavesecuencia+='0'
    for i in range(len(clavesecuencia)//6):
        claveternaria.append(clavesecuencia[i*6:i*6+6])
    if len(clavesecuencia)//4 >= len(mensaje7)*2 and clave3lista==False: #clave 3
        for i in range(len(mensaje7)):
            clave3.append([1,1])
            for j in range(4):
                clave3[i][0]+=int(clavesecuencia[(i*4)+j]) * (3**(3-j))
                clave3[i][1]+=int(clavesecuencia[(len(mensaje7)*4)+((i*4)+j)]) * (3**(3-j))
            clave3.insert(i, (clave3[i][0]*clave3[i][1])%97)
            clave3.remove(clave3[i+1])
        clave3lista=True
    
informacion.append('Clave 3:')
informacion.append(clave3)

#obtencion del mensaje 6

mensaje6=[]
mensaje7numeros=[]

for i in mensaje7:
    mensaje7numeros.append(abecedario.index(i))
    if abecedario.index(i)>126:
        mensaje6.append(abecedario.index(i)-69)
    else:
        mensaje6.append(abecedario.index(i)-34)

informacion.append('Mensaje 7:')
informacion.append(mensaje7numeros)

informacion.append('Mensaje 6:')
informacion.append(mensaje6)

#obtencion del mensaje 5 desencriptando el mensaje 6 con la clave 3

tabla96=[]
archivo96=open('tabla96caracteres.txt','r')
for i in archivo96:
    tabla96.append([])
    for j in i.split('\n')[0].split(','):
        tabla96[-1].append(int(j))
archivo96.close()
mensaje5=[]

for i in range(len(clave3)):
    mensaje5.append(tabla96[clave3[i]-1].index(mensaje6[i])+1)

informacion.append('Mensaje 5:')
informacion.append(mensaje5)

#calculamos cuantos caracteres tenia el mensaje inicial y el espacio que estos ocupan en el mensaje final

longitud_mensaje1=0

for i in range(len(mensaje5[mensaje5.index(89)+1:])):
    longitud_mensaje1 += (44**(len(mensaje5[mensaje5.index(89)+1:])-1-i))*mensaje5[len(mensaje5[:mensaje5.index(89)]) + i + 1]


informacion.append('Número de carácteres del mensaje antes de ser encriptado:')
informacion.append(longitud_mensaje1)

cifras=[]
numero_de_caracteres_restantes= len(mensaje5[:mensaje5.index(89)])

for i in range(longitud_mensaje1,0,-1):
    cifras.append(numero_de_caracteres_restantes//i)
    numero_de_caracteres_restantes -= cifras[-1]

informacion.append('Cuantos carácteres ocupará cada letra del mensaje inicial:')
informacion.append(cifras)

#obtencion del mensaje 4a
mensaje4a=[]

for i in range(longitud_mensaje1):
    mensaje4a.append([])
    for j in range(cifras[i]):
        mensaje4a[i].append(mensaje5[j+sum(cifras[:i])]-1)

informacion.append('Mensaje 4a:')
informacion.append(mensaje4a)

#numeros negativos y en el mensaje 4b
mensaje4b=[]
negativos=[]

for i in range(len(mensaje4a)):
    if mensaje4a[i][0]<44:
        mensaje4b.append(mensaje4a[i])
    else:
        negativos.append(i)
        mensaje4b.append([])
        for j in mensaje4a[i]:
            mensaje4b[-1].append(j-44)

informacion.append('Posición en la que se encontraban los números negativos en el mensaje 4:')
informacion.append(negativos)

informacion.append('Mensaje 4b:')
informacion.append(mensaje4b)

#obtencion mensaje 4c

mensaje4c=[]

for i in mensaje4b:
    mensaje4c.append(0)
    for j in range(len(i)):
        mensaje4c[-1] += i[j] * (44**(len(i)-1-j))

informacion.append('Mensaje 4c:')
informacion.append(mensaje4c)

#obtencion mensaje 4d

mensaje4d=[]

for i in range(len(mensaje4c)):
    if i not in negativos:
        mensaje4d.append(mensaje4c[i])
    else:
        mensaje4d.append(0-mensaje4c[i])

informacion.append('Mensaje 4d:')
informacion.append(mensaje4d)

#obtencion del mensaje 3

mensaje3=[]

for i in range(len(mensaje4d)):
    mensaje3.append(mensaje4d[i] // ((44**(cifras[i])-1)//(256*len(mensaje4d))))

informacion.append('Mensaje 3:')
informacion.append(mensaje3)

#obtencion de la clave 1 y la clave 2

clave1lista=False
clave2lista=False
clave1=[]
clave2=[]
claveternaria=claveternariainicial

while clave1lista==False or clave2lista==False:
    clavesecuencia=''
    for i in claveternaria:
        añadido=False
        for j in range(5, -1, -1):
            if i[j] != '0' and añadido==False:
                clavesecuencia += '1' + i[:j] + str(int(i[j])-1) + ('2'*(5-j))
                añadido=True
        if añadido==False:
            clavesecuencia+= '022222'
    del claveternaria
    claveternaria=[]
    while len(clavesecuencia) % 6 != 0:
        clavesecuencia+='0'
    for i in range(len(clavesecuencia)//6):
        claveternaria.append(clavesecuencia[i*6:i*6+6])
    if len(clavesecuencia)//5 >= len(mensaje3)*2 and clave1lista==False: #clave1
        for i in range(len(mensaje3)):
            clave1.append([1,1])
            for j in range(5):
                clave1[i][0]+=int(clavesecuencia[(i*5)+j]) * (3**(4-j))
                clave1[i][1]+=int(clavesecuencia[(len(mensaje3)*5)+((i*5)+j)]) * (3**(4-j))
            clave1.insert(i, (clave1[i][0]*clave1[i][1])%257)
            clave1.remove(clave1[i+1])
        clave1lista=True
    if len(clavesecuencia) > len(mensaje3)**2 and clave2lista==False: #clave2
        for i in range(len(mensaje3)):
            clave2.append([])
            for j in range(len(mensaje3)):
                if clavesecuencia[j+(i*len(mensaje3))] == '2':
                    clave2[-1].append(-1)
                else:
                    clave2[-1].append(int(clavesecuencia[j+(i*len(mensaje3))]))
        try: #puede ocurrir que se obtenga una matriz sin solucion, en este paso vamos a comprobar que nuestra matriz tiene solucion
            prueba_matriz=[]
            for i in range(len(mensaje3)):
                prueba_matriz.append(0)
                for j in range(len(mensaje3)):
                    prueba_matriz[i]+= range(1,len(mensaje3)+1)[j]*clave2[i][j]
            prueba_matriz_numeros=numpy.array(clave2)
            prueba_matriz_soluciones=numpy.array(prueba_matriz)
            prueba_incognitas=numpy.linalg.solve(prueba_matriz_numeros,prueba_matriz_soluciones)
            clave2lista=True
        except:
            informacion.append('Matriz erronea:')
            informacion.append(clave2)
            clave2=[]
    
informacion.append('Clave 1:')
informacion.append(clave1)
informacion.append('Clave 2:')
informacion.append(clave2)


#desencriptar el mensaje 3 mediante la clave 2, es decir resolviendo un sistema lineal de ecuaciones y obteniendo asi el menaje 2

matriz_numeros=numpy.array(clave2)
matriz_soluciones=numpy.array(mensaje3)
mensaje2=numpy.linalg.solve(matriz_numeros,matriz_soluciones)

informacion.append('Mensaje 2:')
informacion.append(mensaje2)

#obtenemos mensaje 1 desencriptando el mensaje 2 con la clave 1

tabla256=[]
archivo256=open('tabla256caracteres.txt','r')
for i in archivo256:
    tabla256.append([])
    for j in i.split('\n')[0].split(','):
        tabla256[-1].append(int(j))
archivo256.close()

mensaje1=[]

for i in range(len(clave1)):
    mensaje1.append(tabla256[clave1[i]-1].index(int(round(mensaje2[i])))+1)

informacion.append('Mensaje 1:')
informacion.append(mensaje1)

#convertimos el mensaje 1 en letras

mensaje_descifrado=''

for i in mensaje1:
    mensaje_descifrado += abecedario[i]

print('')
print('Mensaje descifrado:')
print(mensaje_descifrado)
print('')

if input('¿Quieres ver toda la informacion de la encriptación? [S/n]  ')=='S':
    for i in range(len(informacion)):
        print(informacion[i])
        if i%2==1:
            print('')
