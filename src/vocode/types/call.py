# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .call_agent import CallAgent
from .call_status import CallStatus


class Call(pydantic.BaseModel):
    id: str
    user_id: str
    to_number: str
    from_number: str
    agent: CallAgent
    goal: typing.Optional[str]
    transcript: typing.Optional[str]
    recording_url: typing.Optional[str]
    status: CallStatus

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
