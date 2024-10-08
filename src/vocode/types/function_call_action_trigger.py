# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .function_call_action_trigger_config import FunctionCallActionTriggerConfig
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class FunctionCallActionTrigger(UniversalBaseModel):
    type: typing.Literal["action_trigger_function_call"] = "action_trigger_function_call"
    config: typing.Optional[FunctionCallActionTriggerConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
