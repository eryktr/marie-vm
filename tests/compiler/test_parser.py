import pytest
import marievm.compiler.ast as ast
from compiler.ast import Label
from compiler.errors import InvalidSkipcondModeError
import marievm.compiler.parser as parse
import marievm.compiler.lexer as lex
from tests.compiler.common import VALID_FILES_PATH, INVALID_FILES_PATH


@pytest.fixture
def parser():
    parser = parse.parser
    lex.lexer.lineno = 0
    return parser


@pytest.mark.parametrize('filename, ast', [
    ('add.mar', [ast.Load(Label('X')), ast.Add(Label('Y')), ast.Store(Label('Z'))])
])
def test_parser_generates_valid_ast(filename, ast, parser):
    codepath = VALID_FILES_PATH / filename
    code = codepath.read_text()
    assert ast == parser.parse(code)


def test_parser_recognizes_invalid_skipcond_mode(parser):
    codepath = INVALID_FILES_PATH / 'invalid_skipcond.mar'
    code = codepath.read_text()
    with pytest.raises(InvalidSkipcondModeError) as err:
        parser.parse(code)
    assert '700' == err.value.mode
    assert 4 == err.value.lineno
