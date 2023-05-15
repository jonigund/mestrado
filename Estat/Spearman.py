import os

import pandas as pd
from scipy.stats import spearmanr

os.chdir("F:/Mestrado_ETA/Valendo/Estatisticas")
myDf = pd.read_csv("spearmanT2T3.csv")
myDf.columns = ['indice', 'T2', 'T3']
myDf.head()

T2 = myDf['T2']
T3 = myDf['T3']
spearmanr_coefficient, p_value = spearmanr(T2, T3)

print(myDf)
print('Coeficiente de Spearman = '+ str(spearmanr_coefficient))
