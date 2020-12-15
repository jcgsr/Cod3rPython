# 10.12.2020
# Susi no hospital ainda

def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 65):
        return 'adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'Idade inválida'


if __name__ == '__main__':
    idades = (17, 0, 35, 87, 113, -2)  # tupla
    for idade in idades:
        print(f'{idade}: {faixa_etaria(idade)}')
