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

    def echo(self, msg: str) -> str:
        if not isinstance(msg, str):
            raise RuntimeError('the type of msg should be str')
        echo = self.__abi_info.get_function('echo')
        echo.set_params_value((msg,))
        response = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0, 0, echo, True)
        response = binascii.a2b_hex(response)
        return response.decode('ascii')

    def notify_args(self, bool_args: bool, int_args: int, list_args: list, str_args: str, bytes_address_args: bytes,
                    acct: Account, payer_acct: Account, gas_limit: int, gas_price: int) -> str:
        notify_args = self.__abi_info.get_function('notify_args')
        notify_args.set_params_value((bool_args, int_args, list_args, str_args, bytes_address_args))
        tx_hash = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, acct, payer_acct, gas_limit,
                                                       gas_price, notify_args, False)
        return tx_hash

    def query_notify_args_event(self, tx_hash: str):
        event = self.__sdk.rpc.get_smart_contract_event_by_tx_hash(tx_hash)
        event = event.get('Notify', list())
        if len(event) == 0:
            return event
        event = event[0]
        event = event.get('States', list())
        if len(event) == 0:
            return event
        event[0] = binascii.a2b_hex(event[0]).decode('ascii')
        event[1] = bool(event[1])
        event[2] = int(''.join(reversed([event[2][i:i + 2] for i in range(0, len(event[2]), 2)])), 16)
        event[3] = list(map(lambda e: int(''.join(reversed([e[i:i + 2] for i in range(0, len(e), 2)])), 16), event[3]))
        event[4] = binascii.a2b_hex(event[4]).decode('ascii')
        event[5] = Address(binascii.a2b_hex(event[5])).b58encode()
        return event

    def put_dict(self, dict_args: dict, acct: Account, payer_acct: Account, gas_limit: int, gas_price: int):
        put_dict = self.__abi_info.get_function('put_dict')
        put_dict.set_params_value((dict_args,))
        tx_hash = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, acct, payer_acct, gas_limit,
                                                       gas_price, put_dict, False)
        return tx_hash

    def get_dict(self):
        get_dict = self.__abi_info.get_function('get_dict')
        response = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0, 0, get_dict,
                                                        True)
        return response

    def put_dict_value(self, dict_value_args, acct: Account, payer_acct: Account, gas_limit: int,
                       gas_price: int) -> str:
        put_dict_value = self.__abi_info.get_function('put_dict_value')
        put_dict_value.set_params_value((dict_value_args,))
        tx_hash = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, acct, payer_acct, gas_limit,
                                                       gas_price, put_dict_value, False)
        return tx_hash

    def query_put_dict_value_event(self, tx_hash):
        event = self.__sdk.rpc.get_smart_contract_event_by_tx_hash(tx_hash)
        event = event.get('Notify', list())
        if len(event) == 0:
            return event
        event = event[0]
        event = event.get('States', list())
        if len(event) == 0:
            return event
        event[0] = binascii.a2b_hex(event[0]).decode('ascii')
        return event

    def get_dict_value(self):
        get_dict_value = self.__abi_info.get_function('get_dict_value')
        response = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0, 0,
                                                        get_dict_value, True)
        return response

    def put_list(self, list_args: list, acct: Account, payer_acct: Account, gas_limit: int, gas_price: int):
        put_list = self.__abi_info.get_function('put_list')
        put_list.set_params_value((list_args,))
        tx_hash = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, acct, payer_acct, gas_limit,
                                                       gas_price, put_list, False)
        return tx_hash

    def query_put_list_event(self, tx_hash):
        event = self.__sdk.rpc.get_smart_contract_event_by_tx_hash(tx_hash)
        event = event.get('Notify', list())
        if len(event) == 0:
            return event
        event = event[0]
        event = event.get('States', list())
        if len(event) == 0:
            return event
        event[0] = binascii.a2b_hex(event[0]).decode('ascii')
        event[1] = list(map(lambda e: int(''.join(reversed([e[i:i + 2] for i in range(0, len(e), 2)])), 16), event[1]))
        return event

    def get_list(self):
        get_list = self.__abi_info.get_function('get_list')
        response = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0, 0, get_list,
                                                        True)
        return response

    def add_key_value_in_dict(self, key, value, acct: Account, payer_acct: Account, gas_limit: int, gas_price: int):
        add_key_value_in_dict = self.__abi_info.get_function('add_key_value_in_dict')
        add_key_value_in_dict.set_params_value((key, value))
        tx_hash = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, acct, payer_acct, gas_limit,
                                                       gas_price, add_key_value_in_dict, False)
        return tx_hash

    def query_add_key_value_in_dict_event(self, tx_hash):
        event = self.__sdk.rpc.get_smart_contract_event_by_tx_hash(tx_hash)
        event = event.get('Notify', list())
        if len(event) == 0:
            return event
        event = event[0]
        event = event.get('States', list())
        if len(event) == 0:
            return event
        event[:3] = list(map(lambda e: binascii.a2b_hex(e).decode('ascii'), event[:3]))
        event[3] = {k.decode('ascii'): v.decode('ascii') for k, v in deserialize_hex(event[3]).items()}
        return event

    def get_value_by_key(self, key, acct: Account, payer_acct: Account, gas_limit: int, gas_price: int):
        get_value_by_key = self.__abi_info.get_function('get_value_by_key')
        get_value_by_key.set_params_value((key,))
        response = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, acct, payer_acct, gas_limit,
                                                        gas_price)
        return response
