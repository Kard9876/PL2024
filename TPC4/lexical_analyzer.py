import ply.lex as lex
import re

# List of tokens names (required)
reserved_words = {
    "select" : 'SELECT',
    "update" : 'UPDATE',
    "create" : 'CREATE',
    "from" : 'FROM',
    "where" : 'WHERE',
    "set" : 'SET',
    "drop" : 'DROP',
    "delete" : 'DELETE',
    "table" : 'TABLE'
}

tokens = [
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
] + list(reserved_words.values())

# Simple tokens' regex

def keyword_type(t):
    match t.type:
        case "SELECT":
            t.lexer.prev_val = "FIELD_NAME"

        case "UPDATE":
            t.lexer.prev_val = "TABLE_NAME"

        case "FROM":
            t.lexer.prev_val = "TABLE_NAME"

        case "WHERE":
            t.lexer.prev_val = "FIELD_NAME"

        case "SET":
            t.lexer.prev_val = "FIELD_NAME"

        case "TABLE":
            t.lexer.prev_val = "TABLE_NAME"

        case _ : 
            print("Error applying keyword type")

    return t

def t_NUMBER(t):
    r'[+\-]?\d+(\.\d+)?'

    return t

def t_FIELD(t):
    r'\w+'

    t.type = reserved_words.get(t.value.lower(), t.lexer.prev_val)

    if t.type != t.lexer.prev_val:
        t = keyword_type(t)

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

lexer.prev_val = ""

test_data = """
    Select id, nome, salario FROM empregados WHERE salário >= 820;
    UPDATE Empregados SET salário = 1000 WHERE salário < 1000;
"""

lexer.input(test_data)

for tok in lexer:
    print(tok)