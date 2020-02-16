import pytest
import copy

from compiler.errors import TooManyNewlinesError
from marievm.compiler.errors import InvalidTokenError
from marievm.compiler import lexer
from tests.compiler.common import VALID_FILES_PATH, INVALID_FILES_PATH

_lex = lexer.lexer


@pytest.mark.parametrize('filename', [
    'valid_code_with_labels.mar',
    'all_valid_instrs.mar',

])
def test_lexer_valid_file(filename):
    lexer = copy.deepcopy(_lex)
    codepath = VALID_FILES_PATH / filename
    code = codepath.read_text()
    lexer.input(code)
    list(lexer)


@pytest.mark.parametrize('filename, lineno, val', [
    ('invalid_instr.mar', 4, '_'),
    ('invalid_num.mar', 1, '-'),
])
def test_lexer_invalid_token(filename, lineno, val):
    lexer = copy.deepcopy(_lex)
    codepath = INVALID_FILES_PATH / filename
    code = codepath.read_text()
    with pytest.raises(InvalidTokenError) as err:
        lexer.input(code)
        list(lexer)
    assert lineno == err.value.lineno
    assert val == err.value.val


def test_lexer_too_many_newlines():
    lexer = copy.deepcopy(_lex)
    codepath = INVALID_FILES_PATH / 'too_many_newlines.mr'
    code = codepath.read_text()
    with pytest.raises(TooManyNewlinesError) as err:
        lexer.input(code)
        list(lexer)
    assert 4 == err.value.lineno
