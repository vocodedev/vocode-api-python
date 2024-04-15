# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .agent_actions_item import AgentActionsItem
from .agent_endpointing_sensitivity import AgentEndpointingSensitivity
from .agent_ivr_navigation_mode import AgentIvrNavigationMode
from .agent_voice import AgentVoice
from .interrupt_sensitivity import InterruptSensitivity
from .language import Language
from .open_ai_account_connection import OpenAiAccountConnection
from .pinecone_vector_database import PineconeVectorDatabase
from .prompt import Prompt
from .webhook import Webhook

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Agent(pydantic.BaseModel):
    id: str
    user_id: str
    name: typing.Optional[str]
    prompt: Prompt
    language: typing.Optional[Language]
    actions: typing.List[AgentActionsItem]
    voice: AgentVoice
    initial_message: typing.Optional[str]
    webhook: typing.Optional[Webhook]
    vector_database: typing.Optional[PineconeVectorDatabase]
    interrupt_sensitivity: typing.Optional[InterruptSensitivity]
    context_endpoint: typing.Optional[str]
    noise_suppression: typing.Optional[bool]
    endpointing_sensitivity: typing.Optional[AgentEndpointingSensitivity]
    ivr_navigation_mode: typing.Optional[AgentIvrNavigationMode]
    conversation_speed: typing.Optional[float]
    initial_message_delay: typing.Optional[float]
    openai_model_name_override: typing.Optional[str]
    ask_if_human_present_on_idle: typing.Optional[bool]
    openai_account_connection: typing.Optional[OpenAiAccountConnection]
    run_do_not_call_detection: typing.Optional[bool]
    llm_temperature: typing.Optional[float]

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
