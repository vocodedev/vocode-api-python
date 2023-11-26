# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class NormalizedCallOnNoHumanAnswer(str, enum.Enum):
    CONTINUE = "continue"
    HANGUP = "hangup"

    def visit(self, continue_: typing.Callable[[], T_Result], hangup: typing.Callable[[], T_Result]) -> T_Result:
        if self is NormalizedCallOnNoHumanAnswer.CONTINUE:
            return continue_()
        if self is NormalizedCallOnNoHumanAnswer.HANGUP:
            return hangup()