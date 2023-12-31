# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BuyPhoneNumberRequestTelephonyProvider(str, enum.Enum):
    VONAGE = "vonage"
    TWILIO = "twilio"

    def visit(self, vonage: typing.Callable[[], T_Result], twilio: typing.Callable[[], T_Result]) -> T_Result:
        if self is BuyPhoneNumberRequestTelephonyProvider.VONAGE:
            return vonage()
        if self is BuyPhoneNumberRequestTelephonyProvider.TWILIO:
            return twilio()
