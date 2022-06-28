#define um dicionário com dados do problema
faturamento = {'sp':67836.43, 'rj':36678.66, 'mg':29229.88, 'es':27165.48, 'n':19849.53}
total = 0

#soma o faturamento do mês
for i in faturamento:
  total += faturamento[i]

#calcula a porcentagem que cada estado teve do total do mês
for i in faturamento:
  fporcento = {i:faturamento[i] * 100 / total}
  if(i != 'n'):
    print(i.upper(), "foi responsavel por", round(fporcento[i], 2), "% das vendas do mes")
  else:
    print("Os outros estados foram responsaveis por", round(fporcento[i], 2), "% das vendas do mes")