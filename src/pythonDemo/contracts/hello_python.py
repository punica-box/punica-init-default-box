from boa.interop.System.Runtime import Notify
from boa.interop.System.Storage import Put, Get, GetContext
from boa.interop.System.Runtime import Serialize, Deserialize

CTX = GetContext()


def main(operation, args):
    if operation == 'echo':
        return echo(args[0])
    elif operation == 'notify_args':
        return notify_args(args[0], args[1], args[2], args[3], args[4])
    elif operation == 'put_dict':
        return put_dict(args[0])
    elif operation == 'get_dict':
        return get_dict()
    elif operation == 'put_dict_value':
        return put_dict_value(args[0])
    elif operation == 'get_dict_value':
        return get_dict_value()
    elif operation == 'add_key_value_in_dict':
        return add_key_value_in_dict(args[0], args[1])
    elif operation == 'get_value_by_key':
        return get_value_by_key(args[0])
    elif operation == 'put_list':
        return put_list(args[0])
    elif operation == 'get_list':
        return get_list()
    else:
        revert()


def echo(msg):
    return msg


def notify_args(bool_args, int_args, list_args, str_args, bytes_address_args):
    Notify(['notify args', bool_args, int_args, list_args, str_args, bytes_address_args])


def put_dict(dict_args):
    dict_info = Serialize(dict_args)
    Put(CTX, 'dict', dict_info)
    Notify(['put dict', dict_info])


def get_dict():
    dict_info = Get(CTX, 'dict')
    return dict_info


def put_dict_value(dict_value_args):
    new_dict = {}
    new_dict['key'] = dict_value_args
    new_dict_info = Serialize(new_dict)
    Put(CTX, 'dict', new_dict_info)
    Notify(['put dict value', new_dict_info])


def get_dict_value():
    new_dict_info = Get(CTX, 'dict')
    if not new_dict_info:
        revert()
    new_dict = Deserialize(new_dict_info)
    return new_dict['key']


def add_key_value_in_dict(key, value):
    new_dict = {}
    new_dict_info = Get(CTX, 'new_dict')
    if new_dict_info:
        new_dict = Deserialize(new_dict_info)
    new_dict[key] = value
    new_dict_info = Serialize(new_dict)
    Put(CTX, 'new_dict', new_dict_info)
    Notify(['add key value in dict', key, value, new_dict_info])


def get_value_by_key(key):
    new_dict_info = Get(CTX, 'new_dict')
    if not new_dict_info:
        revert()
    new_dict = Deserialize(new_dict_info)
    value = new_dict[key]
    if not value:
        revert()
    return value


def put_list(list_args):
    list_info = Serialize(list_args)
    Put(CTX, 'list', list_info)
    Notify(['put list', list_args, list_info])


def get_list():
    new_list = []
    new_list_info = Get(CTX, 'list')
    if new_list_info:
        new_list = Deserialize(new_list_info)
    return new_list


def revert():
    """
    Revert the transaction. The opcodes of this function is `09f7f6f5f4f3f2f1f000f0`,
    but it will be changed to `ffffffffffffffffffffff` since opcode THROW doesn't
    work, so, revert by calling unused opcode.
    """
    raise Exception(0xF1F1F2F2F3F3F4F4)
