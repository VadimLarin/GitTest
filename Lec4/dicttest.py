alph = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'X',
    10: 'Y',
}

for key, value in alph.items(): 
    if value in 'AY|':
        print(f'ключ: {key} значение: {value}')