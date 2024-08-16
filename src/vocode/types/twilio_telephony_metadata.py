# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class TwilioTelephonyMetadata(UniversalBaseModel):
    type: typing.Literal["telephony_metadata_twilio"] = "telephony_metadata_twilio"
    call_sid: typing.Optional[str] = None
    call_status: typing.Optional[str] = None
    transfer_call_sid: typing.Optional[str] = None
    transfer_call_status: typing.Optional[str] = None
    conference_sid: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow