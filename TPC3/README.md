# TPC3: Somador On e Off
## 2024-02-23

## Autor:
- A100695
- Guilherme João Fernandes Barbosa

## Resumo

Este trabalho tem o objetivo de ler um texto e realizar a soma dos inteiros encontrados no mesmo, porém com um pequeno grande detalhe. O somador começa no estado desligado, sendo ligado sempre que encontra a expressão **on** em qualquer combinação de letras maísculas e minúsculas. Sempre que é lida a expressão **off**, também em qualquer combinação de letras maiúsculas e minúsculas, o somador deve ignorar quaisquer inteiros encontrados até a expressão **on** ser lida novamente. Quando é encontrado um sinal **=**, o somador deve imprimir a mensagem "Soma = *soma_atual*".

Para criar este contador foi desenvolvido um [**script**](somador_on_off.py) em python. Este script lê as linhas de texto diretamento do **stdin** e, para cada linha lida, utiliza a expressão regular `(on|off|=|\d+)` para encontrar todas as expressões que correspondem às expressões **on**, **off**, **=** ou inteiros, utilizando o findall para devolver todas as ocorrências detetadas segundo a ordem em que se encontram e utilizando o modo **re.I**, do módulo **re** para fazer a verificação ignorando letras minúsculas ou maiúsculas. A lista devolvida é depois percorridas e, para cada elemento, verifica o que o mesmo representa e realiza a operação correspondente.