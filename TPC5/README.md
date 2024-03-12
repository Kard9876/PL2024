# TPC5: Máquina de Vendas
## 2024-03-08

## Autor:
- A100695
- Guilherme João Fernandes Barbosa

## Resumo

A proposta do quinto projeto desenvolvido no contexto desta UC é a desenvolver, através de um analisador léxico, uma [máquina de vendas](vending_machine.py) que permita os utilizadores listar os diversos produtos que a máquina posusi, inserir moedas, comprar os produtos e sair da máquina, recolhendo o devido troco. Para tal ser possível, foram implementados diversos estados, cada um com os respetivos tokens, para facilitar o processamento da informação. Assim, os estados e respetivos tokens especificados foram:

- `LISTING`, o qual é `inclusive` e que não espera mais nenhum tipo de token
- `INPUT`, que é `inclusive` e espera que, de seguida, sejam indicadas as moedas que serão inseridas (cada moeda deve ser seguida de um `e` [euro] ou de um `c`)
- `SELECT`, o qual é `inclusive`
- `LEAVE`, também `inclusive`

