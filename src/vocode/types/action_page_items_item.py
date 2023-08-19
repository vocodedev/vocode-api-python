# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .dtmf_action import DtmfAction
from .end_conversation_action import EndConversationAction
from .transfer_call_action import TransferCallAction


class ActionPageItemsItem_ActionTransferCall(TransferCallAction):
    type: typing_extensions.Literal["action_transfer_call"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ActionPageItemsItem_ActionEndConversation(EndConversationAction):
    type: typing_extensions.Literal["action_end_conversation"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ActionPageItemsItem_ActionDtmf(DtmfAction):
    type: typing_extensions.Literal["action_dtmf"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


ActionPageItemsItem = typing.Union[
    ActionPageItemsItem_ActionTransferCall, ActionPageItemsItem_ActionEndConversation, ActionPageItemsItem_ActionDtmf
]
