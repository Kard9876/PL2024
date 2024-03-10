# TPC4: Analisador Léxico
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
- `SKIP`[^1]

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

- `FIELD`, que corresponde aos nomes[^2] que identificam as colunas ou as tabelas. Pode ser um `FIELD_NAME` ou um `TABLE_NAME`[^3], o que indica que se trata do nome de uma coluna ou tabela, respetivamente;
- `NUMBER`, que inclui números inteiros e reais.

O script faz utilização da biblioteca **ply** para obter os resultados desejados e, por isso, possui o regex e funções equivalente aos símbolos indicados, além de apresentar duas funções, uma que conta o número da linha e outra que indica quando aparece algum caracter inválido. Por fim, dada uma string multi linha com alguns testes, o script utiliza o módulo **lex** da biblioteca anteriormente referida para identificar os diversos símbolos terminais da string.

[^1]: que corresponde a um espaço
[^2]: combinações de letras que não formem uma palavra reservada
[^3]: Dependente de contexto