# NÃO FUNCIONANDO

qmetais, tamanho_conjunto = [int(x) for x in input().split()]
impurezas = [int(x) for x in input().split()]

def or_list(nums: list[int]):
    num = nums[0]
    for i in range(1, len(nums)):
        num = num | nums[i]
    return num

if tamanho_conjunto == 2:
    print(or_list(impurezas))
    exit()

while len(impurezas) >= tamanho_conjunto:
    max_index = 0
    max_or = 0
    max_diff = 0
    for i in range(0, len(impurezas) - tamanho_conjunto + 1):
        intervalo = impurezas[i : i + tamanho_conjunto]
        curr_or = or_list(intervalo)
        curr_sum = sum(intervalo)
        curr_diff = curr_sum - curr_or
        print(f'intervalo {i+1}: {intervalo}; soma: {curr_sum}; or: {curr_or}; diff: {curr_diff}')
        if curr_diff > max_diff:
            max_index = i
            max_or = curr_or
            max_diff = curr_diff
    
    print(f'intervalo para ORar: # {max_index+1}')
    impurezas = impurezas[: max_index] + impurezas[max_index + tamanho_conjunto:] 
    impurezas.insert(max_index, max_or)
    print(*impurezas, sep=' ')

print(sum(impurezas))