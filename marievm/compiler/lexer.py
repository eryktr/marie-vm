import ply.lex as lex

from marievm.compiler.errors import InvalidTokenError

reserved = {
    'JnS': 'JNS',
    'Load': 'LOAD',
}

tokens = (
    'ID',
    'JNS',
    'LOAD',
    'LOADI',
    'STORE',
    'STOREI',
    'ADD',
    'ADDI',
    'SUBT',
    'INPUT',
    'OUTPUT',
    'SKIPCOND',
    'JUMP',
    'JUMPI',
    'CLEAR',
    'DEC',
    'NUM',
    'COMMA',
)

t_JNS = r'JnS'
t_LOAD = r'Load'
t_LOADI = r'LoadI'
t_STORE = r'Store'
t_STOREI = r'StoreI'
t_ADD = r'Add'
t_ADDI = r'AddI'
t_SUBT = r'Subt'
t_INPUT = r'Input'
t_OUTPUT = r'Output'
t_SKIPCOND = r'Skipcond'
t_JUMP = r'Jump'
t_JUMPI = r'JumpI'
t_CLEAR = r'Clear'
t_DEC = r'DEC'
t_ID = r'[A-Za-z][A-Za-z0-9_]*'
t_NUM = r'[0-9]+'
t_COMMA = r','
t_ignore = r' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    raise InvalidTokenError(t)


lexer = lex.lex()
