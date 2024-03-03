# TPC3: Analisador Léxico
## 2024-03-01

## Autor:
- A100695
- Guilherme João Fernandes Barbosa

## Resumo

A proposta para este 4º projeto foi o desenvolvimento de um analisador léxico. Este analisador deve, pelo menos, ler a frase `SELECT id, name, salario FROM empregados WHERE salario >= 820` e devolver a lista com os símbolos terminais (sinais, palavras reservadas, terminais variáveis) identificados.

Para implementar a proposta foi desenvolvido um [script](lexical_analyzer.py) em python. Os símbolos:

- `>`,
- `<`,
- `=`,
- `,`,
- `;`,
- `(`,
- `)`,
- `+`,
- `-`,
- `*`,
- `/`,

definem o conjunto de sinais aceites e a lista de palavras reservadas definida é constituída por:

- `SELECT`,
- `UPDATE`,
- `CREATE`,
- `FROM`,
- `WHERE`,
- `SET`,
- `DROP`,
- `DELETE`,
- `TABLE`.

Para além disso, as terminais variáveis identificadas são:

- `SKIP`, que corresponde a um espaço;
- `FIELD`, que corresponde aos nomes que identificam as colunas das tabelas (combinações de letras que não formem uma palavra reservada);
- `NUMBER`, que inclui números inteiros e reais.

O script faz utilização da biblioteca **ply** para obter os resultados desejados e, por isso, possui o regex equivalente aos símbolos indicados, além de apresentar duas funções, uma que conta o número da linha e outra que indica quando aparece algum caracter inválido. Por fim, dada uma string multi linha com alguns testes, o script utiliza o **lex** do módulo **lex** da biblioteca anteriormente referida para identificar os diversos símbolos terminais da string.