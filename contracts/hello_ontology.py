from boa.interop.System.Runtime import Log


def Main(operation, args):
    if operation == 'hello':
        msg = args[0]
        return hello(msg)

    return False


def hello(msg):
    Log(msg)
    return True
