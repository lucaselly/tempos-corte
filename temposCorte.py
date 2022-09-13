import pandas as pd

# Criar um DataFrame de um .CSV
temposCorteDados = pd.read_csv("temposCorte-data.csv")

# Separar apenas as colunas úteis
temposCorte = temposCorteDados[[
    'Tipo_de_corte', 'Modelo', 'Tempo_s', 'Categoria']]

# Criando uma cópia para transformar a coluna Tempo_s em Float
temposCortes = temposCorte.copy()
# Aqui é necessário adaptar dependendo da configuração do computador em que for rodar.
# Caso os milhares sejam separados por virgula, utilizar o seguinte:
temposCortes.Tempo_s = temposCorte.Tempo_s.str.replace(',', '').astype(float)

# Uma outra possibilidade é dos milhares serem separados por ponto e as os decimais por virgula, então usar o seguinte:
# temposCorte.Tempo_s = temposCorte.Tempo_s.str.replace('.', '')
# temposCortes.Tempo_s = temposCorte.Tempo_s.str.replace(',', '.').astype(float)


# Criando um dicionário com os tipos de corte
tipoCorte = {'CABEDAL': [], 'FORRO': [], 'COMPLETO': []}

# Criando um dicionário com as categorias
temposCateg = {'BotaCa': [], 'CoturnoCa': [], 'FlatCa': [], 'FlatformCa': [], 'LoaferCa': [], 'MuleCa': [
], 'OpenCa': [], 'OxfordCa': [], 'RasteiraCa': [], 'SapatilhaCa': [], 'SlipperCa': [], 'SneakerCa': [], 'BotaFo': [], 'CoturnoFo': [], 'FlatFo': [], 'FlatformFo': [], 'LoaferFo': [], 'MuleFo': [
], 'OpenFo': [], 'OxfordFo': [], 'RasteiraFo': [], 'SapatilhaFo': [], 'SlipperFo': [], 'SneakerFo': [], 'BotaCo': [], 'CoturnoCo': [], 'FlatCo': [], 'FlatformCo': [], 'LoaferCo': [], 'MuleCo': [
], 'OpenCo': [], 'OxfordCo': [], 'RasteiraCo': [], 'SapatilhaCo': [], 'SlipperCo': [], 'SneakerCo': []}

for linha in temposCortes.values:
    if linha[0] == 'CABEDAL':
        if linha[3] == 'Bota':
            temposCateg['BotaCa'].append(linha[2])
        elif linha[3] == 'Coturno':
            temposCateg['CoturnoCa'].append(linha[2])
        elif linha[3] == 'Flat':
            temposCateg['FlatCa'].append(linha[2])
        elif linha[3] == 'Flatform':
            temposCateg['FlatformCa'].append(linha[2])
        elif linha[3] == 'Loafer':
            temposCateg['LoaferCa'].append(linha[2])
        elif linha[3] == 'Mule':
            temposCateg['MuleCa'].append(linha[2])
        elif linha[3] == 'Open':
            temposCateg['OpenCa'].append(linha[2])
        elif linha[3] == 'Oxford':
            temposCateg['OxfordCa'].append(linha[2])
        elif linha[3] == 'Rasteira':
            temposCateg['RasteiraCa'].append(linha[2])
        elif linha[3] == 'Sapatilha':
            temposCateg['SapatilhaCa'].append(linha[2])
        elif linha[3] == 'Slipper':
            temposCateg['SlipperCa'].append(linha[2])
        elif linha[3] == 'Sneaker':
            temposCateg['SneakerCa'].append(linha[2])
    elif linha[0] == 'FORRO':
        if linha[3] == 'Bota':
            temposCateg['BotaFo'].append(linha[2])
        elif linha[3] == 'Coturno':
            temposCateg['CoturnoFo'].append(linha[2])
        elif linha[3] == 'Flat':
            temposCateg['FlatFo'].append(linha[2])
        elif linha[3] == 'Flatform':
            temposCateg['FlatformFo'].append(linha[2])
        elif linha[3] == 'Loafer':
            temposCateg['LoaferFo'].append(linha[2])
        elif linha[3] == 'Mule':
            temposCateg['MuleFo'].append(linha[2])
        elif linha[3] == 'Open':
            temposCateg['OpenFo'].append(linha[2])
        elif linha[3] == 'Oxford':
            temposCateg['OxfordFo'].append(linha[2])
        elif linha[3] == 'Rasteira':
            temposCateg['RasteiraFo'].append(linha[2])
        elif linha[3] == 'Sapatilha':
            temposCateg['SapatilhaFo'].append(linha[2])
        elif linha[3] == 'Slipper':
            temposCateg['SlipperFo'].append(linha[2])
        elif linha[3] == 'Sneaker':
            temposCateg['SneakerFo'].append(linha[2])
    elif linha[0] == 'COMPLETO':
        if linha[3] == 'Bota':
            temposCateg['BotaCo'].append(linha[2])
        elif linha[3] == 'Coturno':
            temposCateg['CoturnoCo'].append(linha[2])
        elif linha[3] == 'Flat':
            temposCateg['FlatCo'].append(linha[2])
        elif linha[3] == 'Flatform':
            temposCateg['FlatformCo'].append(linha[2])
        elif linha[3] == 'Loafer':
            temposCateg['LoaferCo'].append(linha[2])
        elif linha[3] == 'Mule':
            temposCateg['MuleCo'].append(linha[2])
        elif linha[3] == 'Open':
            temposCateg['OpenCo'].append(linha[2])
        elif linha[3] == 'Oxford':
            temposCateg['OxfordCo'].append(linha[2])
        elif linha[3] == 'Rasteira':
            temposCateg['RasteiraCo'].append(linha[2])
        elif linha[3] == 'Sapatilha':
            temposCateg['SapatilhaCo'].append(linha[2])
        elif linha[3] == 'Slipper':
            temposCateg['SlipperCo'].append(linha[2])
        elif linha[3] == 'Sneaker':
            temposCateg['SneakerCo'].append(linha[2])

teste = pd.DataFrame.from_dict(temposCateg, orient='index')
dfTeste2 = teste.transpose()

dfTeste2.to_csv("temposCorteSep.csv")
