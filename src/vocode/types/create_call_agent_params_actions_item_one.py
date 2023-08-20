# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .dtmf_action_params import DtmfActionParams
from .end_conversation_action_params import EndConversationActionParams
from .transfer_call_action_params import TransferCallActionParams


class CreateCallAgentParamsActionsItemOne_ActionTransferCall(TransferCallActionParams):

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class CreateCallAgentParamsActionsItemOne_ActionEndConversation(EndConversationActionParams):

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class CreateCallAgentParamsActionsItemOne_ActionDtmf(DtmfActionParams):

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


CreateCallAgentParamsActionsItemOne = typing.Union[
    TransferCallActionParams,
    EndConversationActionParams,
    DtmfActionParams,
]
