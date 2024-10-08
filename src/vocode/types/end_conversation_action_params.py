# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .empty_action_config import EmptyActionConfig
from .end_conversation_action_params_action_trigger import EndConversationActionParamsActionTrigger
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class EndConversationActionParams(UniversalBaseModel):
    type: typing.Literal["action_end_conversation"] = "action_end_conversation"
    config: typing.Optional[EmptyActionConfig] = None
    action_trigger: typing.Optional[EndConversationActionParamsActionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
