# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .open_ai_account_connection_update_params import OpenAiAccountConnectionUpdateParams
from .twilio_account_connection_update_params import TwilioAccountConnectionUpdateParams


class AccountConnectionUpdateParamsRequest_AccountConnectionTwilio(TwilioAccountConnectionUpdateParams):
    type: typing_extensions.Literal["account_connection_twilio"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class AccountConnectionUpdateParamsRequest_AccountConnectionOpenai(OpenAiAccountConnectionUpdateParams):
    type: typing_extensions.Literal["account_connection_openai"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


AccountConnectionUpdateParamsRequest = typing.Union[
    AccountConnectionUpdateParamsRequest_AccountConnectionTwilio,
    AccountConnectionUpdateParamsRequest_AccountConnectionOpenai,
]
