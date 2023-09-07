# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .create_call_agent_params_actions_item import CreateCallAgentParamsActionsItem
from .create_call_agent_params_endpointing_sensitivity import CreateCallAgentParamsEndpointingSensitivity
from .create_call_agent_params_ivr_navigation_mode import CreateCallAgentParamsIvrNavigationMode
from .create_call_agent_params_prompt import CreateCallAgentParamsPrompt
from .create_call_agent_params_vector_database import CreateCallAgentParamsVectorDatabase
from .create_call_agent_params_voice import CreateCallAgentParamsVoice
from .create_call_agent_params_webhook import CreateCallAgentParamsWebhook
from .interrupt_sensitivity import InterruptSensitivity
from .language import Language


class CreateCallAgentParams(pydantic.BaseModel):
    prompt: CreateCallAgentParamsPrompt
    language: typing.Optional[Language]
    actions: typing.Optional[typing.List[CreateCallAgentParamsActionsItem]]
    voice: typing.Optional[CreateCallAgentParamsVoice]
    initial_message: typing.Optional[str]
    webhook: typing.Optional[CreateCallAgentParamsWebhook]
    vector_database: typing.Optional[CreateCallAgentParamsVectorDatabase]
    interrupt_sensitivity: typing.Optional[InterruptSensitivity]
    context_endpoint: typing.Optional[str]
    noise_suppression: typing.Optional[bool]
    endpointing_sensitivity: typing.Optional[CreateCallAgentParamsEndpointingSensitivity]
    ivr_navigation_mode: typing.Optional[CreateCallAgentParamsIvrNavigationMode]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
