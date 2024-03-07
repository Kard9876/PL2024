import ply.lex as lex
import re

# List of tokens names (required)
tokens = (
    'SELECT',
    'UPDATE',
    'CREATE',
    'FROM',
    'WHERE',
    'SET',
    'DROP',
    'DELETE',
    'TABLE',
    'GREATER',
    'LESSER',
    'EQUALS',
    'COMMA',
    'SEMICOLON',
    'LPAREN',
    'RPAREN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'SKIP',
    'FIELD',
    'NUMBER',
    'FIELD_NAME',
    'TABLE_NAME'
)

prev_val = ""

# Simple tokens' regex

def t_SELECT(t):
    r'SELECT'

    global prev_val
    prev_val = "FIELD_NAME"

    return t

def t_UPDATE(t):
    r'UPDATE'

    global prev_val
    prev_val = "TABLE_NAME"

    return t

def t_FROM(t):
    r'FROM'

    global prev_val
    prev_val = "TABLE_NAME"

    return t

def t_WHERE(t):
    r'WHERE'

    global prev_val
    prev_val = "FIELD_NAME"

    return t

def t_SET(t):
    r'SET'

    global prev_val
    prev_val = "FIELD_NAME"

    return t

def t_TABLE(t):
    r'TABLE'

    global prev_val
    prev_val = "TABLE_NAME"

    return t

def t_NUMBER(t):
    r'[+\-]?\d+(\.\d+)?'

    return t

def t_FIELD(t):
    r'\w+'

    global prev_val
    t.type = prev_val

    return t

t_DROP = r'DROP'
t_CREATE = r'CREATE'
t_GREATER = r'>'
t_LESSER = r'<'
t_EQUALS = r'='
t_COMMA = r','
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)' 
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_SKIP = r'\s'

# Rule to keep track of line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Invalid characters
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build lexer
lexer = lex.lex()

test_data = """
    SELECT id, nome, salario FROM empregados WHERE salário >= 820;
    UPDATE Empregados SET salário = 1000 WHERE salário < 1000;
"""

lexer.input(test_data)

for tok in lexer:
    print(tok)