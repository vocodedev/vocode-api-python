# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AgentUpdateParamsIvrNavigationMode(str, enum.Enum):
    DEFAULT = "default"
    OFF = "off"

    def visit(self, default: typing.Callable[[], T_Result], off: typing.Callable[[], T_Result]) -> T_Result:
        if self is AgentUpdateParamsIvrNavigationMode.DEFAULT:
            return default()
        if self is AgentUpdateParamsIvrNavigationMode.OFF:
            return off()
