import ply.lex as lex

import sys
import re
import json

class Vending_Machine(object):
    states = [
        ('LISTING', 'inclusive'),
        ('INPUT', 'inclusive'),
        ('SELECT', 'inclusive'),
        ('LEAVE', 'inclusive'),
        ('ADD', 'inclusive')
    ]

    keyword_states = {
        "LISTAR": "LISTING",
        "SELECIONAR": "SELECT",
        "MOEDA": "INPUT",
        "SAIR": "LEAVE",
        "ADICIONAR": "ADD"
    }

    reserverd_words = {
        "listar": "LISTAR",
        "selecionar": "SELECIONAR",
        "moeda": "MOEDA",
        "sair": "SAIR",
        "adicionar": "ADICIONAR"
    }

    tokens = [
        'NUMBER',
        'KEYWORD',
        'OPTION',
        'UNKNOWN_KEYWORD',
        'COIN'
    ] + list(reserverd_words.values())
    
    def __init__(self, produtos):
        self.saldo = 0
        self.produtos = produtos

        self.leave = False
    
    def coin_value(self, num):
        cur = float(num[:-1])

        if num[-1] == 'e':
            cur *= 100

        return cur
    
    def get_saldo(self):
        return f"Saldo= {'%0.0f'%(self.saldo,) + 'c' if self.saldo < 100 else '%0.2f'%(self.saldo / 100,) + 'e'}"

    def prod_val(self, prod_val):
        return f"{'%0.0f'%(prod_val,) + 'c' if prod_val < 100 else '%0.2f'%(prod_val / 100,) + 'e'}"
    
    def process_request(self, opt):
        produto = self.produtos.get(opt, "Invalido")

        if produto == "Invalido":
            print("A máquina não possui o prodruto desejado.")
            print(f"maq: {self.get_saldo()}")

        elif produto[2] <= 0:
            print("A máquina não possui quantidade suficiente do prodruto desejado.")
            print(f"maq: {self.get_saldo()}")

        else: 
            val = produto[1]

            if self.saldo - val < 0:
                print("maq: Saldo insufuciente para satisfazer o seu pedido")
                print(f"maq: {self.get_saldo()}; Pedido = {self.prod_val(produto[1])}")

            else:
                print("Compra bem sucedida")
                self.saldo -= val
                self.produtos[opt] = (produto[0], produto[1], produto[2]-1)
                
                print(f'maq: Pode retirar o produto dispensado "{produto[0]}"')
                print(f"maq: {self.get_saldo()}")


    def return_change(self):
        troco = {}
        troco_str = ""

        while self.saldo > 0:

            count = 0
            coin = ""

            if self.saldo >= 200:
                self.saldo -= 200
                coin = "2e"
                count = troco.get(coin, 0) + 1

            elif self.saldo >= 100:
                self.saldo -= 100
                coin = "1e"
                count = troco.get(coin, 0) + 1

            elif self.saldo >= 50:
                self.saldo -= 50
                coin = "50c"
                count = troco.get(coin, 0) + 1

            elif self.saldo >= 20:
                self.saldo -= 20
                coin = "20c"
                count = troco.get(coin, 0) + 1

            elif self.saldo >= 10:
                self.saldo -= 10
                coin = "10c"
                count = troco.get(coin, 0) + 1

            elif self.saldo >= 5:
                self.saldo -= 5
                coin = "5c"
                count = troco.get(coin, 0) + 1

            elif self.saldo >= 2:
                self.saldo -= 2
                coin = "2c"
                count = troco.get(coin, 0) + 1

            elif self.saldo >= 1:
                self.saldo -= 1
                coin = "1c"
                count = troco.get(coin, 0) + 1

            else:
                print(self.saldo)
                coin = "Unknown"

            troco[coin] = count

        for (k, v) in troco.items():
            troco_str += f"{v}x {k}    "

        print(f"Pode retirar o troco: {troco_str}")
        pass
    
    def t_INPUT_NUMBER(self, t):
        r'\d+(c|e)'

        t.type = 'COIN'

        self.saldo += self.coin_value(t.value)

        return t
    
    def t_SELECT_NUMBER(self, t):
        r'\d+'

        t.type = 'OPTION'

        self.process_request(t.value)

        return t

    def t_KEYWORD(self, t):
        r'\w+'

        t.type = self.reserverd_words.get(t.value.lower(), "UNKNOWN_KEYWORD")

        if t.type == "UNKNOWN_KEYWORD":
            match t.lexer.lexstate:
                case "INPUT":
                    print('O formato da moeda não é o expectável. Indica a moeda no formato Number(c|e).')
                case _:
                    print("Unkown keyword received")

            t.lexer.begin('INITIAL')

        else:
            t.lexer.begin(self.keyword_states.get(t.type, "UNKNOWN_TYPE"))

        return t
    
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_LISTING_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

        print("maq:")

        for (k, v) in self.produtos.items():
            print(f"Cod: {k},  Nome: {v[0]},  Quantidade: {v[2]},  Preço:{'%0.0f'%(v[1],) + 'c' if v[1] < 100 else '%0.2f'%(v[1] / 100,) + 'e'}")

        t.lexer.begin('INITIAL')
    
    def t_INPUT_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

        print(f"Saldo: {'%0.0f'%(self.saldo,) + 'c' if self.saldo < 100 else '%0.2f'%(self.saldo / 100,) + 'e'}")

        t.lexer.begin('INITIAL')

    def t_SELECT_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

        t.lexer.begin('INITIAL')

    def t_LEAVE_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

        self.return_change()

        self.leave = True

        t.lexer.begin('INITIAL')

    def t_ADD_KEYWORD(self, t):
        r'.+'

        t.value = re.sub(r',', r' ', t.value)
        t.value = re.sub(r'\s+', r' ', t.value)

        tmp_words = re.split(r'(\s|(\"|\').*?(\"|\'))', t.value)

        words = []

        for w in tmp_words:
            if w:
                w = w.replace('\'', '')
                w = w.replace('"', '')
                
                if w and re.search(r'^(\s*"?\'?)*$', w) is None:

                    words.append(w)

        if len(words) == 2:
            prod = self.produtos.get(words[0], "Inválido")

            if prod == "Inválido":
                print("maq: O código do produto a adicionar não existe")

            else:
                print("maq: Produto adicionado com sucesso")
                self.produtos[words[0]] = (prod[0], prod[1], prod[2] + int(words[1]))

        elif len(words) == 4:
            print("maq: Produto adicionado com sucesso")
            self.produtos[words[0]] = (words[1], float(words[2]) * 100, int(words[3]))

        else:
            print("maq: Número incorreto de argumentos.")
            print("maq: ADICIONAR [Cod Quant | Cod Nome Preco Quant]")
            print(words)

        return t
    
    def t_ADD_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

        t.lexer.begin('INITIAL')

    t_ignore  = ' \t,'

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
    
    def build(self, **kwargs):
        self.lexer = lex.lex(object=self, **kwargs)

    def run(self):

        for line in sys.stdin:
            self.lexer.input(line)

            for _ in self.lexer:
                pass

            if self.leave:
                return self.produtos


def main(args):
    if len(args) < 2:
        print("Not enough arguments. Please insert the filename of the stock's json.")
    else :
        json_file = open(args[1], 'rt')

        json_db = json.load(json_file)

        json_file.close()

        produtos = {}

        for reg in json_db["stock"]:
            produtos[reg["cod"]] = (reg["nome"], reg["preco"] * 100, reg["quant"])

        vending_machine = Vending_Machine(produtos)

        vending_machine.build()
        produtos = vending_machine.run()

        json_db["stock"] = []

        for (k, v) in produtos.items():
            json_db["stock"].append({
                "cod": k,
                "nome": v[0], 
                "preco": v[1] / 100,
                "quant": v[2]
            })

        json_file = open(args[1], 'wt')

        json.dump(json_db, json_file, ensure_ascii=False)

        json_file.close()

if __name__ == "__main__":
    main(sys.argv)