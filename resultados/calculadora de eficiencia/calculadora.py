sequencialShell = 0.39620000000000005
valoresShell = {2: 0.22650000000000006, 4: 0.14, 8: 0.11190000000000003, 12: 0.10629999999999999}

sequencialMerge = 0.2553636363636363
valoresMerge = {2: 0.15209999999999999, 4: 0.1485, 8: 0.1485}

sequencialSelection = 0.2131
valoresSelection = {2: 0.21372727272727277, 4: 0.09899999999999999, 8: 0.09879999999999999}


def calcularSpeedUp(algoritmo, sequencial, dicionarioParalelo):
    print(algoritmo)
    for i in dicionarioParalelo:
        speedUp = sequencial / dicionarioParalelo[i]
        print(f'SpeedUp do {algoritmo} com {i} threads: {speedUp:.3f}.')

        ganho = (sequencial + dicionarioParalelo[i]) / (sequencial + (dicionarioParalelo[i] / i))
        print(f'O ganho foi de {(ganho-1):.3%}.')

        eficiencia = speedUp / i
        print(f'A eficiência obtida foi de {eficiencia:.3%}.')

        print()

    print('\n------------------\n')



calcularSpeedUp('ShellSort', sequencialShell, valoresShell)
calcularSpeedUp('MergeSort', sequencialMerge, valoresMerge)
calcularSpeedUp('SelectionSort', sequencialSelection, valoresSelection)