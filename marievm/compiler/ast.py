from typing import NamedTuple, Optional, Union
from dataclasses import dataclass


@dataclass
class Label:
    name: str
    value: Optional[int] = None


class Instruction:
    pass


class UnaryInstruction(Instruction):
    operand: Union[Label, str]

    def __init__(self, operand: str):
        self.operand = operand

    def __str__(self):
        return f'{self.__class__.__name__} {self.operand}'


class InstructionWithoutArgs(Instruction):
    def __str__(self):
        return f'{self.__class__.__name__[1:]}'


class _Input(InstructionWithoutArgs):
    pass


class _Output(InstructionWithoutArgs):
    pass


class _Halt(InstructionWithoutArgs):
    pass


class Add(UnaryInstruction):
    pass


class Subt(UnaryInstruction):
    pass


class Store(UnaryInstruction):
    pass


class Jump(UnaryInstruction):
    pass


class Skipcond(UnaryInstruction):
    pass


class AddI(UnaryInstruction):
    pass


class StoreI(UnaryInstruction):
    pass


class Load(UnaryInstruction):
    pass


class LoadI(UnaryInstruction):
    pass


class JumpI(UnaryInstruction):
    pass


class JnS(UnaryInstruction):
    pass


Input = _Input()
Output = _Output()
Halt = _Halt()
