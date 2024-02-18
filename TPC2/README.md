# TPC2: Conversor de MD para HTML
## 2024-02-16

## Autor:
- A100695
- Guilherme João Fernandes Barbosa

## Resumo

Este trabalho tem o objetivo de converter um ficheiro **Markdown** em **HTML**, tendo em consideração apenas algumas notações básicas da sintaxe de **Markdown**.

Para tal, foi desenvolvido um [script](md_to_html.py) em python que converte a sintaxe de *negrito*, *itálico*, listas *numeradas* e *não numeradas*, *cabeçalhos* de diferentes níveis, *código*, *citação de bloco*, *separação horizontal*, *imagem* e *link* no respetivo código **HTML**. Todas as restantes sintaxes são mantidas na sua forma original dentro de um parágrafo. Este script foi desenvolvido de forma a aceitar input diretamente do ***stdin*** e a escrever o seu output no ***stdout***.

Para processar uma linha de texto houve uma mistura de resoluções. Cada linha de texto é verificada através de **Expressões regulares** para detetar algumas sintaxes, enquanto é percorrida sequencialmente para detetar outras (*negrito* e *itálico*). É esta passagem sequencial que permite a deteção de ***notação aninhada*** através da utilização de uma stack, na qual são matidas todas as notações (*negrito* e *itálico*) já encontradas. Além disso, permite ainda que se mantenha a formatação inicial dos blocos de código, isto é, que não sejam processadas eventuais notações (*negrito* e *itálico*) que apareçam dentro dos mesmos.

Para permitir todas as funcionalidades anteriormente descritas, além do script já mencionado, foram ainda desenvolvidos outros dois ficheiros em python. O [primeiro](md_to_html_aux.py) contém apenas as funções auxiliares que adicionam as **tags HTML** ao texto, enquanto que o [segundo](stack.py) contém o código necessário à implementação da stack previamente referida.
