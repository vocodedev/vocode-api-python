# This file was auto-generated by Fern from our API Definition.

import typing

from .azure_voice import AzureVoice
from .eleven_labs_voice import ElevenLabsVoice
from .rime_voice import RimeVoice

CreateVoiceResponse = typing.Union[AzureVoice, RimeVoice, ElevenLabsVoice]
