# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.buy_phone_number_request import BuyPhoneNumberRequest
from ...types.http_validation_error import HttpValidationError
from ...types.phone_number import PhoneNumber
from ...types.phone_number_page import PhoneNumberPage
from .types.update_number_request_example_context import UpdateNumberRequestExampleContext
from .types.update_number_request_inbound_agent import UpdateNumberRequestInboundAgent
from .types.update_number_request_label import UpdateNumberRequestLabel
from .types.update_number_request_outbound_only import UpdateNumberRequestOutboundOnly

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class NumbersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_numbers(self, *, page: typing.Optional[int] = None, size: typing.Optional[int] = None) -> PhoneNumberPage:
        """
        Parameters:
            - page: typing.Optional[int].

            - size: typing.Optional[int].
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/numbers/list"),
            params=remove_none_from_dict({"page": page, "size": size}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PhoneNumberPage, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_number(self, *, phone_number: str) -> PhoneNumber:
        """
        Parameters:
            - phone_number: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/numbers"),
            params=remove_none_from_dict({"phone_number": phone_number}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PhoneNumber, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def buy_number(self, *, request: BuyPhoneNumberRequest) -> PhoneNumber:
        """
        Parameters:
            - request: BuyPhoneNumberRequest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/numbers/buy"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PhoneNumber, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_number(
        self,
        *,
        phone_number: str,
        outbound_only: typing.Optional[UpdateNumberRequestOutboundOnly] = OMIT,
        example_context: typing.Optional[UpdateNumberRequestExampleContext] = OMIT,
        label: typing.Optional[UpdateNumberRequestLabel] = OMIT,
        inbound_agent: typing.Optional[UpdateNumberRequestInboundAgent] = OMIT,
    ) -> PhoneNumber:
        """
        Parameters:
            - phone_number: str.

            - outbound_only: typing.Optional[UpdateNumberRequestOutboundOnly].

            - example_context: typing.Optional[UpdateNumberRequestExampleContext].

            - label: typing.Optional[UpdateNumberRequestLabel].

            - inbound_agent: typing.Optional[UpdateNumberRequestInboundAgent].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if outbound_only is not OMIT:
            _request["outbound_only"] = outbound_only
        if example_context is not OMIT:
            _request["example_context"] = example_context
        if label is not OMIT:
            _request["label"] = label
        if inbound_agent is not OMIT:
            _request["inbound_agent"] = inbound_agent
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/numbers/update"),
            params=remove_none_from_dict({"phone_number": phone_number}),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PhoneNumber, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def cancel_number(self, *, phone_number: str) -> PhoneNumber:
        """
        Parameters:
            - phone_number: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/numbers/cancel"),
            params=remove_none_from_dict({"phone_number": phone_number}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PhoneNumber, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def link_number(
        self, *, phone_number: str, telephony_account_connection: str, outbound_only: typing.Optional[bool] = OMIT
    ) -> PhoneNumber:
        """
        Parameters:
            - phone_number: str.

            - telephony_account_connection: str.

            - outbound_only: typing.Optional[bool].
        """
        _request: typing.Dict[str, typing.Any] = {
            "phone_number": phone_number,
            "telephony_account_connection": telephony_account_connection,
        }
        if outbound_only is not OMIT:
            _request["outbound_only"] = outbound_only
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/numbers/link"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PhoneNumber, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncNumbersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_numbers(
        self, *, page: typing.Optional[int] = None, size: typing.Optional[int] = None
    ) -> PhoneNumberPage:
        """
        Parameters:
            - page: typing.Optional[int].

            - size: typing.Optional[int].
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/numbers/list"),
            params=remove_none_from_dict({"page": page, "size": size}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PhoneNumberPage, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_number(self, *, phone_number: str) -> PhoneNumber:
        """
        Parameters:
            - phone_number: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/numbers"),
            params=remove_none_from_dict({"phone_number": phone_number}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PhoneNumber, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def buy_number(self, *, request: BuyPhoneNumberRequest) -> PhoneNumber:
        """
        Parameters:
            - request: BuyPhoneNumberRequest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/numbers/buy"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PhoneNumber, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_number(
        self,
        *,
        phone_number: str,
        outbound_only: typing.Optional[UpdateNumberRequestOutboundOnly] = OMIT,
        example_context: typing.Optional[UpdateNumberRequestExampleContext] = OMIT,
        label: typing.Optional[UpdateNumberRequestLabel] = OMIT,
        inbound_agent: typing.Optional[UpdateNumberRequestInboundAgent] = OMIT,
    ) -> PhoneNumber:
        """
        Parameters:
            - phone_number: str.

            - outbound_only: typing.Optional[UpdateNumberRequestOutboundOnly].

            - example_context: typing.Optional[UpdateNumberRequestExampleContext].

            - label: typing.Optional[UpdateNumberRequestLabel].

            - inbound_agent: typing.Optional[UpdateNumberRequestInboundAgent].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if outbound_only is not OMIT:
            _request["outbound_only"] = outbound_only
        if example_context is not OMIT:
            _request["example_context"] = example_context
        if label is not OMIT:
            _request["label"] = label
        if inbound_agent is not OMIT:
            _request["inbound_agent"] = inbound_agent
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/numbers/update"),
            params=remove_none_from_dict({"phone_number": phone_number}),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PhoneNumber, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def cancel_number(self, *, phone_number: str) -> PhoneNumber:
        """
        Parameters:
            - phone_number: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/numbers/cancel"),
            params=remove_none_from_dict({"phone_number": phone_number}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PhoneNumber, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def link_number(
        self, *, phone_number: str, telephony_account_connection: str, outbound_only: typing.Optional[bool] = OMIT
    ) -> PhoneNumber:
        """
        Parameters:
            - phone_number: str.

            - telephony_account_connection: str.

            - outbound_only: typing.Optional[bool].
        """
        _request: typing.Dict[str, typing.Any] = {
            "phone_number": phone_number,
            "telephony_account_connection": telephony_account_connection,
        }
        if outbound_only is not OMIT:
            _request["outbound_only"] = outbound_only
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/numbers/link"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PhoneNumber, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
