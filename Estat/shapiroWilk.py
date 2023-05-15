import scipy.stats as stats

y = [0.004759,0.006120,0.008620,0.008874,0.004817,0.004687,0.004773,0.007620,0.005360,0.007544,0.008712,0.008666,0.007400,0.007608,0.005360,0.007628,0.008842,0.012588,0.006216,0.008652,0.010222,0.005303,0.008620,0.004797,0.010078,0.008671,0.010072,0.008756,0.010091,0.009005]

shapiro_stat, shapiro_p_valor = stats.shapiro(y)

print("Valor estatístico de Shapiro-Wilk = " + str(shapiro_stat))
print("Valor de p de Shapiro-Wilk = " + str(shapiro_p_valor))


