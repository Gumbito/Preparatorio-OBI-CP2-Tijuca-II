horas, minutos, segundos = [int(input()) for _ in range(3)]
segundos_adiados = int(input())

segundos += segundos_adiados

minutos += segundos // 60
segundos %= 60

horas += minutos // 60
minutos %= 60

horas %= 24

print()
print(horas)
print(minutos)
print(segundos)