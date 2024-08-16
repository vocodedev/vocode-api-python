# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ElevenLabsVoiceParams(UniversalBaseModel):
    type: typing.Literal["voice_eleven_labs"] = "voice_eleven_labs"
    voice_id: str
    stability: typing.Optional[float] = None
    similarity_boost: typing.Optional[float] = None
    api_key: typing.Optional[str] = None
    optimize_streaming_latency: typing.Optional[int] = None
    model_id: typing.Optional[str] = None
    experimental_input_streaming: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
