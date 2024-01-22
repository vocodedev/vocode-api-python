# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from ....types.add_to_conference_action_params import AddToConferenceActionParams
from ....types.dtmf_action_params import DtmfActionParams
from ....types.end_conversation_action_params import EndConversationActionParams
from ....types.set_hold_action_params import SetHoldActionParams
from ....types.transfer_call_action_params import TransferCallActionParams


class AgentParamsActionsItemOne_ActionTransferCall(TransferCallActionParams):
    type: typing_extensions.Literal["action_transfer_call"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class AgentParamsActionsItemOne_ActionEndConversation(EndConversationActionParams):
    type: typing_extensions.Literal["action_end_conversation"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class AgentParamsActionsItemOne_ActionDtmf(DtmfActionParams):
    type: typing_extensions.Literal["action_dtmf"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class AgentParamsActionsItemOne_ActionAddToConference(AddToConferenceActionParams):
    type: typing_extensions.Literal["action_add_to_conference"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class AgentParamsActionsItemOne_ActionSetHold(SetHoldActionParams):
    type: typing_extensions.Literal["action_set_hold"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


AgentParamsActionsItemOne = typing.Union[
    AgentParamsActionsItemOne_ActionTransferCall,
    AgentParamsActionsItemOne_ActionEndConversation,
    AgentParamsActionsItemOne_ActionDtmf,
    AgentParamsActionsItemOne_ActionAddToConference,
    AgentParamsActionsItemOne_ActionSetHold,
]