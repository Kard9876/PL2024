# TPC1: Análise de um dataset
## 2024-02-09

## Autor:
- A100695
- Guilherme João Fernandes Barbosa

## Resumo

Neste trabalho utilizou-se o material fornecido pelo docente, nomeadamente um ficheiro csv com a informação de 300 exames médicos desportivos.

O objetivo do trabalho é calcular e apresentar um conjunto de estatísticas, o qual involve o cálculo da lista de modalidades frequentadas, ordenada por ordem alfabética, o cálculo da percentagem de atletas considerados aptos e inaptos para a prática desportiva e, por fim, o cálculo da distribuição dos atletas por escalão etário, sendo que cada escalão corresponde a um intervalo de 5 anos. Por embelezamento da resposta apresentada, na primeira estatística foram removidas as modalidades repetidas, sendo assim apresentada cada modalidade apenas uma vez.

Com os dados fornecidos, foi desenvolvido um script em python3 [(Calc Statistics)](calc_statistics.py), o qual lê a partir do stdin os dados introduzidos e envia para o stdout as estatísticas calculadas. Como o script assume que os dados que recebe seguem um formato CSV, este ignora a primeira linha lida, pois esta, no formato indicado, seria a linha responsável por identificar os diversos campos que compõe cada uma das seguintes linhas, não contendo por isso informação útil para o cálculo de qualquer estatística.