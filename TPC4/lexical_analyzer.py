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
    'NUMBER'
)

# Simple tokens' regex

t_SELECT = r'SELECT'
t_UPDATE = r'UPDATE'
t_CREATE = r'CREATE'
t_FROM = r'FROM'
t_WHERE = r'WHERE'
t_SET = r'SET'
t_DROP = r'DROP'
t_DELETE = r'DELETE'
t_TABLE = r'TABLE'
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
t_FIELD = r'\w+'
t_NUMBER = r'[+\-]?\d+(\.\d+)?'

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