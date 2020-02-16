import pytest

import marievm.compiler.ast as ast


@pytest.mark.parametrize('instr, string', [
    (ast.Add('10'), 'Add 10'),
    (ast.Subt('20'), 'Subt 20'),
    (ast.JnS('1'), 'JnS 1'),
    (ast.AddI('5'), 'AddI 5'),
    (ast.Jump('0'), 'Jump 0'),
    (ast.JumpI('0'), 'JumpI 0'),
    (ast.Store('1'), 'Store 1'),
    (ast.Load('10'), 'Load 10'),
    (ast.LoadI('10'), 'LoadI 10'),
    (ast.Skipcond('400'), 'Skipcond 400'),
    (ast.DEC('10'), 'DEC 10'),
    (ast.HEX('20'), 'HEX 20'),
    (ast.Halt, 'Halt'),
    (ast.Input, 'Input'),
    (ast.Output, 'Output'),
    (ast.Clear, 'Clear'),
])
def test_instruction_to_string(instr, string):
    assert string == str(instr)


@pytest.mark.parametrize('instr, value', [
    (ast.DEC('10'), 10),
    (ast.HEX('DEAD'), 57005),
])
def test_address_specifying_instruction_eval(instr, value):
    assert value == instr.eval()
