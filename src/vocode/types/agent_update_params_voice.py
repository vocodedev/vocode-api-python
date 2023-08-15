# This file was auto-generated by Fern from our API Definition.

import typing

from .azure_voice_update_params import AzureVoiceUpdateParams
from .eleven_labs_voice_update_params import ElevenLabsVoiceUpdateParams
from .play_ht_voice_update_params import PlayHtVoiceUpdateParams
from .rime_voice_update_params import RimeVoiceUpdateParams
from .undefined import Undefined

AgentUpdateParamsVoice = typing.Union[
    str, AzureVoiceUpdateParams, RimeVoiceUpdateParams, ElevenLabsVoiceUpdateParams, PlayHtVoiceUpdateParams, Undefined
]
