from boa.interop.System.Runtime import Notify

def Main(operation, args):
    if operation == 'testHello':
        if len(args) != 6:
            return False
        msgBool = args[0]
        msgInt = args[1]
        msgByteArray = args[2]
        msgStr = args[3]
        msgHex = args[4]
        msgAddress = args[5]
        return testHello(msgBool, msgInt, msgByteArray,msgStr,msgHex,msgAddress)
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
    return False

def testHello(msgBool, msgInt, msgByteArray,msgStr,msgHex,msgAddress):
    Notify(["testHello",msgBool, msgInt, msgByteArray,msgStr,msgHex,msgAddress])
    resList = []
    resList.append(msgBool)
    resList.append(msgInt)
    resList.append(msgByteArray)
    resList.append(msgStr)
    resList.append(msgHex)
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
