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
contract_address_hex = '6690b6638251be951dded8c537678200a470c679'
gas_limit = 20000000
gas_price = 500

wallet_manager = WalletManager()
wallet_manager.open_wallet(wallet_path)
password = input('password: ')
acct = wallet_manager.get_account('AKeDu9QW6hfAhwpvCwNNwkEQt1LkUQpBpW', password)
with open(os.path.join(contracts_folder, 'hello_ontology.abi.json')) as f:
    CONTRACT_ABI = json.loads(f.read())
hello_ontology = InvokeHelloPython(ontology, CONTRACT_ABI, contract_address_hex)


class TestHelloOntology(unittest.TestCase):
    def test_name(self):
        response = hello_ontology.name()
        print(response)

    def test_hello(self):
        msg = 'ontology'
        response = hello_ontology.hello(msg)
        print(response)

    def test_test_hello(self):
        bool_msg = True
        int_msg = 1
        bytes_msg = b'Hello'
        str_msg = 'Hello'
        address_msg = acct.get_address().to_array()
        tx_hash = hello_ontology.test_hello(bool_msg, int_msg, bytes_msg, str_msg, address_msg, acct, acct, gas_limit,
                                            gas_price)
        time.sleep(6)
        event = ontology.rpc.get_smart_contract_event_by_tx_hash(tx_hash)
        print(event)

    def test_test_list_and_str(self):
        list_msg = [1, 2, 3]
        tx_hash = hello_ontology.test_list_and_str(list_msg, acct, acct, gas_limit, gas_price)
        time.sleep(6)
        event = ontology.rpc.get_smart_contract_event_by_tx_hash(tx_hash)
        print(event)

    def test_test_dict(self):
        dict_msg = {'key': 'value'}
        dict_value = hello_ontology.test_dict(dict_msg)
        print(dict_value)

    def test_test_get_map(self):
        key = 'key'
        value = hello_ontology.test_get_dict(key)
        print(value)

    def test_test_dict_in_ctx(self):
        dict_msg = {'key': {'key': 'value'}}
        tx_hash = hello_ontology.test_dict_in_ctx(dict_msg, acct, acct, gas_limit, gas_price)
        time.sleep(6)
        event = ontology.rpc.get_smart_contract_event_by_tx_hash(tx_hash)
        print(event)

    def test_test_get_dict_in_ctx(self):
        key = 'key'
        value = hello_ontology.test_get_dict_in_ctx(key)
        print(value)

    def test_test_transfer_multi(self):
        bytes_address = acct.get_address().to_array()
        transfer1 = [bytes_address, bytes_address, 1]
        transfer2 = [bytes_address, bytes_address, 2]
        args = [transfer1, transfer2]
        tx_hash = hello_ontology.test_transfer_multi(args, acct, acct, gas_limit, gas_price)
        print(tx_hash)


if __name__ == '__main__':
    unittest.main()
