from typing import NamedTuple, Optional, Union
from dataclasses import dataclass


@dataclass
class Label:
    name: str
    value: Optional[int] = None

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value


class Instruction:
    pass

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return str(self)


class UnaryInstruction(Instruction):
    operand: Union[Label, str]

    def __init__(self, operand: Union[Label, str]):
        self.operand = operand

    def __str__(self):
        return f'{self.__class__.__name__} {self.operand}'


class SingleInstruction(Instruction):

    def __str__(self):
        return f'{self.__class__.__name__[1:]}'


class AddressDefiningOperation(UnaryInstruction):
    def eval(self):
        pass


class _Input(SingleInstruction):
    pass


class _Output(SingleInstruction):
    pass


class _Halt(SingleInstruction):
    pass


class _Clear(SingleInstruction):
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


class DEC(AddressDefiningOperation):
    def eval(self):
        return int(self.operand)


class HEX(AddressDefiningOperation):
    def eval(self):
        return int(self.operand, base=16)


Input = _Input()
Output = _Output()
Halt = _Halt()
Clear = _Clear()
