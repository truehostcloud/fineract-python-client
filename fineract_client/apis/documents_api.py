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


class DocumentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_document(self, entity_type, entity_id, **kwargs):  # noqa: E501
        """Create a Document  # noqa: E501

        Note: A document is created using a Multi-part form upload   Body Parts  name :  Name or summary of the document  description :  Description of the document  file :  The file to be uploaded  Mandatory Fields :  file and description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_document(entity_type, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: entityType (required)
        :param int entity_id: entityId (required)
        :param str date_format:
        :param str description:
        :param str locale:
        :param str name:
        :param str uploaded_input_stream:
        :param int content_length: Content-Length
        :return: PostEntityTypeEntityIdDocumentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_document_with_http_info(entity_type, entity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_document_with_http_info(entity_type, entity_id, **kwargs)  # noqa: E501
            return data

    def create_document_with_http_info(self, entity_type, entity_id, **kwargs):  # noqa: E501
        """Create a Document  # noqa: E501

        Note: A document is created using a Multi-part form upload   Body Parts  name :  Name or summary of the document  description :  Description of the document  file :  The file to be uploaded  Mandatory Fields :  file and description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_document_with_http_info(entity_type, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: entityType (required)
        :param int entity_id: entityId (required)
        :param str date_format:
        :param str description:
        :param str locale:
        :param str name:
        :param str uploaded_input_stream:
        :param int content_length: Content-Length
        :return: PostEntityTypeEntityIdDocumentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id', 'date_format', 'description', 'locale', 'name', 'uploaded_input_stream', 'content_length']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `create_document`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `create_document`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'content_length' in params:
            header_params['Content-Length'] = params['content_length']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'date_format' in params:
            form_params.append(('dateFormat', params['date_format']))  # noqa: E501
        if 'description' in params:
            form_params.append(('description', params['description']))  # noqa: E501
        if 'locale' in params:
            form_params.append(('locale', params['locale']))  # noqa: E501
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'uploaded_input_stream' in params:
            local_var_files['uploadedInputStream'] = params['uploaded_input_stream']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tenantid']  # noqa: E501

        return self.api_client.call_api(
            '/v1/{entityType}/{entityId}/documents', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostEntityTypeEntityIdDocumentsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_document(self, entity_type, entity_id, document_id, **kwargs):  # noqa: E501
        """Remove a Document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_document(entity_type, entity_id, document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: entityType (required)
        :param int entity_id: entityId (required)
        :param int document_id: documentId (required)
        :return: DeleteEntityTypeEntityIdDocumentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_document_with_http_info(entity_type, entity_id, document_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_document_with_http_info(entity_type, entity_id, document_id, **kwargs)  # noqa: E501
            return data

    def delete_document_with_http_info(self, entity_type, entity_id, document_id, **kwargs):  # noqa: E501
        """Remove a Document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_document_with_http_info(entity_type, entity_id, document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: entityType (required)
        :param int entity_id: entityId (required)
        :param int document_id: documentId (required)
        :return: DeleteEntityTypeEntityIdDocumentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id', 'document_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `delete_document`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `delete_document`")  # noqa: E501
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params or
                params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `delete_document`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']  # noqa: E501

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
            '/v1/{entityType}/{entityId}/documents/{documentId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteEntityTypeEntityIdDocumentsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def download_file(self, entity_type, entity_id, document_id, **kwargs):  # noqa: E501
        """Retrieve Binary File associated with Document  # noqa: E501

        Request used to download the file associated with the document  Example Requests:  clients/1/documents/1/attachment   loans/1/documents/1/attachment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_file(entity_type, entity_id, document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: entityType (required)
        :param int entity_id: entityId (required)
        :param int document_id: documentId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_file_with_http_info(entity_type, entity_id, document_id, **kwargs)  # noqa: E501
        else:
            (data) = self.download_file_with_http_info(entity_type, entity_id, document_id, **kwargs)  # noqa: E501
            return data

    def download_file_with_http_info(self, entity_type, entity_id, document_id, **kwargs):  # noqa: E501
        """Retrieve Binary File associated with Document  # noqa: E501

        Request used to download the file associated with the document  Example Requests:  clients/1/documents/1/attachment   loans/1/documents/1/attachment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_file_with_http_info(entity_type, entity_id, document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: entityType (required)
        :param int entity_id: entityId (required)
        :param int document_id: documentId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id', 'document_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `download_file`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `download_file`")  # noqa: E501
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params or
                params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `download_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth', 'tenantid']  # noqa: E501

        return self.api_client.call_api(
            '/v1/{entityType}/{entityId}/documents/{documentId}/attachment', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document(self, entity_type, entity_id, document_id, **kwargs):  # noqa: E501
        """Retrieve a Document  # noqa: E501

        Example Requests:  clients/1/documents/1   loans/1/documents/1   client_identifiers/1/documents/1?fields=name,description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document(entity_type, entity_id, document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: entityType (required)
        :param int entity_id: entityId (required)
        :param int document_id: documentId (required)
        :return: GetEntityTypeEntityIdDocumentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_document_with_http_info(entity_type, entity_id, document_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_document_with_http_info(entity_type, entity_id, document_id, **kwargs)  # noqa: E501
            return data

    def get_document_with_http_info(self, entity_type, entity_id, document_id, **kwargs):  # noqa: E501
        """Retrieve a Document  # noqa: E501

        Example Requests:  clients/1/documents/1   loans/1/documents/1   client_identifiers/1/documents/1?fields=name,description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document_with_http_info(entity_type, entity_id, document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: entityType (required)
        :param int entity_id: entityId (required)
        :param int document_id: documentId (required)
        :return: GetEntityTypeEntityIdDocumentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id', 'document_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `get_document`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `get_document`")  # noqa: E501
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params or
                params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `get_document`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']  # noqa: E501

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
            '/v1/{entityType}/{entityId}/documents/{documentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetEntityTypeEntityIdDocumentsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_all_documents(self, entity_type, entity_id, **kwargs):  # noqa: E501
        """List documents  # noqa: E501

        Example Requests:  clients/1/documents  client_identifiers/1/documents  loans/1/documents?fields=name,description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_all_documents(entity_type, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: entityType (required)
        :param int entity_id: entityId (required)
        :return: list[GetEntityTypeEntityIdDocumentsResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_all_documents_with_http_info(entity_type, entity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_all_documents_with_http_info(entity_type, entity_id, **kwargs)  # noqa: E501
            return data

    def retrieve_all_documents_with_http_info(self, entity_type, entity_id, **kwargs):  # noqa: E501
        """List documents  # noqa: E501

        Example Requests:  clients/1/documents  client_identifiers/1/documents  loans/1/documents?fields=name,description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_all_documents_with_http_info(entity_type, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: entityType (required)
        :param int entity_id: entityId (required)
        :return: list[GetEntityTypeEntityIdDocumentsResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_all_documents" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `retrieve_all_documents`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `retrieve_all_documents`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501

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
            '/v1/{entityType}/{entityId}/documents', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetEntityTypeEntityIdDocumentsResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_document(self, entity_type, entity_id, document_id, **kwargs):  # noqa: E501
        """Update a Document  # noqa: E501

        Note: A document is updated using a Multi-part form upload  Body Parts name Name or summary of the document description Description of the document file The file to be uploaded  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_document(entity_type, entity_id, document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: entityType (required)
        :param int entity_id: entityId (required)
        :param int document_id: documentId (required)
        :param str date_format:
        :param str description:
        :param str locale:
        :param str name:
        :param str uploaded_input_stream:
        :param int content_length: Content-Length
        :return: PutEntityTypeEntityIdDocumentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_document_with_http_info(entity_type, entity_id, document_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_document_with_http_info(entity_type, entity_id, document_id, **kwargs)  # noqa: E501
            return data

    def update_document_with_http_info(self, entity_type, entity_id, document_id, **kwargs):  # noqa: E501
        """Update a Document  # noqa: E501

        Note: A document is updated using a Multi-part form upload  Body Parts name Name or summary of the document description Description of the document file The file to be uploaded  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_document_with_http_info(entity_type, entity_id, document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: entityType (required)
        :param int entity_id: entityId (required)
        :param int document_id: documentId (required)
        :param str date_format:
        :param str description:
        :param str locale:
        :param str name:
        :param str uploaded_input_stream:
        :param int content_length: Content-Length
        :return: PutEntityTypeEntityIdDocumentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id', 'document_id', 'date_format', 'description', 'locale', 'name', 'uploaded_input_stream', 'content_length']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `update_document`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `update_document`")  # noqa: E501
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params or
                params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `update_document`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'content_length' in params:
            header_params['Content-Length'] = params['content_length']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'date_format' in params:
            form_params.append(('dateFormat', params['date_format']))  # noqa: E501
        if 'description' in params:
            form_params.append(('description', params['description']))  # noqa: E501
        if 'locale' in params:
            form_params.append(('locale', params['locale']))  # noqa: E501
        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'uploaded_input_stream' in params:
            local_var_files['uploadedInputStream'] = params['uploaded_input_stream']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tenantid']  # noqa: E501

        return self.api_client.call_api(
            '/v1/{entityType}/{entityId}/documents/{documentId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PutEntityTypeEntityIdDocumentsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
