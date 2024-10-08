# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .create_call_agent_params_prompt import CreateCallAgentParamsPrompt
from .language import Language
from .create_call_agent_params_actions_item import CreateCallAgentParamsActionsItem
from .create_call_agent_params_voice import CreateCallAgentParamsVoice
from .create_call_agent_params_webhook import CreateCallAgentParamsWebhook
from .create_call_agent_params_vector_database import CreateCallAgentParamsVectorDatabase
from .interrupt_sensitivity import InterruptSensitivity
from .create_call_agent_params_endpointing_sensitivity import CreateCallAgentParamsEndpointingSensitivity
from .create_call_agent_params_ivr_navigation_mode import CreateCallAgentParamsIvrNavigationMode
from .create_call_agent_params_openai_account_connection import CreateCallAgentParamsOpenaiAccountConnection
from .internal_llm_fallback import InternalLlmFallback
from .create_call_agent_params_deepgram_keywords_value import CreateCallAgentParamsDeepgramKeywordsValue
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class CreateCallAgentParams(UniversalBaseModel):
    name: typing.Optional[str] = None
    prompt: CreateCallAgentParamsPrompt
    language: typing.Optional[Language] = None
    actions: typing.Optional[typing.List[CreateCallAgentParamsActionsItem]] = None
    voice: typing.Optional[CreateCallAgentParamsVoice] = None
    initial_message: typing.Optional[str] = None
    webhook: typing.Optional[CreateCallAgentParamsWebhook] = None
    vector_database: typing.Optional[CreateCallAgentParamsVectorDatabase] = None
    interrupt_sensitivity: typing.Optional[InterruptSensitivity] = None
    context_endpoint: typing.Optional[str] = None
    noise_suppression: typing.Optional[bool] = None
    endpointing_sensitivity: typing.Optional[CreateCallAgentParamsEndpointingSensitivity] = None
    ivr_navigation_mode: typing.Optional[CreateCallAgentParamsIvrNavigationMode] = None
    conversation_speed: typing.Optional[float] = None
    initial_message_delay: typing.Optional[float] = None
    openai_model_name_override: typing.Optional[str] = None
    ask_if_human_present_on_idle: typing.Optional[bool] = None
    openai_account_connection: typing.Optional[CreateCallAgentParamsOpenaiAccountConnection] = None
    run_do_not_call_detection: typing.Optional[bool] = None
    llm_fallback: typing.Optional[InternalLlmFallback] = None
    deepgram_keywords: typing.Optional[
        typing.Dict[str, typing.Optional[CreateCallAgentParamsDeepgramKeywordsValue]]
    ] = None
    idle_time_seconds: typing.Optional[int] = None
    llm_temperature: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
