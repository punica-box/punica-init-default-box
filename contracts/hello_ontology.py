from boa.interop.System.Runtime import Notify
from boa.interop.System.Storage import Put, Get, GetContext

def Main(operation, args):
    if operation == 'hello':
        if len(args) != 1:
            return False
        msg = args[0]
        return hello(msg)
    if operation == 'testHello':
        if len(args) != 5:
            return False
        msgBool = args[0]
        msgInt = args[1]
        msgByteArray = args[2]
        msgStr = args[3]
        msgAddress = args[4]
        return testHello(msgBool, msgInt, msgByteArray,msgStr,msgAddress)
    if operation == 'testNumList':
        if len(args) != 1:
            return False
        numList = args[0]
        return testNumList(numList)
    if operation == 'testNumListAndStr':
        Notify([args])
        if len(args) != 2:
            return False
        numList = args[0]
        msgStr = args[1]
        return testNumListAndStr(numList, msgStr)
    if operation == 'testStrListAndStr':
        if len(args) != 2:
            return False
        strList = args[0]
        msgStr = args[1]
        return testStrListAndStr(strList, msgStr)
    if operation == 'testByteArrayListAndStr':
        if len(args) !=2:
            return False
        msgList = args[0]
        msg = args[1]
        return testByteArrayListAndStr(msgList, msg)
    if operation == 'testStructList':
        Notify(args)
        structList = args[0]
        return testStructList(structList)
    if operation == 'testStructListAndStr':
        if len(args) !=2:
            return False
        structList = args[0]
        msgStr = args[1]
        return testStructListAndStr(structList,msgStr)
    if operation == 'testMap':
        msg = args[0]
        return testMap(msg)
    if operation == 'testGetMap':
        if len(args) != 1:
            return False
        key = args[0]
        return testGetMap(key)
    if operation == 'testMapInMap':
        msg = args[0]
        return testMapInMap(msg)
    if operation == 'testGetMapInMap':
        if len(args) != 1:
            return False
        key = args[0]
        return testGetMapInMap(key)
    if operation == 'transferMulti':
        states = args[0]
        return transferMulti(states)
    return False

def hello(msg):
    return msg

def testHello(msgBool, msgInt, msgByteArray,msgStr,msgAddress):
    Notify(["testHello",msgBool, msgInt, msgByteArray,msgStr,msgAddress])
    resList = []
    resList.append(msgBool)
    resList.append(msgInt)
    resList.append(msgByteArray)
    resList.append(msgStr)
    resList.append(msgAddress)
    return resList

def testNumList(numList):
    Notify(["testNumList", numList])
    return numList

def testNumListAndStr(numList, msgStr):
    Notify(["testNumListAndStr",numList,msgStr])
    resList = []
    resList.append(numList)
    resList.append(msgStr)
    return resList

def testStrListAndStr(strList, msgStr):
    Notify(["testStrListAndStr", strList, msgStr])
    resList = []
    resList.append(strList)
    resList.append(msgStr)
    return resList

def testByteArrayListAndStr(bytearrayList, msgStr):
    Notify(["testByteArrayListAndStr", bytearrayList, msgStr])
    resList = []
    resList.append(bytearrayList)
    resList.append(msgStr)
    return resList

def testStructList(structList):
    Notify(["testStructList", structList])
    return structList
def testStructListAndStr(structList, msgStr):
    Notify(["testStructListAndStr", structList, msgStr])
    resList = []
    resList.append(structList)
    resList.append(msgStr)
    return resList

def testMap(msg):
    map = msg #Deserialize(msg)
    mapInfo = Serialize(map)
    Put(GetContext(), 'map_key', mapInfo)
    return map['key']
def testGetMap(key):
    mapInfo = Get(GetContext(), 'map_key')
    map = Deserialize(mapInfo)
    return map[key]

def testMapInMap(msg):
    map = msg #Deserialize(msg)
    mapInfo = Serialize(map)
    Notify(["mapInfo",mapInfo])
    mapInfo2 = Serialize(map['key'])
    Put(GetContext(), 'map_key2', mapInfo2)
    return mapInfo
def testGetMapInMap(key):
    mapInfo = Get(GetContext(), 'map_key2')
    map = Deserialize(mapInfo)
    return map[key]

def transfer(from_acct,to_acct,amount):
    return True
def transferMulti(states):
    """
    :param states: the parameter is an array, containing element like [from, to, amount]
    :return: True means success, False or raising exception means failure.
    """
    for p in states:
        if len(p) != 3:
            # return False is wrong
            raise Exception("transferMulti params error.")
        if transfer(p[0], p[1], p[2]) == False:
            # return False is wrong since the previous transaction will be successful
            raise Exception("transferMulti failed.")
    return True
