import ply.lex as lex

import sys
import re

class Vending_Machine(object):
    states = [
        ('LISTING', 'inclusive'),
        ('INPUT', 'inclusive'),
        ('SELECT', 'inclusive'),
        ('LEAVE', 'inclusive')
    ]

    keyword_states = {
        "LISTAR": "LISTING",
        "SELECIONAR": "SELECT",
        "MOEDA": "INPUT",
        "SAIR": "LEAVE"
    }

    reserverd_words = {
        "listar": "LISTAR",
        "selecionar": "SELECIONAR",
        "moeda": "MOEDA",
        "sair": "SAIR"
    }

    tokens = [
        'NUMBER',
        'KEYWORD',
        'OPTION',
        'UNKNOWN_KEYWORD',
        'COIN'
    ] + list(reserverd_words.values())
    
    def __init__(self):
        self.saldo = 0
        self.produtos = {
            "1": ("água", "50c"),
            "2": ("bolo", "1.50e"),
            "3": ("sandes mista", "1.00e"),
            "4": ("snickers", "2.00e"),
            "5": ("ice tea", "80c"),
            "6": ("coca cola", "1.20e"),
            "7": ("lays", "1.40e"),
            "8": ("kit kat", "1.30e"),
            "9": ("red bull", "1.50e"),
            "10": ("tuna sandwich", "1.25e")
        }

        self.leave = False
    
    def coin_value(self, num):
        cur = float(num[:-1])

        if num[-1] == 'e':
            cur *= 100

        return cur
    
    def process_request(self, opt):
        produto = self.produtos.get(opt, "Invalido")

        if produto == "Invalido":
            print("A máquina não possui o prodruto desejado")
        else: 
            val = self.coin_value(produto[1])

            if self.saldo - val < 0:
                print("Saldo insuficiente")

            else:
                print("Compra bem sucedida")
                self.saldo -= val

        print(produto[0], produto[1])
        print(f"Saldo: {'%0.0f'%(self.saldo,) + 'c' if self.saldo < 100 else '%0.2f'%(self.saldo / 100,) + 'e'}")

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
            troco_str += f"{k}: {v}\t"

        print(f"Troco: {troco_str}")
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

        for (k, v) in self.produtos.items():
            print(f"{k}: {v[0]}({v[1]})")

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

    t_ignore  = ' \t'

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
            #    print(tok)

            if self.leave:
                exit(0)

vending_machine = Vending_Machine()

vending_machine.build()
vending_machine.run()