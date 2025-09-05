# Medical Data Visualizer

Projeto desenvolvido para o curso FreeCodeCamp - Data Analysis with Python.  
O objetivo é analisar e visualizar dados médicos usando pandas, matplotlib e seaborn.



##  Funcionalidades
- Calcula o IMC (BMI) e cria a coluna overweight onde 0 = normal e 1 = sobrepeso.
- Normaliza as variáveis cholesterol e gluc onde 0 = normal e 1 = alto.
- Gera um Catplot mostrando a distribuição de fatores de saúde cholesterol, gluc, smoke, alco, active, overweight) para pacientes com (cardio=1) e sem (cardio=0) doenças cardíacas.
- Gera um Heatmap da matriz de correlação após limpeza dos dados.



## Tecnologias utilizadas
- Python 3
- pandas
- matplotlib
- seaborn
- numpy



## Como rodar

Instale as dependências:
```bash
pip install -r requirements.txt

python main.py

