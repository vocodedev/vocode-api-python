# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .plan_type import PlanType
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class Usage(UniversalBaseModel):
    user_id: str
    plan_type: PlanType
    monthly_usage_minutes: int
    monthly_usage_limit_minutes: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
