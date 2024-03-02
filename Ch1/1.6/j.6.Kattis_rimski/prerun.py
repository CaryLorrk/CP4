ones = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
}

tens = {
    1: 'X',
    2: 'XX',
    3: 'XXX',
    4: 'XL',
    5: 'L',
    6: 'LX',
    7: 'LXX',
    8: 'LXXX',
    9: 'XC',
}

mapping = {}
for i in range(100):
    ten = ''
    one = ''
    if i // 10 > 0:
        ten = tens[i // 10]
    if i % 10 > 0:
        one = ones[i % 10]
    mapping[f"{ten}{one}"] = i

print(mapping)
    
