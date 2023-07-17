# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class VoiceType(str, enum.Enum):
    """
    An enumeration.
    """

    VOICE_BASE = "voice_base"
    VOICE_AZURE = "voice_azure"
    VOICE_RIME = "voice_rime"
    VOICE_ELEVEN_LABS = "voice_eleven_labs"

    def visit(
        self,
        voice_base: typing.Callable[[], T_Result],
        voice_azure: typing.Callable[[], T_Result],
        voice_rime: typing.Callable[[], T_Result],
        voice_eleven_labs: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VoiceType.VOICE_BASE:
            return voice_base()
        if self is VoiceType.VOICE_AZURE:
            return voice_azure()
        if self is VoiceType.VOICE_RIME:
            return voice_rime()
        if self is VoiceType.VOICE_ELEVEN_LABS:
            return voice_eleven_labs()
