# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .azure_voice_update_params import AzureVoiceUpdateParams
from .eleven_labs_voice_update_params import ElevenLabsVoiceUpdateParams
from .play_ht_voice_update_params import PlayHtVoiceUpdateParams
from .rime_voice_update_params import RimeVoiceUpdateParams


class AgentUpdateParamsVoiceOne_VoiceAzure(AzureVoiceUpdateParams):
    type: typing_extensions.Literal["voice_azure"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class AgentUpdateParamsVoiceOne_VoiceRime(RimeVoiceUpdateParams):
    type: typing_extensions.Literal["voice_rime"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class AgentUpdateParamsVoiceOne_VoiceElevenLabs(ElevenLabsVoiceUpdateParams):
    type: typing_extensions.Literal["voice_eleven_labs"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class AgentUpdateParamsVoiceOne_VoicePlayHt(PlayHtVoiceUpdateParams):
    type: typing_extensions.Literal["voice_play_ht"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


AgentUpdateParamsVoiceOne = typing.Union[
    AgentUpdateParamsVoiceOne_VoiceAzure,
    AgentUpdateParamsVoiceOne_VoiceRime,
    AgentUpdateParamsVoiceOne_VoiceElevenLabs,
    AgentUpdateParamsVoiceOne_VoicePlayHt,
]
