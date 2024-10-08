# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ExternalActionConfig(UniversalBaseModel):
    processing_mode: typing.Optional[typing.Literal["muted"]] = None
    name: str
    description: str
    url: str
    input_schema: typing.Dict[str, typing.Optional[typing.Any]]
    speak_on_send: bool
    speak_on_receive: bool
    signature_secret: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
