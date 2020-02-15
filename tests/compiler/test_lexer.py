from pathlib import Path

import pytest
import copy

from marievm.compiler.errors import InvalidTokenError
from marievm.compiler import lexer

_lex = lexer.lexer
_VALID_FILES_PATH = Path(__file__).parent / 'valid_files'
_INVALID_FILES_PATH = Path(__file__).parent / 'invalid_files'


@pytest.mark.parametrize('filename', [
    'valid_code_with_labels.mar',
    'all_valid_instrs.mar',

])
def test_lexer_valid_file(filename):
    lexer = copy.deepcopy(_lex)
    codepath = _VALID_FILES_PATH / filename
    code = codepath.read_text()
    lexer.input(code)
    list(lexer)


@pytest.mark.parametrize('filename, lineno, val', [
    ('invalid_instr.mar', 4, '_'),
    ('invalid_num.mar', 1, '-'),
])
def test_lexer_invalid_token(filename, lineno, val):
    lexer = copy.deepcopy(_lex)
    codepath = _INVALID_FILES_PATH / filename
    code = codepath.read_text()
    with pytest.raises(InvalidTokenError) as err:
        lexer.input(code)
        list(lexer)
    assert lineno == err.value.lineno
    assert val == err.value.val
