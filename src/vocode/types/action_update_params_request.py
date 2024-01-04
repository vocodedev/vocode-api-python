# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .add_to_conference_action_update_params import AddToConferenceActionUpdateParams
from .dtmf_action_update_params import DtmfActionUpdateParams
from .end_conversation_action_update_params import EndConversationActionUpdateParams
from .set_hold_action_update_params import SetHoldActionUpdateParams
from .transfer_call_action_update_params import TransferCallActionUpdateParams


class ActionUpdateParamsRequest_ActionTransferCall(TransferCallActionUpdateParams):
    type: typing_extensions.Literal["action_transfer_call"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ActionUpdateParamsRequest_ActionEndConversation(EndConversationActionUpdateParams):
    type: typing_extensions.Literal["action_end_conversation"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ActionUpdateParamsRequest_ActionDtmf(DtmfActionUpdateParams):
    type: typing_extensions.Literal["action_dtmf"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ActionUpdateParamsRequest_ActionAddToConference(AddToConferenceActionUpdateParams):
    type: typing_extensions.Literal["action_add_to_conference"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ActionUpdateParamsRequest_ActionSetHold(SetHoldActionUpdateParams):
    type: typing_extensions.Literal["action_set_hold"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


ActionUpdateParamsRequest = typing.Union[
    TransferCallActionUpdateParams,
    EndConversationActionUpdateParams,
    DtmfActionUpdateParams,
    AddToConferenceActionUpdateParams,
    SetHoldActionUpdateParams,
]
