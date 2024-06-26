# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .add_to_conference_action_update_params import AddToConferenceActionUpdateParams
from .dtmf_action_update_params import DtmfActionUpdateParams
from .end_conversation_action_update_params import EndConversationActionUpdateParams
from .external_action_update_params import ExternalActionUpdateParams
from .set_hold_action_update_params import SetHoldActionUpdateParams
from .transfer_call_action_update_params import TransferCallActionUpdateParams


class AgentUpdateParamsActionsItemOne_ActionTransferCall(
    TransferCallActionUpdateParams
):

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class AgentUpdateParamsActionsItemOne_ActionEndConversation(
    EndConversationActionUpdateParams
):

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class AgentUpdateParamsActionsItemOne_ActionDtmf(DtmfActionUpdateParams):
    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class AgentUpdateParamsActionsItemOne_ActionAddToConference(
    AddToConferenceActionUpdateParams
):
    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class AgentUpdateParamsActionsItemOne_ActionSetHold(SetHoldActionUpdateParams):
    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class AgentUpdateParamsActionsItemOne_ActionExternal(ExternalActionUpdateParams):
    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


AgentUpdateParamsActionsItemOne = typing.Union[
    TransferCallActionUpdateParams,
    EndConversationActionUpdateParams,
    DtmfActionUpdateParams,
    AddToConferenceActionUpdateParams,
    SetHoldActionUpdateParams,
    ExternalActionUpdateParams,
]
