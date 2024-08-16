# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .internal_llm_fallback_provider import InternalLlmFallbackProvider
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class InternalLlmFallback(UniversalBaseModel):
    provider: InternalLlmFallbackProvider
    model_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow