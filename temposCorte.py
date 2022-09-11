import pandas as pd

# Criar um DataFrame de um .CSV
temposCorteDados = pd.read_csv("temposCorte-data.csv")

# Separar apenas as colunas úteis
temposCorte = temposCorteDados[[
    'Tipo_de_corte', 'Modelo', 'Tempo_s', 'Categoria']]

# Criando uma cópia para transformar a coluna Tempo_s em Float
temposCortes = temposCorte.copy()
temposCortes.Tempo_s = temposCorte.Tempo_s.str.replace(',', '').astype(float)

tipoCorte = {'CABEDAL': [], 'FORRO': [], 'COMPLETO': []}

categoria = {'Bota': [], 'Coturno': [], 'Flat': [], 'Flatform': [], 'Loafer': [], 'Mule': [
], 'Open': [], 'Oxford': [], 'Rasteira': [], 'Sapatilha': [], 'Slipper': [], 'Sneaker': []}

final = tipoCorte.copy()
for tipo in tipoCorte:
    final[tipo] = categoria
print(final)
