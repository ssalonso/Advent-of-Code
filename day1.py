""" Advent of Code Day 1

El primer reto del AOC2024 nos pide, a partir de dos listas de números enteros, emparejar el número más pequeño de
la lista de la izquierda con el número más pequeño de la lista de la derecha, luego el segundo número más pequeño
de la izquierda con el segundo número más pequeño de la derecha, y así sucesivamente. Por ejemplo, si emparejamos
un 3 de la lista de la izquierda con un 7 de la lista de la derecha, la distancia es 4; si emparejamos un 9 con un 3,
la distancia es 6.

La parte I nos pide hallar la distancia total entre la lista izquierda y la lista derecha, sumando las distancias
entre todos los pares que hemos encontrado.

En la parte II, hay que averiguar con qué frecuencia aparece cada número de la lista de la izquierda en
la lista de la derecha para, a partir de esos valores, calcular una puntuación total de similitud sumando cada número
de la lista de la izquierda y multiplicándolo por el número de veces que aparece en la lista de la derecha. Así por
ejemplo, el primer número de la lista de la izquierda es el 3, y como aparece en la lista de la derecha tres veces,
esto aumenta la puntuación de similitud en 3 * 3 = 9.

Enunciado completo: https://adventofcode.com/2024/day/1

"""

f = open('input1.txt')
left_list = []
right_list = []
for line in f:
    clean_line = line.split()
    left_list.append(int(clean_line[0]))
    right_list.append(int(clean_line[1]))
left_list.sort()
right_list.sort()
f.close()

total_distance = 0
for i,j in zip(left_list,right_list): total_distance += abs(i-j)
print('Part I: ', total_distance)

similarity_score = 0
for i in left_list: similarity_score += i*right_list.count(i)
print('Part II: ', similarity_score)


