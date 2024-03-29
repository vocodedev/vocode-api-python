# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import typing_extensions

from ..core.datetime_utils import serialize_datetime
from .add_to_conference_action_params_action_trigger import AddToConferenceActionParamsActionTrigger
from .add_to_conference_config import AddToConferenceConfig

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AddToConferenceActionParams(pydantic.BaseModel):
    type: typing_extensions.Literal["action_add_to_conference"]
    config: AddToConferenceConfig
    action_trigger: typing.Optional[AddToConferenceActionParamsActionTrigger]

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
