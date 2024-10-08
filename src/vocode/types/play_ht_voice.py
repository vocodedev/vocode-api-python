# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .play_ht_voice_version import PlayHtVoiceVersion
from .play_ht_voice_quality import PlayHtVoiceQuality
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PlayHtVoice(UniversalBaseModel):
    id: str
    user_id: str
    type: typing.Literal["voice_play_ht"] = "voice_play_ht"
    voice_id: str
    api_user_id: typing.Optional[str] = None
    api_key: typing.Optional[str] = None
    version: typing.Optional[PlayHtVoiceVersion] = None
    speed: typing.Optional[float] = None
    quality: typing.Optional[PlayHtVoiceQuality] = None
    temperature: typing.Optional[float] = None
    top_p: typing.Optional[float] = None
    text_guidance: typing.Optional[float] = None
    voice_guidance: typing.Optional[float] = None
    experimental_remove_silence: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
