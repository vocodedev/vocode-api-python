# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .azure_voice import AzureVoice
from .eleven_labs_voice import ElevenLabsVoice
from .play_ht_voice import PlayHtVoice
from .rime_voice import RimeVoice


class VoiceResponseModel_VoiceAzure(AzureVoice):
    type: typing_extensions.Literal["voice_azure"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class VoiceResponseModel_VoiceRime(RimeVoice):
    type: typing_extensions.Literal["voice_rime"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class VoiceResponseModel_VoiceElevenLabs(ElevenLabsVoice):
    type: typing_extensions.Literal["voice_eleven_labs"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class VoiceResponseModel_VoicePlayHt(PlayHtVoice):
    type: typing_extensions.Literal["voice_play_ht"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


VoiceResponseModel = typing.Union[
    VoiceResponseModel_VoiceAzure,
    VoiceResponseModel_VoiceRime,
    VoiceResponseModel_VoiceElevenLabs,
    VoiceResponseModel_VoicePlayHt,
]
