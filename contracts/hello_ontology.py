from boa.interop.System.Runtime import Notify

def Main(operation, args):
    if operation == 'hello':
        msg = args[0]
        return hello(msg)
    if operation == 'testListNum':
        if len(args) != 1:
            return False
        msgList = args[0]
        return testListNum(msgList)
    if operation == 'testListNumStr':
        Notify([args])
        if len(args) != 2:
            return False
        msgList = args[0]
        msg = args[1]
        return testListNumStr(msgList, msg)
    if operation == 'testListStr':
        if len(args) != 2:
            return False
        msgList = args[0]
        msg = args[1]
        return testListStr(msgList, msg)
    if operation == 'testListByteArray':
        if len(args) !=2:
            return False
        msgList = args[0]
        msg = args[1]
        return testListByteArray(msgList, msg)
    if operation == 'testListStruct':
        Notify(args)
        msgList = args[0]
        return testListStruct(msgList)
    if operation == 'testListStructStr':
        if len(args) !=2:
            return False
        msgList = args[0]
        msg = args[1]
        return testListStruct(msgList,msg)
    return False

def hello(msg):
    Notify([msg])
    return msg

def testListNum(msg):
    Notify([msg])
    return msg

def testListNumStr(msgList, msg):
    Notify([msgList])
    Notify([msg])
    resList = []
    resList.append(msgList)
    resList.append(msg)
    return resList

def testListStr(msgList, msg):
    Notify([msgList])
    Notify([msg])
    resList = []
    resList.append(msgList)
    resList.append(msg)
    return resList
def testListByteArray(msgList, msg):
    Notify([msgList])
    Notify([msg])
    resList = []
    resList.append(msgList)
    resList.append(msg)
    return resList
def testListStruct(msgList):
    Notify([msgList])
    return msgList
def testListStructStr(msgList, msg):
    Notify([msgList, msg])
    resList = []
    resList.append(msgList)
    resList.append(msg)
    return resList
