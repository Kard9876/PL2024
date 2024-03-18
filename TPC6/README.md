# TPC6: Gramática Independente de Contexto LL(1)
## 2024-03-08

## Autor:
- A100695
- Guilherme João Fernandes Barbosa

## Resumo

O objetivo deste sexto trabalho da UC de *Processamento de Linguagens* foi o de criar uma Gramática Independente de Contexto que suporte uma série de frases exemplo fornecidas pelo docente. Esta gramática deve pertencer à categoria LL(1) pelo que, além de não poder conter ambiguidade nas suas regras, a interseção dos Look Ahead de cada conjunto de produções originadas do mesmo símbolo não-terminal tem de ser o conjunto vazio.

## Resolução

### Frases Exemplo

- ? a
- b = a * 2 / (27 - 3)
- ! a + b
- c = a * b / (a / b)

### Gramática Independente de Contexto inicial

A gramática seguinte possui ambiguidade, porém serviu para derivar a gramática final.

T = {`?`, `!`, `=`, `+`, `-`, `*`, `/`, `num`, `id_var`, `\n`}

N = {S, Value, Exp, Termo, Fator}

S = S
```
p = {
    p1:          S → `?` Exp Separador
    p2:            | `!` Exp Separador
    p3:            | `id_var` `=` Exp Separador
    p4:        Exp → Termo `+` Exp
    p5:            | Termo `-` Exp
    p6:            | Termo
    p7:      Termo → Fator `*` Termo
    p8:            | Fator `/` Termo
    p9:            | Fator
    p10:     Fator → `(` Exp `)`
    p11:           | num
    p12:           | id_var
    p13: Separador → `\n` Separador S 
    p14:           | ε
}
```

### Gramática Independente de Contexto final

Para obter esta gramática apenas se colocou em evidência os prefixos comuns, criando assim mais símbolos não-terminais.

T = {`?`, `!`, `=`, `+`, `-`, `*`, `/`, `num`, `id_var`, `\n`}

N = {S, Value, Exp, Exp2, Termo, Termo2, Fator}

S = Z

```
p = {
        p1:          S → `?` Exp Separador
        p2:            | `!` Exp Separador
        p3:            | `id_var` `=` Exp Separador
        p4:            | ε
        p5:        Exp → Termo Exp2
        p6:       Exp2 → `+` Exp
        p7:            | `-` Exp
        p8:            | ε
        p9:      Termo → Fator Termo2
        p10:     Termo2 → `*` Termo
        p11:           | `/` Termo
        p12:           | ε
        p13:     Fator → `(` Exp `)`
        p14:           | num
        p15:           | id_var
        p16: Separador → `\n` Separador S 
        p17:           | ε
}
```

### Look Ahead

LA(p1) = {`?`}

LA(p2) = {`!`}

LA(p3) = {`id_var`}

LA(p4) = Follow(S) = {`$`}

LA(p5) = FirstN(Termo) = FirstN(Fator) = {`(`, `num`, `id_var`}

LA(p6) = {`+`}

LA(p7) = {`-`}

LA(p8) = Follow(Exp2) = Follow(Exp) = {`)`} U FirstN(Separador) = {`)`, `\n`} U Follow(Separador) = {`)`, `\n`} U Follow(S) = {`)`, `\n`, `$`}

LA(p9) = FirstN(Fator) = {`(`, `num`, `id_var`}

LA(p10) = {`*`}

LA(p11) = {`/`}

LA(p12) = Follow(Termo2) = Follow(Termo) = FirstN(Exp2) = {`+`, `-`} U Follow(Exp2) = {`+`, `-`} U Follow(Exp) = {`+`, `-`, `)`} U FirstN(Separador) = {`+`, `-`, `)`, `\n`} U Follow(Separador) = {`+`, `-`, `)`, `\n`} U Follow(S) = {`+`, `-`, `)`, `\n`, `$`}

LA(p13) = {`(`}

LA(p14) = {`num`}

LA(p15) = {`id_var`}

LA(p16) = {`\n`}

LA(p17) = Follow(Separador) = Follow(S) = {`$`}

#### Verificar que interseção dos Look Ahead é o conjunto vazio

- LA(p1) ∩ LA(p2) ∩ LA(p3) = {`?`} ∩ {`!`} ∩ {`id_var`} = {}

- LA(p6) ∩ LA(p7) ∩ LA(p8) = {`+`} ∩ {`-`} ∩ {`)`, `\n`, `$`} = {}

- LA(p10) ∩ LA(p11) ∩ LA(p12) = {`*`} ∩ {`/`} ∩ {`+`, `-`, `)`, `\n`, `$`} = {}

- LA(p13) ∩ LA(p14) ∩ LA(p15) = {`(`} ∩ {`num`} ∩ {`id_var`} = {}

- LA(p16) ∩ LA(p17) = {`\n`} ∩ {`$`} = {}
