import os
import time
import unittest

from ontology.utils.contract import (
    Event,
    Data
)

from ontology.sdk import Ontology
from ontology.wallet.wallet_manager import WalletManager

from src.pythonDemo.src.invoke_hello_ontology import InvokeHelloPython

gas_limit = 20000000
gas_price = 500


class TestHelloOntology(unittest.TestCase):
    def setUp(self):
        root_folder = os.path.dirname(os.path.dirname(__file__))
        wallet_path = os.path.join(root_folder, 'wallet', 'wallet.json')
        self.ontology = Ontology()
        self.ontology.rpc.set_address('http://polaris3.ont.io:20336')
        self.ontology.wallet_manager.open_wallet(wallet_path)
        self.acct = self.ontology.wallet_manager.get_account_by_b58_address('AKeDu9QW6hfAhwpvCwNNwkEQt1LkUQpBpW',
                                                                            'password')
        self.hex_contract_address = '6fa374c57ea53680f5733d789a4f03b0ea45d82e'
        self.hello_ontology = InvokeHelloPython(self.ontology, self.hex_contract_address)

    def test_name(self):
        response = self.hello_ontology.name()
        self.assertEqual('name', response)

    def test_hello(self):
        msg = 'ontology'
        response = self.hello_ontology.hello(msg)
        self.assertEqual(msg, response)

    def test_test_hello(self):
        bool_msg = True
        int_msg = 1
        bytes_msg = b'Hello'
        str_msg = 'Hello'
        address_msg = self.acct.get_address().to_bytes()
        tx_hash = self.hello_ontology.test_hello(bool_msg, int_msg, bytes_msg, str_msg, address_msg, self.acct,
                                                 gas_limit,
                                                 gas_price)
        time.sleep(6)
        event = self.ontology.rpc.get_contract_event_by_tx_hash(tx_hash)
        states = Event.get_states_by_contract_address(event, self.hex_contract_address)
        states[0] = Data.to_utf8_str(states[0])
        self.assertEqual('testHello', states[0])
        states[1] = Data.to_bool(states[1])
        self.assertEqual(bool_msg, states[1])
        states[2] = Data.to_int(states[2])
        self.assertEqual(int_msg, states[2])
        states[3] = Data.to_bytes(states[3])
        self.assertEqual(bytes_msg, states[3])
        states[4] = Data.to_utf8_str(states[4])
        self.assertEqual(str_msg, states[4])
        states[5] = Data.to_b58_address(states[5])
        self.assertEqual(self.acct.get_address_base58(), states[5])

    def test_test_list_and_str(self):
        list_msg = [1, 2, 3]
        tx_hash = self.hello_ontology.test_list(list_msg, self.acct, gas_limit, gas_price)
        time.sleep(6)
        event = self.ontology.rpc.get_contract_event_by_tx_hash(tx_hash)
        states = Event.get_states_by_contract_address(event, self.hex_contract_address)
        states[0] = Data.to_utf8_str(states[0])
        self.assertEqual('testMsgList', states[0])
        states[1] = Data.to_int_list(states[1])
        self.assertEqual(list_msg, states[1])

    def test_test_dict_pre_exec(self):
        dict_msg = {'key': 'value'}
        dict_value = self.hello_ontology.test_dict_pre_exec(dict_msg)
        dict_value = Data.to_utf8_str(dict_value.get('Result', ''))
        self.assertEqual('value', dict_value)

    def test_test_dict(self):
        dict_msg = {'key': 'value'}
        tx_hash = self.hello_ontology.test_dict(dict_msg, self.acct, gas_limit, gas_price)
        self.assertEqual(64, len(tx_hash))

    def test_test_get_dict(self):
        key = 'key'
        value = self.hello_ontology.test_get_dict(key)
        value = Data.to_utf8_str(value.get('Result', ''))
        self.assertEqual('value', value)

    def test_test_struct_list_and_str_pre_exec(self):
        bool_msg = True
        int_msg = 10
        bytes_msg = b'Hello'
        str_msg = 'Hello'
        list_msg = [1, 10, 1024, [1, 10, 1024, [1, 10, 1024]]]
        struct_list = [bool_msg, int_msg, bytes_msg, str_msg, list_msg]
        value = self.hello_ontology.test_struct_list_and_str_pre_exec(struct_list, str_msg)
        value[0][0] = Data.to_bool(value[0][0])
        self.assertEqual(bool_msg, value[0][0])
        value[0][1] = Data.to_int(value[0][1])
        self.assertEqual(int_msg, value[0][1])
        value[0][2] = Data.to_bytes(value[0][2])
        self.assertEqual(bytes_msg, value[0][2])
        value[0][3] = Data.to_utf8_str(value[0][3])
        self.assertEqual(str_msg, value[0][3])
        value[0][4] = Data.to_int_list(value[0][4])
        self.assertEqual(list_msg, value[0][4])
        value[1] = Data.to_utf8_str(value[1])
        self.assertEqual(str_msg, value[1])

    def test_test_struct_list_and_str(self):
        bool_msg = True
        int_msg = 10
        bytes_msg = b'Hello'
        str_msg = 'Hello'
        list_msg = [1, 10, 1024, [1, 10, 1024, [1, 10, 1024]]]
        struct_list = [bool_msg, int_msg, bytes_msg, str_msg, list_msg]
        tx_hash = self.hello_ontology.test_struct_list_and_str(struct_list, str_msg, self.acct, gas_limit, gas_price)
        time.sleep(6)
        event = self.ontology.rpc.get_contract_event_by_tx_hash(tx_hash)
        states = Event.get_states_by_contract_address(event, self.hex_contract_address)
        states[0] = Data.to_utf8_str(states[0])
        states[1][0] = Data.to_bool(states[1][0])
        self.assertEqual(bool_msg, states[1][0])
        states[1][1] = Data.to_int(states[1][1])
        self.assertEqual(int_msg, states[1][1])
        states[1][2] = Data.to_bytes(states[1][2])
        self.assertEqual(bytes_msg, states[1][2])
        states[1][3] = Data.to_utf8_str(states[1][3])
        self.assertEqual(str_msg, states[1][3])
        states[1][4] = Data.to_int_list(states[1][4])
        self.assertEqual(list_msg, states[1][4])
        states[2] = Data.to_utf8_str(states[2])

    def test_test_dict_in_ctx(self):
        bool_value = True
        int_value = 100
        str_value = 'value3'
        dict_value = {'key': 'value'}
        list_value = [1, 10, 1024, [1, 10, 1024, [1, 10, 1024]]]
        dict_msg = {'key': dict_value, 'key1': int_value, 'key2': str_value, 'key3': bool_value, 'key4': list_value}
        tx_hash = self.hello_ontology.test_dict_in_ctx(dict_msg, self.acct, gas_limit, gas_price)
        time.sleep(6)
        event = self.ontology.rpc.get_contract_event_by_tx_hash(tx_hash)
        states = Event.get_states_by_contract_address(event, self.hex_contract_address)
        states[0] = Data.to_utf8_str(states[0])
        self.assertEqual('mapInfo', states[0])
        states[1] = Data.to_dict(states[1])
        self.assertTrue(isinstance(states[1], dict))

    def test_test_get_dict_in_ctx(self):
        key = 'key'
        value = self.hello_ontology.test_get_dict_in_ctx(key)
        value = Data.to_utf8_str(value.get('Result', ''))
        self.assertEqual('value', value)

    def test_test_transfer_multi(self):
        bytes_address = self.acct.get_address().to_bytes()
        transfer1 = [bytes_address, bytes_address, 1]
        transfer2 = [bytes_address, bytes_address, 2]
        transfer_list = [transfer1, transfer2]
        tx_hash = self.hello_ontology.test_transfer_multi(transfer_list, self.acct, gas_limit, gas_price)
        time.sleep(6)
        event = self.ontology.rpc.get_contract_event_by_tx_hash(tx_hash)
        self.assertEqual(1, event['State'])


if __name__ == '__main__':
    unittest.main()
