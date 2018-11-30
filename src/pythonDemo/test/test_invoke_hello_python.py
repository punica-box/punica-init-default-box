#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import binascii
import os
import json
import time
import unittest

from ontology.ont_sdk import OntologySdk
from ontology.wallet.wallet_manager import WalletManager

from src.invoke_hello_python import InvokeHelloPython

ontology = OntologySdk()
remote_rpc_address = 'http://polaris3.ont.io:20336'
ontology.set_rpc(remote_rpc_address)

root_folder = os.path.dirname(os.path.dirname(__file__))
wallet_path = os.path.join(root_folder, 'wallet', 'wallet.json')
contracts_folder = os.path.join(root_folder, 'contracts')
contract_address_hex = '4855735ffadad50e7000d73e1c4e96f38d225f70'
gas_limit = 20000000
gas_price = 500

wallet_manager = WalletManager()
wallet_manager.open_wallet(wallet_path)
password = input('password: ')
acct = wallet_manager.get_account('AKeDu9QW6hfAhwpvCwNNwkEQt1LkUQpBpW', password)
with open(os.path.join(contracts_folder, 'hello_python.abi.json')) as f:
    CONTRACT_ABI = json.loads(f.read())
hello_python = InvokeHelloPython(ontology, CONTRACT_ABI, contract_address_hex)


class TestInvokeSavingPot(unittest.TestCase):
    def test_echo(self):
        msg = 'Hello, Ontology'
        response = hello_python.echo(msg)
        self.assertEqual(msg, response)

    def test_notify_args(self):
        bool_args = True
        int_args = 1024
        list_args = [0, 1, 1024, 2048]
        str_args = 'Hello, Ontology'
        bytes_address_args = acct.get_address().to_array()
        tx_hash = hello_python.notify_args(bool_args, int_args, list_args, str_args, bytes_address_args, acct, acct,
                                           gas_limit, gas_price)
        time.sleep(6)
        event = hello_python.query_notify_args_event(tx_hash)
        self.assertIn(bool_args, event)
        self.assertIn(int_args, event)
        self.assertIn(list_args, event)
        self.assertIn(str_args, event)
        self.assertIn(acct.get_address().b58encode(), event)

    def test_put_get_list(self):
        list_args = [0, 1, 1024, 2048]
        tx_hash = hello_python.put_list(list_args, acct, acct, gas_limit, gas_price)
        time.sleep(6)
        event = hello_python.query_put_list_event(tx_hash)
        self.assertIn('put list', event)
        self.assertIn(list_args, event)
        ret_list = hello_python.get_list()
        ret_list = list(map(lambda e: int(''.join(reversed([e[i:i + 2] for i in range(0, len(e), 2)])), 16), ret_list))
        self.assertEqual(list_args, ret_list)

    def test_put_get_dict(self):
        dict_args = {'key1': 'value1'}
        tx_hash = hello_python.put_dict(dict_args, acct, acct, gas_limit, gas_price)
        time.sleep(6)
        event = hello_python.query_put_dict_value_event(tx_hash)
        print(event)
        self.assertIn('put dict', event)
        self.assertIn(binascii.b2a_hex('key1'.encode('ascii')).decode('ascii'), event[1])
        self.assertIn(binascii.b2a_hex('value1'.encode('ascii')).decode('ascii'), event[1])
        dict_info = hello_python.get_dict()
        self.assertEqual(dict_info, event[1])

    def test_put_dict_value(self):
        dict_value_args = 'value'
        tx_hash = hello_python.put_dict_value(dict_value_args, acct, acct, gas_limit, gas_price)
        time.sleep(6)
        event = hello_python.query_put_dict_value_event(tx_hash)
        self.assertIn('put dict value', event)
        value = hello_python.get_dict_value()
        value = binascii.a2b_hex(value).decode('ascii')
        self.assertEqual(dict_value_args, value)

    def test_add_key_value_in_dict(self):
        key = 'key'
        value = 'value'
        tx_hash = hello_python.add_key_value_in_dict(key, value, acct, acct, gas_limit, gas_price)
        time.sleep(6)
        event = hello_python.query_add_key_value_in_dict_event(tx_hash)
        self.assertIn('add key value in dict', event)
        self.assertIn(key, event)
        self.assertIn(value, event)
        self.assertIn({key: value}, event)


if __name__ == '__main__':
    unittest.main()
