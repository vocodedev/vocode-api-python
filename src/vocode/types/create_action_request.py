# This file was auto-generated by Fern from our API Definition.

import typing

from .dtmf_action_params import DtmfActionParams
from .end_conversation_action_params import EndConversationActionParams
from .transfer_call_action_params import TransferCallActionParams

CreateActionRequest = typing.Union[TransferCallActionParams, EndConversationActionParams, DtmfActionParams]
