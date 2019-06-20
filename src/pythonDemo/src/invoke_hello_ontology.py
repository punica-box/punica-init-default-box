from ontology.sdk import Ontology
from ontology.utils.contract import Data
from ontology.account.account import Account
from ontology.contract.neo.invoke_function import InvokeFunction


class InvokeHelloPython(object):
    def __init__(self, sdk: Ontology, hex_contract_address: str):
        if not isinstance(sdk, Ontology):
            raise RuntimeError('the type of sdk is error')
        if not isinstance(hex_contract_address, str):
            raise RuntimeError('the type of contract address should be str')
        if len(hex_contract_address) != 40:
            raise RuntimeError()
        self.__sdk = sdk
        self.__hex_contract_address = hex_contract_address

    def name(self):
        func = InvokeFunction('name')
        tx = self.__sdk.neo_vm.make_invoke_transaction(self.__hex_contract_address, func)
        value = self.__sdk.rpc.send_raw_transaction_pre_exec(tx)
        return Data.to_utf8_str(value.get('Result', ''))

    def hello(self, msg: str) -> str:
        if not isinstance(msg, str):
            raise RuntimeError('the type of msg should be str')
        func = InvokeFunction('hello')
        func.set_params_value(msg)
        tx = self.__sdk.neo_vm.make_invoke_transaction(self.__hex_contract_address, func)
        value = self.__sdk.rpc.send_raw_transaction_pre_exec(tx)
        return Data.to_utf8_str(value.get('Result', ''))

    def test_hello(self, bool_msg, int_msg, bytes_msg, str_msg, bytes_address_msg: bytes, payer_acct: Account,
                   gas_limit: int, gas_price: int) -> str:
        func = InvokeFunction('testHello')
        func.set_params_value(bool_msg, int_msg, bytes_msg, str_msg, bytes_address_msg)
        tx = self.__sdk.neo_vm.make_invoke_transaction(self.__hex_contract_address, func, payer_acct.get_address(),
                                                       gas_price, gas_limit)
        tx.sign_transaction(payer_acct)
        tx_hash = self.__sdk.rpc.send_raw_transaction(tx)
        return tx_hash

    def test_list(self, list_msg: list, payer_acct, gas_limit, gas_price):
        func = InvokeFunction('testList')
        func.set_params_value(list_msg)
        tx = self.__sdk.neo_vm.make_invoke_transaction(self.__hex_contract_address, func, payer_acct.get_address(),
                                                       gas_price, gas_limit)
        tx.sign_transaction(payer_acct)
        tx_hash = self.__sdk.rpc.send_raw_transaction(tx)
        return tx_hash

    def test_dict_pre_exec(self, dict_msg: dict):
        func = InvokeFunction('testMap')
        func.set_params_value(dict_msg)
        tx = self.__sdk.neo_vm.make_invoke_transaction(self.__hex_contract_address, func)
        value = self.__sdk.rpc.send_raw_transaction_pre_exec(tx)
        return value

    def test_dict(self, dict_msg: dict, payer_acct: Account, gas_limit, gas_price):
        func = InvokeFunction('testMap')
        func.set_params_value(dict_msg)
        tx = self.__sdk.neo_vm.make_invoke_transaction(self.__hex_contract_address, func, payer_acct.get_address(),
                                                       gas_price, gas_limit)
        tx.sign_transaction(payer_acct)
        tx_hash = self.__sdk.rpc.send_raw_transaction(tx)
        return tx_hash

    def test_struct_list_and_str_pre_exec(self, struct_list, str_msg):
        func = InvokeFunction('testStructListAndStr')
        func.set_params_value(struct_list, str_msg)
        tx = self.__sdk.neo_vm.make_invoke_transaction(self.__hex_contract_address, func)
        value = self.__sdk.rpc.send_raw_transaction_pre_exec(tx)
        return value.get('Result', list())

    def test_struct_list_and_str(self, struct_list, str_msg, payer_acct: Account, gas_limit, gas_price):
        func = InvokeFunction('testStructListAndStr')
        func.set_params_value(struct_list, str_msg)
        tx = self.__sdk.neo_vm.make_invoke_transaction(self.__hex_contract_address, func, payer_acct.get_address(),
                                                       gas_price, gas_limit)
        tx.sign_transaction(payer_acct)
        tx_hash = self.__sdk.rpc.send_raw_transaction(tx)
        return tx_hash

    def test_get_dict(self, key):
        func = InvokeFunction('testGetMap')
        func.set_params_value(key)
        tx = self.__sdk.neo_vm.make_invoke_transaction(self.__hex_contract_address, func)
        value = self.__sdk.rpc.send_raw_transaction_pre_exec(tx)
        return value

    def test_dict_in_ctx(self, map_msg, payer_acct, gas_limit, gas_price):
        func = InvokeFunction('testMapInMap')
        func.set_params_value(map_msg)
        tx = self.__sdk.neo_vm.make_invoke_transaction(self.__hex_contract_address, func, payer_acct.get_address(),
                                                       gas_price, gas_limit)
        tx.sign_transaction(payer_acct)
        tx_hash = self.__sdk.rpc.send_raw_transaction(tx)
        return tx_hash

    def test_get_dict_in_ctx(self, key):
        func = InvokeFunction('testGetMapInMap')
        func.set_params_value(key)
        tx = self.__sdk.neo_vm.make_invoke_transaction(self.__hex_contract_address, func)
        value = self.__sdk.rpc.send_raw_transaction_pre_exec(tx)
        return value

    def test_transfer_multi(self, transfer_list, payer_acct, gas_limit, gas_price):
        func = InvokeFunction('transferMulti')
        func.set_params_value(transfer_list)
        tx = self.__sdk.neo_vm.make_invoke_transaction(self.__hex_contract_address, func, payer_acct.get_address(),
                                                       gas_price, gas_limit)
        tx.sign_transaction(payer_acct)
        tx_hash = self.__sdk.rpc.send_raw_transaction(tx)
        return tx_hash
