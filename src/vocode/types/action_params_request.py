# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .dtmf_action_params import DtmfActionParams
from .end_conversation_action_params import EndConversationActionParams
from .transfer_call_action_params import TransferCallActionParams


class ActionParamsRequest_ActionTransferCall(TransferCallActionParams):
    type: typing_extensions.Literal["action_transfer_call"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ActionParamsRequest_ActionEndConversation(EndConversationActionParams):
    type: typing_extensions.Literal["action_end_conversation"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ActionParamsRequest_ActionDtmf(DtmfActionParams):
    type: typing_extensions.Literal["action_dtmf"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


ActionParamsRequest = typing.Union[
    ActionParamsRequest_ActionTransferCall, ActionParamsRequest_ActionEndConversation, ActionParamsRequest_ActionDtmf
]