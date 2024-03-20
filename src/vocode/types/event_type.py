# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EventType(str, enum.Enum):
    """
    An enumeration.
    """

    EVENT_MESSAGE = "event_message"
    EVENT_ACTION = "event_action"
    EVENT_PHONE_CALL_CONNECTED = "event_phone_call_connected"
    EVENT_PHONE_CALL_ENDED = "event_phone_call_ended"
    EVENT_PHONE_CALL_DID_NOT_CONNECT = "event_phone_call_did_not_connect"
    EVENT_TRANSCRIPT = "event_transcript"
    EVENT_RECORDING = "event_recording"
    EVENT_HUMAN_DETECTION = "event_human_detection"

    def visit(
        self,
        event_message: typing.Callable[[], T_Result],
        event_action: typing.Callable[[], T_Result],
        event_phone_call_connected: typing.Callable[[], T_Result],
        event_phone_call_ended: typing.Callable[[], T_Result],
        event_phone_call_did_not_connect: typing.Callable[[], T_Result],
        event_transcript: typing.Callable[[], T_Result],
        event_recording: typing.Callable[[], T_Result],
        event_human_detection: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EventType.EVENT_MESSAGE:
            return event_message()
        if self is EventType.EVENT_ACTION:
            return event_action()
        if self is EventType.EVENT_PHONE_CALL_CONNECTED:
            return event_phone_call_connected()
        if self is EventType.EVENT_PHONE_CALL_ENDED:
            return event_phone_call_ended()
        if self is EventType.EVENT_PHONE_CALL_DID_NOT_CONNECT:
            return event_phone_call_did_not_connect()
        if self is EventType.EVENT_TRANSCRIPT:
            return event_transcript()
        if self is EventType.EVENT_RECORDING:
            return event_recording()
        if self is EventType.EVENT_HUMAN_DETECTION:
            return event_human_detection()
