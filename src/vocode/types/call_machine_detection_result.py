# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CallMachineDetectionResult(str, enum.Enum):
    HUMAN = "human"
    MACHINE = "machine"

    def visit(self, human: typing.Callable[[], T_Result], machine: typing.Callable[[], T_Result]) -> T_Result:
        if self is CallMachineDetectionResult.HUMAN:
            return human()
        if self is CallMachineDetectionResult.MACHINE:
            return machine()