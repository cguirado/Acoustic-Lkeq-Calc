#Daniel Barreno
#Fernando Gutierrez

import csv
import math
import json
import sy
if __name__ == '__main__':
    try:
        MODO = sys.argv[1]
    except:
        sys.exit("No olvide introducir interior o exterior como argumento al ejecutar el programa")
    DatosLAe = []
    DatosLCe = []
    DatosLAN = []
    DatosLCN = []
    NombreGuardado = "LKeq.txt"
    with open('LAeq.txt') as LAeqtxt:
        DatosLAeq = csv.reader(LAeqtxt)
        for line in DatosLAeq:
            DatosLAe.append(line)
    with open('LCeq.txt') as LCeqtxt:
        DatosLCeq = csv.reader(LCeqtxt)
        for line in DatosLCeq:
            DatosLCe.append(line)
    with open('LANoise.txt') as LANoisetxt:
        DatosLANoise = csv.reader(LANoisetxt)
        for line in DatosLANoise:
            DatosLAN.append(line)
    with open('LCNoise.txt') as LCeqtxt:
        DatosLCNoise = csv.reader(LCeqtxt)
        for line in DatosLCNoise:
            DatosLCN.append(line)

#Corregir LAeq

LAeKCorregidoLista = []
LAeKCorregidoA = []

Y = 0
X = 0

while (Y < len(DatosLAe)):
    while (X < len(str(DatosLAe[Y]).split(' '))):
        if X == 0 and len(str(DatosLAe[Y]).split(' ')) != 1:
            A = float(str(DatosLAe[Y]).split(' ')[X][2:])
            A = 10**(A/10)
            B = float(str(DatosLAN[Y]).split(' ')[X][2:])
            B = 10**(B/10)
            LAeKCorregido = int(10*math.log10(A-B)+0.5)
            LAeKCorregidoA.append(LAeKCorregido)
        if X == len(str(DatosLAe[Y]).split(' '))-1 and len(str(DatosLAe[Y]).split(' ')) != 1:
            A = float(str(DatosLAe[Y]).split(' ')[X][:-2])
            A = 10**(A/10)
            B = float(str(DatosLAN[Y]).split(' ')[X][:-2])
            B = 10**(B/10)
            LAeKCorregido = int(10*math.log10(A-B)+0.5)
            LAeKCorregidoA.append(LAeKCorregido)
        if X != 0 and X != len(str(DatosLAe[Y]).split(' '))-1:
            A = float(str(DatosLAe[Y]).split(' ')[X])
            A = 10**(A/10)
            B = float(str(DatosLAN[Y]).split(' ')[X])
            B = 10**(B/10)
            LAeKCorregido = int(10*math.log10(A-B)+0.5)
            LAeKCorregidoA.append(LAeKCorregido)
        if len(str(DatosLAe[Y]).split(' ')) == 1:
            A = float(str(DatosLAe[Y]).split(' ')[X][2:-2])
            A = 10**(A/10)
            B = float(str(DatosLAN[Y]).split(' ')[X][2:-2])
            B = 10**(B/10)
            LAeKCorregido = int(10*math.log10(A-B)+0.5)
            LAeKCorregidoA.append(LAeKCorregido)
        X = X +1
    X = 0;
    LAeKCorregidoLista.append(LAeKCorregidoA)
    LAeKCorregidoA = []
    Y = Y +1;

#Corregir LCeq

LCeKCorregidoLista = []
LCeKCorregidoC = []

Y = 0
X = 0
while (Y < len(DatosLCe)):
    while (X < len(str(DatosLCe[Y]).split(' '))):
        if X == 0 and len(str(DatosLCe[Y]).split(' ')) != 1:
            A = float(str(DatosLCe[Y]).split(' ')[X][2:])
            A = 10**(A/10)
            B = float(str(DatosLCN[Y]).split(' ')[X][2:])
            B = 10**(B/10)
            LCeKCorregido = int(10*math.log10(A-B)+0.5)
            LCeKCorregidoC.append(LCeKCorregido)
        if X == len(str(DatosLCe[Y]).split(' '))-1 and len(str(DatosLCe[Y]).split(' ')) != 1:
            A = float(str(DatosLCe[Y]).split(' ')[X][:-2])
            A = 10**(A/10)
            B = float(str(DatosLCN[Y]).split(' ')[X][:-2])
            B = 10**(B/10)
            LCeKCorregido = int(10*math.log10(A-B)+0.5)
            LCeKCorregidoC.append(LCeKCorregido)
        if X != 0 and X != len(str(DatosLCe[Y]).split(' '))-1:
            A = float(str(DatosLCe[Y]).split(' ')[X])
            A = 10**(A/10)
            B = float(str(DatosLCN[Y]).split(' ')[X])
            B = 10**(B/10)
            LCeKCorregido = int(10*math.log10(A-B)+0.5)
            LCeKCorregidoC.append(LCeKCorregido)
        if len(str(DatosLCe[Y]).split(' ')) == 1:
            A = float(str(DatosLCe[Y]).split(' ')[X][2:-2])
            A = 10**(A/10)
            B = float(str(DatosLCN[Y]).split(' ')[X][2:-2])
            B = 10**(B/10)
            LCeKCorregido = int(10*math.log10(A-B)+0.5)
            LCeKCorregidoC.append(LCeKCorregido)
        X = X +1
    X = 0;
    LCeKCorregidoLista.append(LCeKCorregidoC)
    LCeKCorregidoC = []
    Y = Y +1;

#Calcular Kf
#Calcular LKeq,T = LAeq, T + Kt + Kf + Ki
#Ki = Kt = 0

if MODO == "interior":
    Limite = 55+3
elif MODO == "exterior":
    Limite = 60+3
else:
    sys.exit("No olvide introducir interior o exterior como argumento al ejecutar el programa")

LKeqTLista = []
LKeqTindividual = []
Y = 0
X = 0
while (Y < len(LAeKCorregidoLista)):
    while (X < len(str(LAeKCorregidoLista[Y]).split(' '))):
        A = LAeKCorregidoLista[Y][X]
        B = LCeKCorregidoLista[Y][X]
        Diferencia = B - A
        if Diferencia < 10:
            K = 0
        if Diferencia < 15 and Diferencia >= 10:
            K = 3
        if Diferencia >= 15:
            K = 6
        LKeqX = A + K
        K = 0
        LKeqTindividual.append(LKeqX)
        X = X +1
    X = 0;
    LKeqTLista.append(LKeqTindividual)
    LKeqTindividual = []
    Y = Y +1;

Y = 0
CUMPLE = True
Desfavorable = -1
string = "Valor limite = " + str(Limite) + "dBA" + '\n'
for linea in LKeqTLista:
    Y = Y +1
    for key in linea:
        if Desfavorable < key:
            Desfavorable = key
    string = (string + "Punto " + str(Y) + " LKeq: " + str(Desfavorable) + " dBA" + " (El mas desfavorable de todas las mediciones en ese punto)" '\n')
    if Desfavorable > Limite:
        CUMPLE = False
    Desfavorable = -1
if CUMPLE:
    print("")
    print("Cumplimos la normativa")
    string = (string + " No cunplimos la normativa porque una medida de uno del os puntos esta por encima del limite")
else:
    print("")
    print("No cumple la normativa ya que uno o varios puntos no estan dentro de los valores permitidos")

with open(NombreGuardado, 'w') as DatosFinales:
    DatosFinales.write(string)
