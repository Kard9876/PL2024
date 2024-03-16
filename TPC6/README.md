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

T = {`?`, `!`, `=`, `+`, `-`, `*`, `/`, `num`, `id_var`}

N = {S, Value, Exp, Termo, Fator}

S = S
```
p = {
    p1:      S → `?` Exp
    p2:        | `!` Exp
    p3:        | `id_var` `=` Exp
    p4:    Exp → Termo `+` Exp
    p5:        | Termo `-` Exp
    p6:        | Termo
    p7:  Termo → Fator `*` Termo
    p8:        | Fator `/` Termo
    p9:        | Fator
    p10: Fator → `(` Exp `)`
    p11:       | num
    p12:       | id_var
}
```

### Gramática Independente de Contexto final

Para obter esta gramática apenas se colocou em evidência os prefixos comuns, criando assim mais símbolos não-terminais.

T = {`?`, `!`, `=`, `+`, `-`, `*`, `/`, `num`, `id_var`}

N = {S, Value, Exp, Exp2, Termo, Termo2, Fator}

S = Z

```
p = {
        p1:      S → `?` Exp
        p2:        | `!` Exp
        p3:        | `id_var` `=` Exp
        p4:    Exp → Termo Exp2
        p5:   Exp2 → `+` Exp
        p6:        | `-` Exp
        p7:        | ε
        p8:  Termo → Fator Termo2
        p9: Termo2 → `*` Termo
        p10:       | `/` Termo
        p11:       | ε
        p12: Fator → `(` Exp `)`
        p13:       | num
        p14:       | id_var
}
```

### Look Ahead

LA(p1) = {`?`}

LA(p2) = {`!`}

LA(p3) = {`id_var`}

LA(p4) = FirstN(Termo) = FirstN(Fator) = {`(`, `num`, `id_var`}

LA(p5) = {`+`}

LA(p6) = {`-`}

LA(p7) = Follow(Exp2) = Follow(Exp) = {`)`} U Follow(S) = {`)`, `$`}

LA(p8) = FirstN(Fator) = {`(`, `num`, `id_var`}

LA(p9) = {`*`}

LA(p10) = {`/`}

LA(p11) = Follow(Termo2) = Follow(Termo) = FirstN(Exp2) = {`+`, `-`} U Follow(Exp2) = {`+`, `-`} U Follow(Exp) = {`+`, `-`, `)`} U Follow(S) = {`+`, `-`, `)`, `$`}

LA(p12) = {`(`}

LA(p13) = {`num`}

LA(p14) = {`id_var`}

#### Verificar que interseção dos Look Ahead é o conjunto vazio

- LA(p1) ∩ LA(p2) ∩ LA(p3) = {`?`} ∩ {`!`} ∩ {`id_var`} = {}

- LA(p5) ∩ LA(p6) ∩ LA(p7) = {`+`} ∩ {`-`} ∩ {`)`, `$`} = {}

- LA(p9) ∩ LA(p10) ∩ LA(p11) = {`*`} ∩ {`/`} ∩ {`+`, `-`, `)`, `$`} = {}

- LA(p12) ∩ LA(p13) ∩ LA(p14) = {`(`} ∩ {`num`} ∩ {`id_var`} = {}
