# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .azure_voice import AzureVoice
from .eleven_labs_voice import ElevenLabsVoice
from .play_ht_voice import PlayHtVoice
from .rime_voice import RimeVoice


class VoicePageItemsItem_VoiceAzure(AzureVoice):
    type: typing_extensions.Literal["voice_azure"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class VoicePageItemsItem_VoiceRime(RimeVoice):
    type: typing_extensions.Literal["voice_rime"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class VoicePageItemsItem_VoiceElevenLabs(ElevenLabsVoice):
    type: typing_extensions.Literal["voice_eleven_labs"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class VoicePageItemsItem_VoicePlayHt(PlayHtVoice):
    type: typing_extensions.Literal["voice_play_ht"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


VoicePageItemsItem = typing.Union[
    VoicePageItemsItem_VoiceAzure,
    VoicePageItemsItem_VoiceRime,
    VoicePageItemsItem_VoiceElevenLabs,
    VoicePageItemsItem_VoicePlayHt,
]
