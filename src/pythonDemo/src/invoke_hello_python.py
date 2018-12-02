#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import binascii

from ontology.ont_sdk import OntologySdk
from ontology.common.address import Address
from ontology.account.account import Account
from ontology.utils.util import deserialize_hex
from ontology.smart_contract.neo_contract.abi.abi_info import AbiInfo


class InvokeHelloPython(object):
    def __init__(self, sdk: OntologySdk, abi: dict, hex_contract_address: str):
        if not isinstance(sdk, OntologySdk):
            raise RuntimeError('the type of sdk is error')
        if not isinstance(abi, dict):
            raise RuntimeError('the type of abi should be dict')
        if not isinstance(hex_contract_address, str):
            raise RuntimeError('the type of contract address should be str')
        if len(hex_contract_address) != 40:
            raise RuntimeError()
        self.__sdk = sdk
        self.__contract_address_hex = hex_contract_address
        self.__contract_address_bytearray = bytearray(binascii.a2b_hex(hex_contract_address))
        self.__contract_address_bytearray.reverse()
        self.__abi = abi
        entry_point = self.__abi.get('entrypoint', '')
        functions = self.__abi['abi']['functions']
        events = self.__abi.get('events', list())
        self.__abi_info = AbiInfo(hex_contract_address, entry_point, functions, events)

    def name(self):
        name_func = self.__abi_info.get_function('name')
        response = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0, 0, name_func,
                                                        True)
        response = binascii.a2b_hex(response)
        return response.decode('ascii')

    def hello(self, msg: str) -> str:
        if not isinstance(msg, str):
            raise RuntimeError('the type of msg should be str')
        echo = self.__abi_info.get_function('hello')
        echo.set_params_value((msg,))
        response = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0, 0, echo, True)
        response = binascii.a2b_hex(response)
        return response.decode('ascii')

    def test_hello(self, bool_msg, int_msg, bytes_msg, str_msg, bytes_address_msg: bytes, acct: Account,
                   payer_acct: Account, gas_limit: int, gas_price: int) -> str:
        notify_args = self.__abi_info.get_function('testHello')
        notify_args.set_params_value((bool_msg, int_msg, bytes_msg, str_msg, bytes_address_msg))
        tx_hash = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, acct, payer_acct, gas_limit,
                                                       gas_price, notify_args, False)
        return tx_hash

    def test_list_and_str(self, list_msg: list, acct, payer_acct, gas_limit, gas_price):
        func = self.__abi_info.get_function('testList')
        func.set_params_value((list_msg,))
        tx_hash = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, acct, payer_acct, gas_limit,
                                                       gas_price, func, False)
        return tx_hash

    def test_dict(self, dict_msg: dict):
        func = self.__abi_info.get_function('testMap')
        func.set_params_value((dict_msg,))
        value = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0,
                                                     0, func, True)
        value = binascii.a2b_hex(value)
        return value.decode('ascii')

    def test_get_dict(self, key):
        func = self.__abi_info.get_function('testGetMap')
        func.set_params_value((key,))
        value = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0, 0, func, True)
        value = binascii.a2b_hex(value)
        return value.decode('ascii')

    def test_dict_in_ctx(self, map_msg, acct, payer_acct, gas_limit, gas_price):
        func = self.__abi_info.get_function('testMapInMap')
        func.set_params_value((map_msg,))
        tx_hash = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, acct, payer_acct, gas_limit,
                                                       gas_price, func, False)
        return tx_hash

    def test_get_dict_in_ctx(self, key):
        func = self.__abi_info.get_function('testGetMapInMap')
        func.set_params_value((key,))
        value = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0, 0, func, True)
        value = binascii.a2b_hex(value)
        return value.decode('ascii')

    def test_transfer_multi(self, args, acct, payer_acct, gas_limit, gas_price):
        func = self.__abi_info.get_function('transferMulti')
        func.set_params_value((args,))
        tx_hash = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, acct, payer_acct, gas_limit,
                                                       gas_price, func, False)
        return tx_hash
