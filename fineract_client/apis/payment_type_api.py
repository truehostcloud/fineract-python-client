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


class PaymentTypeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_payment_type(self, body, **kwargs):  # noqa: E501
        """Create a Payment Type  # noqa: E501

        Creates a new Payment type  Mandatory Fields: name  Optional Fields: Description, isCashPayment,Position  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_payment_type(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostPaymentTypesRequest body: (required)
        :return: PostPaymentTypesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_payment_type_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_payment_type_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_payment_type_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a Payment Type  # noqa: E501

        Creates a new Payment type  Mandatory Fields: name  Optional Fields: Description, isCashPayment,Position  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_payment_type_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostPaymentTypesRequest body: (required)
        :return: PostPaymentTypesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_payment_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_payment_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/v1/paymenttypes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostPaymentTypesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_code1(self, payment_type_id, **kwargs):  # noqa: E501
        """Delete a Payment Type  # noqa: E501

        Deletes payment type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_code1(payment_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int payment_type_id: paymentTypeId (required)
        :return: DeletePaymentTypesPaymentTypeIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_code1_with_http_info(payment_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_code1_with_http_info(payment_type_id, **kwargs)  # noqa: E501
            return data

    def delete_code1_with_http_info(self, payment_type_id, **kwargs):  # noqa: E501
        """Delete a Payment Type  # noqa: E501

        Deletes payment type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_code1_with_http_info(payment_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int payment_type_id: paymentTypeId (required)
        :return: DeletePaymentTypesPaymentTypeIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_type_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_code1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_type_id' is set
        if ('payment_type_id' not in params or
                params['payment_type_id'] is None):
            raise ValueError("Missing the required parameter `payment_type_id` when calling `delete_code1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payment_type_id' in params:
            path_params['paymentTypeId'] = params['payment_type_id']  # noqa: E501

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
            '/v1/paymenttypes/{paymentTypeId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeletePaymentTypesPaymentTypeIdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_payment_types(self, **kwargs):  # noqa: E501
        """Retrieve all Payment Types  # noqa: E501

        Retrieve list of payment types  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_payment_types(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool only_with_code: onlyWithCode
        :return: list[GetPaymentTypesResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_payment_types_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_payment_types_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_payment_types_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve all Payment Types  # noqa: E501

        Retrieve list of payment types  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_payment_types_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool only_with_code: onlyWithCode
        :return: list[GetPaymentTypesResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['only_with_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_payment_types" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'only_with_code' in params:
            query_params.append(('onlyWithCode', params['only_with_code']))  # noqa: E501

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
            '/v1/paymenttypes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetPaymentTypesResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_one_payment_type(self, payment_type_id, **kwargs):  # noqa: E501
        """Retrieve a Payment Type  # noqa: E501

        Retrieves a payment type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_one_payment_type(payment_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int payment_type_id: paymentTypeId (required)
        :return: GetPaymentTypesPaymentTypeIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_one_payment_type_with_http_info(payment_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_one_payment_type_with_http_info(payment_type_id, **kwargs)  # noqa: E501
            return data

    def retrieve_one_payment_type_with_http_info(self, payment_type_id, **kwargs):  # noqa: E501
        """Retrieve a Payment Type  # noqa: E501

        Retrieves a payment type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_one_payment_type_with_http_info(payment_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int payment_type_id: paymentTypeId (required)
        :return: GetPaymentTypesPaymentTypeIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_type_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_one_payment_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_type_id' is set
        if ('payment_type_id' not in params or
                params['payment_type_id'] is None):
            raise ValueError("Missing the required parameter `payment_type_id` when calling `retrieve_one_payment_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payment_type_id' in params:
            path_params['paymentTypeId'] = params['payment_type_id']  # noqa: E501

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
            '/v1/paymenttypes/{paymentTypeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetPaymentTypesPaymentTypeIdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_payment_type(self, body, payment_type_id, **kwargs):  # noqa: E501
        """Update a Payment Type  # noqa: E501

        Updates a Payment Type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_payment_type(body, payment_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PutPaymentTypesPaymentTypeIdRequest body: (required)
        :param int payment_type_id: paymentTypeId (required)
        :return: PutPaymentTypesPaymentTypeIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_payment_type_with_http_info(body, payment_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_payment_type_with_http_info(body, payment_type_id, **kwargs)  # noqa: E501
            return data

    def update_payment_type_with_http_info(self, body, payment_type_id, **kwargs):  # noqa: E501
        """Update a Payment Type  # noqa: E501

        Updates a Payment Type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_payment_type_with_http_info(body, payment_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PutPaymentTypesPaymentTypeIdRequest body: (required)
        :param int payment_type_id: paymentTypeId (required)
        :return: PutPaymentTypesPaymentTypeIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'payment_type_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_payment_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_payment_type`")  # noqa: E501
        # verify the required parameter 'payment_type_id' is set
        if ('payment_type_id' not in params or
                params['payment_type_id'] is None):
            raise ValueError("Missing the required parameter `payment_type_id` when calling `update_payment_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payment_type_id' in params:
            path_params['paymentTypeId'] = params['payment_type_id']  # noqa: E501

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
            '/v1/paymenttypes/{paymentTypeId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PutPaymentTypesPaymentTypeIdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
