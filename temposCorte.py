import pandas as pd

temposCorteDados = pd.read_csv("temposCorte-data.csv")

temposCorteDados = pd.DataFrame(temposCorteDados)

temposCorte = temposCorteDados[[
    'Tipo_de_corte', 'Modelo', 'Tempo_s', 'Categoria']]

temposCortes = temposCorte.copy()
temposCortes.Tempo_s = temposCorte.Tempo_s.str.replace(',', '').astype(float)
