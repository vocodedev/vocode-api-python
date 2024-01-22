# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ..core.datetime_utils import serialize_datetime
from .azure_voice_update_params_pitch import AzureVoiceUpdateParamsPitch
from .azure_voice_update_params_rate import AzureVoiceUpdateParamsRate
from .azure_voice_update_params_voice_name import AzureVoiceUpdateParamsVoiceName

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AzureVoiceUpdateParams(pydantic.BaseModel):
    type: typing_extensions.Literal["voice_azure"]
    voice_name: typing.Optional[AzureVoiceUpdateParamsVoiceName]
    pitch: typing.Optional[AzureVoiceUpdateParamsPitch]
    rate: typing.Optional[AzureVoiceUpdateParamsRate]

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
