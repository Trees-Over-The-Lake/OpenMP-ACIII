from prettytable import PrettyTable
import sys

results_map = {}
section = ''
contador = 0

sort_name = sys.argv[1].split('.')[0]

with open(sys.argv[1], "r") as a_file:

  for line in a_file:

    stripped_line = line.strip()

    if  sort_name in stripped_line:
        if section != '':
          results_map[section] /= contador
        section = stripped_line
        results_map[section] = 0
        contador = 0
    
    if "Tempo" in stripped_line: 
        values = stripped_line.split(": ")
        results_map[section] += float(values[1])
        contador += 1

results_map[section] /= contador
table = PrettyTable() 

for key, value in results_map.items():
  table.add_column(key,[value])

# file_object = open('resultado.txt', 'a')

# file_object.write('\n')

# file_object.write(str(table))

print(table)