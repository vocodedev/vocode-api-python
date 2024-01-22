# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ..core.datetime_utils import serialize_datetime
from .eleven_labs_voice_update_params_api_key import ElevenLabsVoiceUpdateParamsApiKey
from .eleven_labs_voice_update_params_similarity_boost import ElevenLabsVoiceUpdateParamsSimilarityBoost
from .eleven_labs_voice_update_params_stability import ElevenLabsVoiceUpdateParamsStability
from .eleven_labs_voice_update_params_voice_id import ElevenLabsVoiceUpdateParamsVoiceId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ElevenLabsVoiceUpdateParams(pydantic.BaseModel):
    type: typing_extensions.Literal["voice_eleven_labs"]
    voice_id: typing.Optional[ElevenLabsVoiceUpdateParamsVoiceId]
    stability: typing.Optional[ElevenLabsVoiceUpdateParamsStability]
    similarity_boost: typing.Optional[ElevenLabsVoiceUpdateParamsSimilarityBoost]
    api_key: typing.Optional[ElevenLabsVoiceUpdateParamsApiKey]

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
