# coding: utf-8

"""
    Apache Fineract REST API

    Apache Fineract is a secure, multi-tenanted microfinance platform. The goal of the Apache Fineract API is to empower developers to build apps on top of the Apache Fineract Platform. The https://cui.fineract.dev[reference app] (username: mifos, password: password) works on the same demo tenant as the interactive links in this documentation. Until we complete the new REST API documentation you still have the legacy documentation available https://fineract.apache.org/legacy-docs/apiLive.htm[here]. Please check https://fineract.apache.org/docs/current[the Fineract documentation] for more information.  # noqa: E501

    OpenAPI spec version: 1.11.0-SNAPSHOT
    Contact: dev@fineract.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from fineract_client.api_client import ApiClient


class ClientIdentifierApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_client_identifier(self, body, client_id, **kwargs):  # noqa: E501
        """Create an Identifier for a Client  # noqa: E501

        Mandatory Fields documentKey, documentTypeId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_client_identifier(body, client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostClientsClientIdIdentifiersRequest body: (required)
        :param int client_id: clientId (required)
        :return: PostClientsClientIdIdentifiersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_client_identifier_with_http_info(body, client_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_client_identifier_with_http_info(body, client_id, **kwargs)  # noqa: E501
            return data

    def create_client_identifier_with_http_info(self, body, client_id, **kwargs):  # noqa: E501
        """Create an Identifier for a Client  # noqa: E501

        Mandatory Fields documentKey, documentTypeId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_client_identifier_with_http_info(body, client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostClientsClientIdIdentifiersRequest body: (required)
        :param int client_id: clientId (required)
        :return: PostClientsClientIdIdentifiersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'client_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_client_identifier" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_client_identifier`")  # noqa: E501
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `create_client_identifier`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tenantid']  # noqa: E501

        return self.api_client.call_api(
            '/v1/clients/{clientId}/identifiers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostClientsClientIdIdentifiersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_client_identifier(self, client_id, identifier_id, **kwargs):  # noqa: E501
        """Delete a Client Identifier  # noqa: E501

        Deletes a Client Identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_client_identifier(client_id, identifier_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int client_id: clientId (required)
        :param int identifier_id: identifierId (required)
        :return: DeleteClientsClientIdIdentifiersIdentifierIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_client_identifier_with_http_info(client_id, identifier_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_client_identifier_with_http_info(client_id, identifier_id, **kwargs)  # noqa: E501
            return data

    def delete_client_identifier_with_http_info(self, client_id, identifier_id, **kwargs):  # noqa: E501
        """Delete a Client Identifier  # noqa: E501

        Deletes a Client Identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_client_identifier_with_http_info(client_id, identifier_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int client_id: clientId (required)
        :param int identifier_id: identifierId (required)
        :return: DeleteClientsClientIdIdentifiersIdentifierIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_id', 'identifier_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_client_identifier" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `delete_client_identifier`")  # noqa: E501
        # verify the required parameter 'identifier_id' is set
        if ('identifier_id' not in params or
                params['identifier_id'] is None):
            raise ValueError("Missing the required parameter `identifier_id` when calling `delete_client_identifier`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']  # noqa: E501
        if 'identifier_id' in params:
            path_params['identifierId'] = params['identifier_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tenantid']  # noqa: E501

        return self.api_client.call_api(
            '/v1/clients/{clientId}/identifiers/{identifierId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteClientsClientIdIdentifiersIdentifierIdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def new_client_identifier_details(self, client_id, **kwargs):  # noqa: E501
        """Retrieve Client Identifier Details Template  # noqa: E501

        This is a convenience resource useful for building maintenance user interface screens for client applications. The template data returned consists of any or all of:   Field Defaults  Allowed description Lists   Example Request: clients/1/identifiers/template  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.new_client_identifier_details(client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int client_id: clientId (required)
        :return: GetClientsClientIdIdentifiersTemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.new_client_identifier_details_with_http_info(client_id, **kwargs)  # noqa: E501
        else:
            (data) = self.new_client_identifier_details_with_http_info(client_id, **kwargs)  # noqa: E501
            return data

    def new_client_identifier_details_with_http_info(self, client_id, **kwargs):  # noqa: E501
        """Retrieve Client Identifier Details Template  # noqa: E501

        This is a convenience resource useful for building maintenance user interface screens for client applications. The template data returned consists of any or all of:   Field Defaults  Allowed description Lists   Example Request: clients/1/identifiers/template  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.new_client_identifier_details_with_http_info(client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int client_id: clientId (required)
        :return: GetClientsClientIdIdentifiersTemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method new_client_identifier_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `new_client_identifier_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tenantid']  # noqa: E501

        return self.api_client.call_api(
            '/v1/clients/{clientId}/identifiers/template', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetClientsClientIdIdentifiersTemplateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_all_client_identifiers(self, client_id, **kwargs):  # noqa: E501
        """List all Identifiers for a Client  # noqa: E501

        Example Requests: clients/1/identifiers   clients/1/identifiers?fields=documentKey,documentType,description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_all_client_identifiers(client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int client_id: clientId (required)
        :return: list[GetClientsClientIdIdentifiersResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_all_client_identifiers_with_http_info(client_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_all_client_identifiers_with_http_info(client_id, **kwargs)  # noqa: E501
            return data

    def retrieve_all_client_identifiers_with_http_info(self, client_id, **kwargs):  # noqa: E501
        """List all Identifiers for a Client  # noqa: E501

        Example Requests: clients/1/identifiers   clients/1/identifiers?fields=documentKey,documentType,description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_all_client_identifiers_with_http_info(client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int client_id: clientId (required)
        :return: list[GetClientsClientIdIdentifiersResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_all_client_identifiers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `retrieve_all_client_identifiers`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tenantid']  # noqa: E501

        return self.api_client.call_api(
            '/v1/clients/{clientId}/identifiers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetClientsClientIdIdentifiersResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_client_identifiers(self, client_id, identifier_id, **kwargs):  # noqa: E501
        """Retrieve a Client Identifier  # noqa: E501

        Example Requests: clients/1/identifier/2   clients/1/identifier/2?template=true  clients/1/identifiers/2?fields=documentKey,documentType,description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_client_identifiers(client_id, identifier_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int client_id: clientId (required)
        :param int identifier_id: identifierId (required)
        :return: GetClientsClientIdIdentifiersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_client_identifiers_with_http_info(client_id, identifier_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_client_identifiers_with_http_info(client_id, identifier_id, **kwargs)  # noqa: E501
            return data

    def retrieve_client_identifiers_with_http_info(self, client_id, identifier_id, **kwargs):  # noqa: E501
        """Retrieve a Client Identifier  # noqa: E501

        Example Requests: clients/1/identifier/2   clients/1/identifier/2?template=true  clients/1/identifiers/2?fields=documentKey,documentType,description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_client_identifiers_with_http_info(client_id, identifier_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int client_id: clientId (required)
        :param int identifier_id: identifierId (required)
        :return: GetClientsClientIdIdentifiersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_id', 'identifier_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_client_identifiers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `retrieve_client_identifiers`")  # noqa: E501
        # verify the required parameter 'identifier_id' is set
        if ('identifier_id' not in params or
                params['identifier_id'] is None):
            raise ValueError("Missing the required parameter `identifier_id` when calling `retrieve_client_identifiers`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']  # noqa: E501
        if 'identifier_id' in params:
            path_params['identifierId'] = params['identifier_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tenantid']  # noqa: E501

        return self.api_client.call_api(
            '/v1/clients/{clientId}/identifiers/{identifierId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetClientsClientIdIdentifiersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_client_identifer(self, body, client_id, identifier_id, **kwargs):  # noqa: E501
        """Update a Client Identifier  # noqa: E501

        Updates a Client Identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_client_identifer(body, client_id, identifier_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PutClientsClientIdIdentifiersIdentifierIdRequest body: (required)
        :param int client_id: clientId (required)
        :param int identifier_id: identifierId (required)
        :return: PutClientsClientIdIdentifiersIdentifierIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_client_identifer_with_http_info(body, client_id, identifier_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_client_identifer_with_http_info(body, client_id, identifier_id, **kwargs)  # noqa: E501
            return data

    def update_client_identifer_with_http_info(self, body, client_id, identifier_id, **kwargs):  # noqa: E501
        """Update a Client Identifier  # noqa: E501

        Updates a Client Identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_client_identifer_with_http_info(body, client_id, identifier_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PutClientsClientIdIdentifiersIdentifierIdRequest body: (required)
        :param int client_id: clientId (required)
        :param int identifier_id: identifierId (required)
        :return: PutClientsClientIdIdentifiersIdentifierIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'client_id', 'identifier_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_client_identifer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_client_identifer`")  # noqa: E501
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `update_client_identifer`")  # noqa: E501
        # verify the required parameter 'identifier_id' is set
        if ('identifier_id' not in params or
                params['identifier_id'] is None):
            raise ValueError("Missing the required parameter `identifier_id` when calling `update_client_identifer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']  # noqa: E501
        if 'identifier_id' in params:
            path_params['identifierId'] = params['identifier_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tenantid']  # noqa: E501

        return self.api_client.call_api(
            '/v1/clients/{clientId}/identifiers/{identifierId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PutClientsClientIdIdentifiersIdentifierIdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
