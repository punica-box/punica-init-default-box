#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import binascii
import os
import json
import time
import unittest

from ontology.ont_sdk import OntologySdk
from ontology.utils.contract_data_parser import ContractDataParser
from ontology.utils.contract_event_parser import ContractEventParser
from ontology.wallet.wallet_manager import WalletManager

from src.invoke_hello_python import InvokeHelloPython

ontology = OntologySdk()
remote_rpc_address = 'http://polaris3.ont.io:20336'
ontology.set_rpc(remote_rpc_address)

root_folder = os.path.dirname(os.path.dirname(__file__))
wallet_path = os.path.join(root_folder, 'wallet', 'wallet.json')
contracts_folder = os.path.join(root_folder, 'contracts')
hex_contract_address = '16edbe366d1337eb510c2ff61099424c94aeef02'
gas_limit = 20000000
gas_price = 500

wallet_manager = WalletManager()
wallet_manager.open_wallet(wallet_path)
# password = input('password: ')
password = 'password'
acct = wallet_manager.get_account('AKeDu9QW6hfAhwpvCwNNwkEQt1LkUQpBpW', password)
with open(os.path.join(contracts_folder, 'hello_ontology.abi.json')) as f:
    CONTRACT_ABI = json.loads(f.read())
hello_ontology = InvokeHelloPython(ontology, CONTRACT_ABI, hex_contract_address)


class TestHelloOntology(unittest.TestCase):
    def test_name(self):
        response = hello_ontology.name()
        self.assertEqual('name', response)

    def test_hello(self):
        msg = 'ontology'
        response = hello_ontology.hello(msg)
        self.assertEqual(msg, response)

    def test_test_hello(self):
        bool_msg = True
        int_msg = 1
        bytes_msg = b'Hello'
        str_msg = 'Hello'
        address_msg = acct.get_address().to_bytes()
        tx_hash = hello_ontology.test_hello(bool_msg, int_msg, bytes_msg, str_msg, address_msg, acct, gas_limit,
                                            gas_price)
        time.sleep(6)
        event = ontology.rpc.get_smart_contract_event_by_tx_hash(tx_hash)
        states = ContractEventParser.get_states_by_contract_address(event, hex_contract_address)
        states[0] = ContractDataParser.to_utf8_str(states[0])
        self.assertEqual('testHello', states[0])
        states[1] = ContractDataParser.to_bool(states[1])
        self.assertEqual(bool_msg, states[1])
        states[2] = ContractDataParser.to_int(states[2])
        self.assertEqual(int_msg, states[2])
        states[3] = ContractDataParser.to_bytes(states[3])
        self.assertEqual(bytes_msg, states[3])
        states[4] = ContractDataParser.to_utf8_str(states[4])
        self.assertEqual(str_msg, states[4])
        states[5] = ContractDataParser.to_b58_address(states[5])
        self.assertEqual(acct.get_address_base58(), states[5])

    def test_test_list_and_str(self):
        list_msg = [1, 2, 3]
        tx_hash = hello_ontology.test_list(list_msg, acct, gas_limit, gas_price)
        time.sleep(6)
        event = ontology.rpc.get_smart_contract_event_by_tx_hash(tx_hash)
        print(event)

    def test_test_dict(self):
        dict_msg = {'key': 'value'}
        dict_value = hello_ontology.test_dict(dict_msg)
        self.assertEqual('value', dict_value)

    def test_test_get_dict(self):
        key = 'key'
        value = hello_ontology.test_get_dict(key)
        print(value)

    def test_test_dict_in_ctx(self):
        bool_value = True
        int_value = 100
        str_value = 'value3'
        dict_value = {'key': 'value'}
        list_value = [1, 10, 1024, [1, 10, 1024, [1, 10, 1024]]]
        dict_msg = {'key': dict_value, 'key1': int_value, 'key2': str_value, 'key3': bool_value, 'key4': list_value}
        tx_hash = hello_ontology.test_dict_in_ctx(dict_msg, acct, gas_limit, gas_price)
        time.sleep(6)
        event = ontology.rpc.get_smart_contract_event_by_tx_hash(tx_hash)
        states = ContractEventParser.get_states_by_contract_address(event, hex_contract_address)
        states[0] = ContractDataParser.to_utf8_str(states[0])
        self.assertEqual('mapInfo', states[0])
        states[1] = ContractDataParser.to_dict(states[1])
        self.assertTrue(isinstance(states[1], dict))

    def test_test_get_dict_in_ctx(self):
        key = 'key'
        value = hello_ontology.test_get_dict_in_ctx(key)
        value = ContractDataParser.to_utf8_str(value)
        self.assertEqual('value', value)

    def test_test_transfer_multi(self):
        bytes_address = acct.get_address().to_bytes()
        transfer1 = [bytes_address, bytes_address, 1]
        transfer2 = [bytes_address, bytes_address, 2]
        transfer_list = [transfer1, transfer2]
        tx_hash = hello_ontology.test_transfer_multi(transfer_list, acct, gas_limit, gas_price)
        time.sleep(6)
        event = ontology.rpc.get_smart_contract_event_by_tx_hash(tx_hash)
        self.assertEqual(1, event['State'])


if __name__ == '__main__':
    unittest.main()
