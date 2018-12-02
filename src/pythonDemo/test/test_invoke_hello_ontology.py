#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import binascii
import os
import json
import time
import unittest

from ontology.ont_sdk import OntologySdk
from ontology.wallet.wallet_manager import WalletManager

from src.invoke_hello_ontology import InvokeHelloOntology

ontology = OntologySdk()
remote_rpc_address = 'http://polaris3.ont.io:20336'
# remote_rpc_address = 'http://127.0.0.1:20336'
ontology.set_rpc(remote_rpc_address)

root_folder = os.path.dirname(os.path.dirname(__file__))
wallet_path = os.path.join(root_folder, 'wallet', 'wallet.json')

contract_address_hex = '16edbe366d1337eb510c2ff61099424c94aeef02'
gas_limit = 20000000
gas_price = 500

wallet_manager = WalletManager()
wallet_manager.open_wallet(wallet_path)
# password = input('password: ')
acct = wallet_manager.get_account('AUr5QUfeBADq6BMY6Tp5yuMsUNGpsD7nLZ', "password")

hello_ontology = InvokeHelloOntology(ontology, contract_address_hex)


class TestInvokeSavingPot(unittest.TestCase):
    # def test_name(self):
    #     resp = hello_ontology.name()
    #     #self.assertEqual(msg, response)
    #
    # def test_Hello(self):
    #     bool_arg = True
    #     int_arg = 1024
    #     bys_arg = b'aabb'
    #     str_args = 'Hello, Ontology'
    #     bytes_address_arg = acct.get_address().to_array()
    #     resp = hello_ontology.test_Hello(bool_arg, int_arg, bys_arg, str_args, bytes_address_arg)
    #
    # def test_List(self):
    #     bool_arg = True
    #     int_arg = 1024
    #     bys_arg = b'aabb'
    #     str_arg = 'hello'
    #     bytes_address_arg = acct.get_address().to_array()
    #     list_args = [bool_arg, int_arg, bys_arg,str_arg,bytes_address_arg]
    #
    #     resp = hello_ontology.test_List(list_args)
    #
    # def test_List_And_Str(self):
    #     bool_arg = True
    #     int_arg = 1024
    #     bys_arg = b'aabb'
    #     str_arg = 'hello'
    #     bytes_address_arg = acct.get_address().to_array()
    #     list_args = [bool_arg, int_arg, bys_arg, str_arg, bytes_address_arg]
    #
    #     resp = hello_ontology.test_List_And_Str(list_args,str_arg)

    def test_Struct_List(self):
        bool_arg = True
        int_arg = 1024
        bys_arg = b'aabb'
        str_arg = 'hello'
        struct = [bool_arg, int_arg, bys_arg,str_arg]
        struct2 = [False, 10, bys_arg, str_arg]
        list_args = [struct,struct2]

        resp = hello_ontology.test_Struct_List(list_args)

    # def test_Struct_List_And_Str(self):
    #     bool_arg = True
    #     int_arg = 1024
    #     bys_arg = b'aabb'
    #     str_arg = 'hello'
    #     bytes_address_arg = acct.get_address().to_array()
    #     list_args = [[bool_arg, int_arg, bys_arg, str_arg, bytes_address_arg],[bool_arg, int_arg, bys_arg, str_arg, bytes_address_arg]]
    #
    #     resp = hello_ontology.test_Struct_List_And_Str(list_args,str_arg)

    # def test_Map(self):
    #     bool_arg = True
    #     int_arg = 1024
    #     bys_arg = b'aabb'
    #     str_arg = 'hello'
    #     dict_args = {'key': str_arg,'key1': bool_arg,'key2': int_arg,'key3': bys_arg}
    #     resp = hello_ontology.test_Map(dict_args,acct)

    # def test_Get_Map(self):
    #     resp = hello_ontology.test_Get_Map('key')

    # def test_Map_In_Map(self):
    #     bool_arg = True
    #     int_arg = 1024
    #     bys_arg = b'aabb'
    #     str_arg = 'hello'
    #     list_arg = [str_arg]
    #     dict_args = {'key': str_arg,'key1': bool_arg,'key2': int_arg,'key3': bys_arg,'key4': list_arg}
    #     dict_args2 = {'key': dict_args, 'key11': 'hello2'}
    #     resp = hello_ontology.test_Map_In_Map(dict_args2,acct)

    # def test_Get_Map_In_Map(self):
    #     resp = hello_ontology.test_Get_Map_In_Map('key2')

    def test_transferMulti(self):
        state = [acct.get_address().to_array(),acct.get_address().to_array(),10]
        state2 = [acct.get_address().to_array(), acct.get_address().to_array(), 100]
        resp = hello_ontology.test_transferMulti([state,state2])





if __name__ == '__main__':
    unittest.main()
