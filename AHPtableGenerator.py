# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# El código original fue hecho por: El Inge MX
# Información disponible en: https://www.youtube.com/watch?v=p-sEVyERS_w
# Esta versión cambia el uso de Excel a código LaTeX
# 
# 18/08/2021 | v1.1 | @hasecilu
# https://github.com/hasecilu/AHPtableGenerator
# 
# ¿Dudas? RTFM -> https://jeltef.github.io/PyLaTeX/current/
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import numpy as np

from pylatex import Document, Section, Subsection, Tabular, NoEscape

import os

# Ingreso de datos # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
print('''\n\t\t\tようこうそ\n\n
Bienvenido al asistente para generar tablas de resultados mediante 
el Proceso Analítico Jerárquico (AHP - Analytic Hierarchy Process).
\n\t\t\t\tBy: @hasecilu ft. El Inge MX\n''')

cadena = (input('Ingrese los elementos separados por espacio. Ejemplo: "Red Green Blue"\n\n-> ').split(" "))
size = len(cadena) # Matriz cuadrada tamaño size
for x in cadena:
  print(x)
print() # Salto de línea

# Procesamiento de datos # # # # # # # # # # # # # # # # # # # # # # # # # # # 

general = np.identity(size)
cr_list = range(1, size + 1)

decimal = 4
fila = 1
col = 0
k = 1

# Matriz AHP
while col < size:
    while fila < size:
        # cf = fila + 1
        # cc = col + 1
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

# Matriz normalizada
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

# Generación de tablas # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

if __name__ == '__main__':
    geometry_options = {"tmargin": "1cm", "lmargin": "1cm"}
    doc = Document(geometry_options=geometry_options)
    
    with doc.create(Section('Proceso Analítico Jerárquico (AHP - Analitic Hierarchy Process)')):
        
        # Para poder usar \toprule, \midrule y \bottomrule
        doc.preamble.append(NoEscape("\\usepackage{booktabs}"))
        
        # Crear tabla de la Matriz general
        tablesize = ''
        for var in range(general.shape[0]+1):   # +1 porque se agregan 1 columna
           tablesize = tablesize + 'c'     # Concatenar
   
        with doc.create(Subsection('Matriz general')):
            doc.append(NoEscape("\\begin{table}[!ht]"))
            doc.append(NoEscape("\\centering"))
            with doc.create(Tabular(tablesize)) as table:
                # Encabezado
                # table.add_hline()   # Cambiar por \toprule en LaTeX
                doc.append(NoEscape("\\toprule"))
                encabezado = ['Criterios',]
                for var in range(len(cadena)):
                    encabezado.append(cadena[var])
                table.add_row(encabezado)
                # table.add_hline()   # Cambiar por \midrule en LaTeX
                doc.append(NoEscape("\\midrule"))
                
                # Contenido
                for var in range(general.shape[0]):
                    contenido = [cadena[var],]
                    for var2 in range(general.shape[0]):
                        contenido.append(general[var][var2])
                    table.add_row(contenido)
                
                # Suma
                # table.add_hline()   # Cambiar por \midrule en LaTeX
                doc.append(NoEscape("\\midrule"))
                encabezado = ['Suma',]
                for var in range(len(sum1)):
                    encabezado.append(sum1[var])
                table.add_row(encabezado)
                # table.add_hline()   # Cambiar por \bottomrule en LaTeX
                doc.append(NoEscape("\\bottomrule"))
        
        doc.append(NoEscape("\\caption{Matriz general}"))
        doc.append(NoEscape("\\end{table}"))
        
        # Crear tabla de la Matriz normalizada
        tablesize = ''
        for var in range(general.shape[0]+3):   # +3 porque se agregan 3 columnas
           tablesize = tablesize + 'c'     # Concatenar
        
        with doc.create(Subsection('Matriz normalizada')):
            doc.append(NoEscape("\\begin{table}[!ht]"))
            doc.append(NoEscape("\\centering"))
            with doc.create(Tabular(tablesize)) as table:
                # Encabezado
                # table.add_hline()   # Cambiar por \toprule en LaTeX
                doc.append(NoEscape("\\toprule"))
                encabezado = ['Criterios',]
                for var in range(len(cadena)):
                    encabezado.append(cadena[var])
                encabezado.append('Total de fila')
                encabezado.append('Vector de prioridad')
                table.add_row(encabezado)
                # table.add_hline()   # Cambiar por \midrule en LaTeX
                doc.append(NoEscape("\\midrule"))
                
                # Contenido
                for var in range(general.shape[0]):
                    contenido = [cadena[var],]
                    for var2 in range(general.shape[0]):
                        contenido.append(norm[var][var2])
                    contenido.append(vec[var])
                    contenido.append(vp[var])
                    table.add_row(contenido)
                
                # Suma
                # table.add_hline()   # Cambiar por \midrule en LaTeX
                doc.append(NoEscape("\\midrule"))
                encabezado = ['Suma',]  # Reciclar variable
                for var in range(len(sum2)):
                    encabezado.append(np.around(sum2[var], decimal))
                encabezado.append(np.around(sumNormRow, decimal))
                encabezado.append(np.around(comp, decimal))
                table.add_row(encabezado)
                # table.add_hline()   # Cambiar por \bottomrule en LaTeX
                doc.append(NoEscape("\\bottomrule"))
                
        doc.append(NoEscape("\\caption{Matriz normalizada}"))
        doc.append(NoEscape("\\end{table}"))
        
    Name = str(input('''File's name: '''))
    doc.generate_pdf(Name, clean_tex=False) # No borrar el archivo .tex
    
    print('''\nRecuerda revisar el código generado y modificar de ser necesario. ñ.ñ\n\n
          \t\t\tさようなら\n''')

