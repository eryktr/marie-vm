import ply.lex as lex

from compiler.errors import TooManyNewlinesError
from marievm.compiler.errors import InvalidTokenError

reserved = {
    'JnS': 'JNS',
    'Load': 'LOAD',
    'LoadI': 'LOADI',
    'Store': 'STORE',
    'StoreI': 'STOREI',
    'Add': 'ADD',
    'AddI': 'ADDI',
    'Subt': 'SUBT',
    'Input': 'INPUT',
    'Output': 'OUTPUT',
    'Skipcond': 'SKIPCOND',
    'Jump': 'JUMP',
    'JumpI': 'JUMPI',
    'Clear': 'CLEAR',
    'Halt': 'HALT',
    'DEC': 'DEC',
    'HEX': 'HEX',
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
    'HALT',
    'INPUT',
    'OUTPUT',
    'SKIPCOND',
    'JUMP',
    'JUMPI',
    'CLEAR',
    'DEC',
    'HEX',
    'NUM',
    'COMMA',
    'NEWLINE',
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
t_HALT = r'Halt'
t_DEC = r'DEC'
t_HEX = r'HEX'
t_NUM = r'[0-9]+'
t_COMMA = r','
t_ignore = r' \t'


def t_NEWLINE(t):
    r'\n+'
    num_newlines = len(t.value)
    if num_newlines > 2:
        raise TooManyNewlinesError(t)
    t.lexer.lineno += num_newlines
    return t


def t_ID(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t


def t_error(t):
    raise InvalidTokenError(t)


lexer = lex.lex()
