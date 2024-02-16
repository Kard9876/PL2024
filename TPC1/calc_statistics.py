import sys

def chaveOrd(s):
    s = s.lower()

    special_chars = {
        'á': 'a',
        'à': 'a',
        'â': 'a',
        'ã': 'a',
        'é': 'e',
        'ê': 'e',
        'í': 'i',
        'ó': 'o',
        'ô': 'o',
        'õ': 'o',
        'ú': 'u',
        'ç': 'c',
    }

    for special, default in special_chars.items():
        s = s.replace(special, default)

    return s

val = True

modalidades = set()

escaloes = {}

atletas_total = 0
atletas_aptos = 0
atletas_inaptos = 0

idade_min = 200
idade_max = 0

for line in sys.stdin:
    if val:
        val = False
        continue

    line = line.split(',')

    id = line[0]
    index = line[1]
    dataEMD = line[2]
    primeiro_nome = line[3]
    último_nome = line[4]
    idade = int(line[5])
    género = line[6]
    morada = line[7]
    modalidade = line[8]
    clube = line[9]
    email = line[10]
    federado = line[11]
    resultado = line[12] == 'true\n'

    escalao_start = idade - (idade % 5)

    idade_min = min(idade_min, escalao_start)
    idade_max = max(idade_max, escalao_start)

    cur_count = escaloes.get(escalao_start, 0)

    escaloes[escalao_start] = cur_count + 1

    modalidades.add(modalidade)

    atletas_total += 1

    if resultado:
        atletas_aptos += 1
    else:
        atletas_inaptos += 1

print(f"Atletas aptos: {'100' if atletas_total == 0 else str((atletas_aptos / atletas_total) * 100)}%")
print(f"Atletas inaptos: {'0' if atletas_total == 0 else str((atletas_inaptos / atletas_total)*100)}%")
print()

modalidades = list(modalidades)

modalidades.sort(key = chaveOrd)

print(f"Modalidades: {modalidades}")
print()

escaloes_str = "Escalões: {"

while idade_min <= idade_max:
    escaloes_str += f"{idade_min}-{idade_min+4}: {(escaloes.get(idade_min, 0) / atletas_total) * 100}% ({escaloes.get(idade_min, 0)} atletas)"
    
    idade_min += 5

    if idade_min <= idade_max:
        escaloes_str += ", "

escaloes_str += "}"

print(escaloes_str)
print()
