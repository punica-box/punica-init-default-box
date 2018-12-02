#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import binascii
import json

from ontology.ont_sdk import OntologySdk
from ontology.common.address import Address
from ontology.account.account import Account
from ontology.utils.util import deserialize_hex
from ontology.smart_contract.neo_contract.abi.abi_info import AbiInfo


class InvokeHelloOntology(object):
    def __init__(self, sdk: OntologySdk, hex_contract_address: str):
        if not isinstance(sdk, OntologySdk):
            raise RuntimeError('the type of sdk is error')
        if not isinstance(hex_contract_address, str):
            raise RuntimeError('the type of contract address should be str')
        if len(hex_contract_address) != 40:
            raise RuntimeError()
        self.__sdk = sdk
        self.__contract_address_hex = hex_contract_address
        self.__contract_address_bytearray = bytearray(binascii.a2b_hex(hex_contract_address))
        self.__contract_address_bytearray.reverse()
        str_abi = '{"CompilerVersion": "1.0.2", "hash": "16edbe366d1337eb510c2ff61099424c94aeef02", "entrypoint": "Main", "functions": [{"name": "name", "parameters": []}, {"name": "hello", "parameters": [{"name": "msg", "type": ""}]}, {"name": "testHello", "parameters": [{"name": "msgBool", "type": ""}, {"name": "msgInt", "type": ""}, {"name": "msgByteArray", "type": ""}, {"name": "msgStr", "type": ""}, {"name": "msgAddress", "type": ""}]}, {"name": "testList", "parameters": [{"name": "msgList", "type": ""}]}, {"name": "testListAndStr", "parameters": [{"name": "msgList", "type": ""}, {"name": "msgStr", "type": ""}]}, {"name": "testStructList", "parameters": [{"name": "structList", "type": ""}]}, {"name": "testStructListAndStr", "parameters": [{"name": "structList", "type": ""}, {"name": "msgStr", "type": ""}]}, {"name": "testMap", "parameters": [{"name": "msg", "type": ""}]}, {"name": "testGetMap", "parameters": [{"name": "key", "type": ""}]}, {"name": "testMapInMap", "parameters": [{"name": "msg", "type": ""}]}, {"name": "testGetMapInMap", "parameters": [{"name": "key", "type": ""}]}, {"name": "transferMulti", "parameters": [{"name": "args", "type": ""}]}]}'
        dict_abi = json.loads(str_abi)

        self.__abi_info = AbiInfo(self.__contract_address_hex, '',dict_abi['functions'])

    def name(self) -> str:
        name = self.__abi_info.get_function('name')
        name.set_params_value(())
        response = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0, 0, name, True)
        print("Name: ",response,binascii.a2b_hex(response).decode('ascii'))
        return response

    def test_Hello(self, bool_arg: bool, int_arg: int, bys_arg: bytes,str_args: str, bytes_address_arg: bytes) -> str:
        testHello = self.__abi_info.get_function('testHello')
        testHello.set_params_value((bool_arg, int_arg, bys_arg, str_args, bytes_address_arg,))
        response = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0,0, testHello, True)
        print("testHello: ",response)
        return response

    def test_List(self, list_arg: list) -> str:
        testList = self.__abi_info.get_function('testList')
        testList.set_params_value((list_arg,))
        response = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0,0, testList, True)
        print("testList: ",response)
        return response

    def test_List_And_Str(self, list_arg: list,str_args: str) -> str:
        testListAndStr = self.__abi_info.get_function('testListAndStr')
        testListAndStr.set_params_value((list_arg,str_args))
        response = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0,0, testListAndStr, True)
        print("testListAndStr: ",response)
        return response

    def test_Struct_List(self, list_arg: list) -> str:
        testStructList = self.__abi_info.get_function('testStructList')
        testStructList.set_params_value((list_arg,))
        response = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0,0, testStructList, True)
        print("testStructList: ",response)
        return response

    def test_Struct_List_And_Str(self, list_arg: list,str_args: str) -> str:
        testStructListAndStr = self.__abi_info.get_function('testStructListAndStr')
        testStructListAndStr.set_params_value((list_arg,str_args))
        response = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0,0, testStructListAndStr, True)
        print("testStructListAndStr: ",response)
        return response

    def test_Map(self, dict_args: dict,acct: Account) -> str:
        testMap = self.__abi_info.get_function('testMap')
        testMap.set_params_value((dict_args,))
        txhash = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, acct, acct, 30000, 500, testMap, False)
        print("txhash: ", txhash)
        response = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0,0, testMap, True)
        print("testMap: ",response)
        return response

    def test_Get_Map(self, str_arg: str) -> str:
        testGetMap = self.__abi_info.get_function('testGetMap')
        testGetMap.set_params_value((str_arg,))
        response = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0,0, testGetMap, True)
        print("testGetMap: ",response)
        return response

    def test_Map_In_Map(self, dict_args: dict,acct: Account) -> str:
        testMapInMap = self.__abi_info.get_function('testMapInMap')
        testMapInMap.set_params_value((dict_args,))
        txhash = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, acct, acct, 30000, 500,
                                                      testMapInMap, False)
        print("txhash: ", txhash)
        response = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, acct, acct, 0,0, testMapInMap, True)
        print("testMapInMap: ",response)
        return response

    def test_Get_Map_In_Map(self,str_args: str) -> str:
        testGetMapInMap = self.__abi_info.get_function('testGetMapInMap')
        testGetMapInMap.set_params_value((str_args,))
        response = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0,0, testGetMapInMap, True)
        print("testGetMapInMap: ",response)
        return response

    def test_transferMulti(self, list_arg: list) -> str:
        transferMulti = self.__abi_info.get_function('transferMulti')
        transferMulti.set_params_value((list_arg,))
        response = self.__sdk.neo_vm().send_transaction(self.__contract_address_bytearray, None, None, 0,0, transferMulti, True)
        print("transferMulti: ",response)
        return response

