import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np

data = pd.read_csv("ConceitoEnade2019.csv")



media = data["Conceito Enade (Contínuo)"].mean()
variancia = data["Conceito Enade (Contínuo)"].var()
moda = data["Conceito Enade (Contínuo)"].mode()
mediana = data["Conceito Enade (Contínuo)"].median()
desvio_padrao = data["Conceito Enade (Contínuo)"].std()

print("ESTATÍSTICAS A RESPEITO DO CONCEITO ENADE (CONTÍNUO):\n")
print("Media: "+ str(round(media,3)))
print("Variância: "+ str(round(variancia,3)))
print("Mediana: "+ str(round(mediana,3)))
print("Desvio padrão: "+ str(round(desvio_padrao,3)))
print("Moda: "+ str(round(moda,3)))



# Histograma

curso = "ENGENHARIA MECÂNICA"

histogramaData = data[data["Área de Avaliação"] == curso]
histogramaData = histogramaData[["Sigla da IES", "Conceito Enade (Contínuo)"]]
histogramaData = histogramaData.groupby("Sigla da IES").head(1)

histChart = px.histogram(histogramaData, x="Sigla da IES", y="Conceito Enade (Contínuo)")
histChart.show() 

# Star Plot

universidade = "UFRJ"

radarDataIME = data[data["Sigla da IES"] == 'IME']
radarDataOutro = data[data["Sigla da IES"] == universidade]

fig = make_subplots(rows=1, cols=5, specs=[[{'type': 'polar'}] * 5] * 1)
fig.add_trace(
    go.Scatterpolar(
      theta=radarDataIME["Área de Avaliação"], 
      r=radarDataIME["Conceito Enade (Contínuo)"],
      fill='toself',
      name='IME'
      ),
    row=1, col=2
)

fig.add_trace(
    go.Scatterpolar(
      theta=radarDataOutro["Área de Avaliação"], 
      r=radarDataOutro["Conceito Enade (Contínuo)"],
      fill='toself',
      name=universidade
    ),
    row=1, col=4
)

title = f'Comparação entre o IME e {universidade}'

fig.update_layout( title_text=title)
fig.show()




