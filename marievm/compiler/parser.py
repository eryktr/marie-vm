import ply.yacc as yacc

import marievm.compiler.ast as ast
from compiler.errors import InvalidSkipcondModeError, InvalidSyntaxError

from marievm.compiler.lexer import tokens


def p_program(p):
    'program : instructions'
    p[0] = p[1]


def p_instructions_instructions(p):
    'instructions : instruction instructions'
    p[0] = [p[1]] + p[2]


def p_instructions_instruction(p):
    'instructions : instruction'
    p[0] = [p[1]]


def p_instruction_unary_instruction(p):
    'instruction : unary_instruction'
    p[0] = p[1]


def p_unary_instruction_add(p):
    'unary_instruction : ADD operand NEWLINE'
    p[0] = ast.Add(p[2])


def p_unary_instruction_subt(p):
    'unary_instruction : SUBT operand NEWLINE'
    p[0] = ast.Subt(p[2])


def p_unary_instruction_load(p):
    'unary_instruction : LOAD operand NEWLINE'
    p[0] = ast.Load(p[2])


def p_unary_instruction_store(p):
    'unary_instruction : STORE operand NEWLINE'
    p[0] = ast.Store(p[2])


def p_unary_instruction_skipcond(p):
    'unary_instruction : SKIPCOND operand NEWLINE'
    mode = p[2]
    if mode not in ('000', '400', '800'):
        raise InvalidSkipcondModeError(p.lexer.lineno, mode)
    p[0] = ast.Skipcond(mode)


def p_operand_num(p):
    'operand : NUM'
    p[0] = p[1]


def p_operand_id(p):
    'operand : ID'
    p[0] = ast.Label(name=p[1])


def p_instruction_single_instruction(p):
    'instruction : single_instruction'
    p[0] = p[1]


def p_single_instruction_halt(p):
    'single_instruction : HALT NEWLINE'
    p[0] = ast.Halt


def p_single_instruction_input(p):
    'single_instruction : INPUT NEWLINE'
    p[0] = ast.Input


def p_single_instruction_clear(p):
    'single_instruction : CLEAR NEWLINE'
    p[0] = ast.Clear


def p_single_instruction_output(p):
    'single_instruction : OUTPUT NEWLINE'
    p[0] = ast.Output


def p_intruction_instruction_with_label(p):
    'instruction : ID COMMA address_defining_instruction NEWLINE'
    p[0] = ast.Label(name=p[1], value=p[3])


def p_address_defining_instruction_dec(p):
    'address_defining_instruction : DEC operand'
    p[0] = ast.DEC(p[2])


def p_address_defining_instruction_hex(p):
    'address_defining_instruction : HEX operand'
    p[0] = ast.HEX(p[2])


def p_error(p):
    raise InvalidSyntaxError(p.lexer.lineno, p.value)


parser = yacc.yacc(debug=0, write_tables=0)
