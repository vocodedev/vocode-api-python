# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.pinecone_vector_database import PineconeVectorDatabase
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.vector_database_page import VectorDatabasePage
from ..types.pinecone_vector_database_update_params_index import PineconeVectorDatabaseUpdateParamsIndex
from ..types.pinecone_vector_database_update_params_api_key import PineconeVectorDatabaseUpdateParamsApiKey
from ..types.pinecone_vector_database_update_params_api_environment import (
    PineconeVectorDatabaseUpdateParamsApiEnvironment,
)
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class VectorDatabasesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_vector_database(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PineconeVectorDatabase:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PineconeVectorDatabase
            Successful Response

        Examples
        --------
        from vocode import Vocode

        client = Vocode(
            token="YOUR_TOKEN",
        )
        client.vector_databases.get_vector_database(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/vector_databases",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PineconeVectorDatabase,
                    parse_obj_as(
                        type_=PineconeVectorDatabase,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_vector_databases(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VectorDatabasePage:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VectorDatabasePage
            Successful Response

        Examples
        --------
        from vocode import Vocode

        client = Vocode(
            token="YOUR_TOKEN",
        )
        client.vector_databases.list_vector_databases()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/vector_databases/list",
            method="GET",
            params={
                "page": page,
                "size": size,
                "sort_column": sort_column,
                "sort_desc": sort_desc,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    VectorDatabasePage,
                    parse_obj_as(
                        type_=VectorDatabasePage,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_vector_database(
        self, *, index: str, api_key: str, api_environment: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PineconeVectorDatabase:
        """
        Parameters
        ----------
        index : str

        api_key : str

        api_environment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PineconeVectorDatabase
            Successful Response

        Examples
        --------
        from vocode import Vocode

        client = Vocode(
            token="YOUR_TOKEN",
        )
        client.vector_databases.create_vector_database(
            index="index",
            api_key="api_key",
            api_environment="api_environment",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/vector_databases/create",
            method="POST",
            json={
                "index": index,
                "api_key": api_key,
                "api_environment": api_environment,
                "type": "vector_database_pinecone",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PineconeVectorDatabase,
                    parse_obj_as(
                        type_=PineconeVectorDatabase,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_vector_database(
        self,
        *,
        id: str,
        index: typing.Optional[PineconeVectorDatabaseUpdateParamsIndex] = OMIT,
        api_key: typing.Optional[PineconeVectorDatabaseUpdateParamsApiKey] = OMIT,
        api_environment: typing.Optional[PineconeVectorDatabaseUpdateParamsApiEnvironment] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PineconeVectorDatabase:
        """
        Parameters
        ----------
        id : str

        index : typing.Optional[PineconeVectorDatabaseUpdateParamsIndex]

        api_key : typing.Optional[PineconeVectorDatabaseUpdateParamsApiKey]

        api_environment : typing.Optional[PineconeVectorDatabaseUpdateParamsApiEnvironment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PineconeVectorDatabase
            Successful Response

        Examples
        --------
        from vocode import Vocode

        client = Vocode(
            token="YOUR_TOKEN",
        )
        client.vector_databases.update_vector_database(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/vector_databases/update",
            method="POST",
            params={
                "id": id,
            },
            json={
                "index": index,
                "api_key": api_key,
                "api_environment": api_environment,
                "type": "vector_database_pinecone",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PineconeVectorDatabase,
                    parse_obj_as(
                        type_=PineconeVectorDatabase,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncVectorDatabasesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_vector_database(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PineconeVectorDatabase:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PineconeVectorDatabase
            Successful Response

        Examples
        --------
        import asyncio

        from vocode import AsyncVocode

        client = AsyncVocode(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vector_databases.get_vector_database(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/vector_databases",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PineconeVectorDatabase,
                    parse_obj_as(
                        type_=PineconeVectorDatabase,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_vector_databases(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VectorDatabasePage:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VectorDatabasePage
            Successful Response

        Examples
        --------
        import asyncio

        from vocode import AsyncVocode

        client = AsyncVocode(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vector_databases.list_vector_databases()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/vector_databases/list",
            method="GET",
            params={
                "page": page,
                "size": size,
                "sort_column": sort_column,
                "sort_desc": sort_desc,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    VectorDatabasePage,
                    parse_obj_as(
                        type_=VectorDatabasePage,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_vector_database(
        self, *, index: str, api_key: str, api_environment: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PineconeVectorDatabase:
        """
        Parameters
        ----------
        index : str

        api_key : str

        api_environment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PineconeVectorDatabase
            Successful Response

        Examples
        --------
        import asyncio

        from vocode import AsyncVocode

        client = AsyncVocode(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vector_databases.create_vector_database(
                index="index",
                api_key="api_key",
                api_environment="api_environment",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/vector_databases/create",
            method="POST",
            json={
                "index": index,
                "api_key": api_key,
                "api_environment": api_environment,
                "type": "vector_database_pinecone",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PineconeVectorDatabase,
                    parse_obj_as(
                        type_=PineconeVectorDatabase,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_vector_database(
        self,
        *,
        id: str,
        index: typing.Optional[PineconeVectorDatabaseUpdateParamsIndex] = OMIT,
        api_key: typing.Optional[PineconeVectorDatabaseUpdateParamsApiKey] = OMIT,
        api_environment: typing.Optional[PineconeVectorDatabaseUpdateParamsApiEnvironment] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PineconeVectorDatabase:
        """
        Parameters
        ----------
        id : str

        index : typing.Optional[PineconeVectorDatabaseUpdateParamsIndex]

        api_key : typing.Optional[PineconeVectorDatabaseUpdateParamsApiKey]

        api_environment : typing.Optional[PineconeVectorDatabaseUpdateParamsApiEnvironment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PineconeVectorDatabase
            Successful Response

        Examples
        --------
        import asyncio

        from vocode import AsyncVocode

        client = AsyncVocode(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vector_databases.update_vector_database(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/vector_databases/update",
            method="POST",
            params={
                "id": id,
            },
            json={
                "index": index,
                "api_key": api_key,
                "api_environment": api_environment,
                "type": "vector_database_pinecone",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PineconeVectorDatabase,
                    parse_obj_as(
                        type_=PineconeVectorDatabase,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
