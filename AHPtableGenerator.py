# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# El código original fue hecho por: El Inge MX
# Información disponible en: https://www.youtube.com/watch?v=p-sEVyERS_w
# Esta versión cambia el uso de Excel a código LaTeX
# 01/04/2021 @hasecilu
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import numpy as np

from pylatex import Document, Section, Subsection, Tabular
import os

print('''\n\t\t\tようこうそ\n\n
Bienvenido al asistente para generar tablas de resultados mediante 
el Proceso Analítico Jerárquico (AHP - Analitic Hierarchy Process).
\n\t\t\t\tBy: @hasecilu ft. El Inge MX\n''')

cadena = (input('Ingrese los elementos separados por espacio. Ej. "Red Green Blue": ').split(" "))
size = len(cadena) # Matriz cuadrada tamaño size
for x in cadena:
  print(x)

general = np.identity(size)
cr_list = range(1, size + 1)

decimal = 4
fila = 1
col = 0
k = 1

#Matriz AHP
while col < size:
    while fila < size:
        #cf = fila + 1
        #cc = col + 1
        while k == 1:
            try:
                value = float(input('Opción "' + cadena[fila] + '" contra opción "' + cadena[col] + '": '))
                k = 0
            except:
                value = print('La regaste, vas de nuez.')
                k = 1
        k = 1
        if value > 0:
            general[fila, col] = value
            general[col, fila] = round(1/value, decimal)
        else:
            value = abs(value)
            general[fila, col] = round(1 / value, decimal)
            general[col, fila] = value
        fila += 1
    col += 1
    fila = col + 1

#Matriz normalizada
sum1 = np.apply_along_axis(sum, 0, general)
norm = general.copy()
col = 0
fila = 0
while col < size:
    while fila < size:
        norm[fila, col] = round(norm[fila, col]/sum1[col], decimal)
        fila += 1
    col += 1
    fila = 0

sum2 = np.apply_along_axis(sum, 0, norm)
vec = np.apply_along_axis(sum, 1, norm)
vec = np.around(vec, decimal)
vp = vec/size
vp = np.around(vp, decimal)
vp = vp.reshape(size, 1)

sumNormRow = np.apply_along_axis(sum, 0, vec)
comp = np.apply_along_axis(sum, 0, vp)

# print('\n\nMatriz general\n')
# print(general)
# print('\n\nSuma de columnas\n')
# print(sum1)
# print('\n\nMatriz normalizada\n')
# print(norm)
# print('\n\nSuma de filas normalizadas')
# print(vec)
# print('\n\nVector de prioridad normalizado')
# print(vp)
# print('\n\nSuma del vector de prioridad')
# print(comp)
# print('\n')


if __name__ == '__main__':
    geometry_options = {"tmargin": "1cm", "lmargin": "1cm"}
    doc = Document(geometry_options=geometry_options)
    
    with doc.create(Section('Proceso Analítico Jerárquico (AHP - Analitic Hierarchy Process)')):
                   
        tablesize = ''
        for var in range(general.shape[0]+1):   # +1 porque se agregan 1 columna
           tablesize = tablesize + 'c'     #Concatenar
   
        with doc.create(Subsection('Matriz general')):
            with doc.create(Tabular(tablesize)) as table:
                # Encabezado
                table.add_hline()   # Cambiar por \toprule en LaTeX
                encabezado = ['Criterios',]
                for var in range(len(cadena)):
                    encabezado.append(cadena[var])
                table.add_row(encabezado)
                table.add_hline()   # Cambiar por \midrule en LaTeX
                # Contenido
                for var in range(general.shape[0]):
                    contenido = [cadena[var],]
                    for var2 in range(general.shape[0]):
                        contenido.append(general[var][var2])
                    table.add_row(contenido)
                # Suma
                table.add_hline()   # Cambiar por \midrule en LaTeX
                encabezado = ['Suma',]
                for var in range(len(sum1)):
                    encabezado.append(sum1[var])
                table.add_row(encabezado)
                table.add_hline()   # Cambiar por \bottomrule en LaTeX
        
        tablesize = ''
        for var in range(general.shape[0]+3):   # +3 porque se agregan 3 columnas
           tablesize = tablesize + 'c'     #Concatenar
        
        with doc.create(Subsection('Matriz normalizada')):
            with doc.create(Tabular(tablesize)) as table:
                # Encabezado
                table.add_hline()   # Cambiar por \toprule en LaTeX
                encabezado = ['Criterios',]
                for var in range(len(cadena)):
                    encabezado.append(cadena[var])
                encabezado.append('Total de fila')
                encabezado.append('Vector de prioridad')
                table.add_row(encabezado)
                table.add_hline()   # Cambiar por \midrule en LaTeX
                # Contenido
                for var in range(general.shape[0]):
                    contenido = [cadena[var],]
                    for var2 in range(general.shape[0]):
                        contenido.append(norm[var][var2])
                    contenido.append(vec[var])
                    contenido.append(vp[var])
                    table.add_row(contenido)
                # Suma
                table.add_hline()   # Cambiar por \midrule en LaTeX
                encabezado = ['Suma',]  # Reciclar variable
                for var in range(len(sum2)):
                    encabezado.append(np.around(sum2[var], decimal))
                encabezado.append(np.around(sumNormRow, decimal))
                encabezado.append(np.around(comp, decimal))
                table.add_row(encabezado)
                table.add_hline()   # Cambiar por \bottomrule en LaTeX
    Name = str(input('''File's name: '''))
    doc.generate_pdf(Name, clean_tex=False)
    
    print('''\n\t\t\tさようなら\n''')
