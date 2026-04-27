# NÃO É A MESMA QUESTÃO QUE "Cafeteria" DO MESMO ANO E MESMA FASE

SIM = 'S'
NAO = 'N'

min_leite, max_leite = [int(input()) for _ in range(2)]
capacidade_xicara = int(input())
cafe_preparado = int(input())

qleite = capacidade_xicara - cafe_preparado

if min_leite <= qleite <= max_leite: print(SIM)
else: print(NAO)