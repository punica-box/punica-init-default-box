package com.java.example.demo.com.java.example.service;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.github.ontio.OntSdk;
import com.github.ontio.account.Account;
import com.github.ontio.common.Address;
import com.github.ontio.common.Helper;
import com.github.ontio.core.transaction.Transaction;
import com.github.ontio.crypto.SignatureScheme;
import com.github.ontio.sdk.exception.SDKException;
import com.github.ontio.smartcontract.neovm.abi.BuildParams;
import com.github.ontio.smartcontract.neovm.abi.Struct;
import org.bouncycastle.util.encoders.Hex;

import java.util.ArrayList;
import java.util.Base64;
import java.util.List;

public class ContractService {
    private final static ContractService contractService = new ContractService();

    private static OntSdk ontSdk = null;

    public static String contractCode = "0140c56b6a00527ac46a51527ac46a00c30568656c6c6f9c6424006a51c3c0519e640700006c7566616a51c300c36a52527ac46a52c36531066c7566616a00c3097465737448656c6c6f9c646c006a51c3c0559e640700006c7566616a51c300c36a53527ac46a51c351c36a54527ac46a51c352c36a55527ac46a51c353c36a56527ac46a51c354c36a57527ac46a53c36a54c36a55c36a56c36a57c354795179567275517275537952795572755272756533056c7566616a00c30b746573744e756d4c6973749c6424006a51c3c0519e640700006c7566616a51c300c36a58527ac46a58c365c5046c7566616a00c311746573744e756d4c697374416e645374729c6451006a51c351c176c9681553797374656d2e52756e74696d652e4e6f74696679616a51c3c0529e640700006c7566616a51c300c36a58527ac46a51c351c36a56527ac46a58c36a56c37c65ff036c7566616a00c311746573745374724c697374416e645374729c6432006a51c3c0529e640700006c7566616a51c300c36a59527ac46a51c351c36a56527ac46a59c36a56c37c6558036c7566616a00c317746573744279746541727261794c697374416e645374729c6432006a51c3c0529e640700006c7566616a51c300c36a5a527ac46a51c351c36a52527ac46a5ac36a52c37c65a5026c7566616a00c30e746573745374727563744c6973749c6431006a51c3681553797374656d2e52756e74696d652e4e6f74696679616a51c300c36a5b527ac46a5bc36524026c7566616a00c314746573745374727563744c697374416e645374729c6432006a51c3c0529e640700006c7566616a51c300c36a5b527ac46a51c351c36a56527ac46a5bc36a56c37c6577016c7566616a00c307746573744d61709c6432006a51c3c0529e640700006c7566616a51c300c36a5c527ac46a51c351c36a5d527ac46a5cc36a5dc37c65b5006c7566616a00c30a746573744765744d61709c6424006a51c3c0519e640700006c7566616a51c300c36a5c527ac46a5cc3650b006c756661006c756656c56b6a00527ac4681953797374656d2e53746f726167652e476574436f6e7465787461076d61705f6b65797c681253797374656d2e53746f726167652e476574616a51527ac46a51c3681a53797374656d2e52756e74696d652e446573657269616c697a65616a52527ac46a52c36a00c3c36c756659c56b6a00527ac46a51527ac4c76a52527ac46a51c36a52c36a00c37bc46a52c3681853797374656d2e52756e74696d652e53657269616c697a65616a53527ac4681953797374656d2e53746f726167652e476574436f6e7465787461076d61705f6b65796a53c35272681253797374656d2e53746f726167652e50757461516c756659c56b6a00527ac46a51527ac414746573745374727563744c697374416e645374726a00c36a51c353c176c9681553797374656d2e52756e74696d652e4e6f746966796100c176c96a52527ac46a52c36a00c3c86a52c36a51c3c86a52c36c756655c56b6a00527ac40e746573745374727563744c6973746a00c352c176c9681553797374656d2e52756e74696d652e4e6f74696679616a00c36c756659c56b6a00527ac46a51527ac417746573744279746541727261794c697374416e645374726a00c36a51c353c176c9681553797374656d2e52756e74696d652e4e6f746966796100c176c96a52527ac46a52c36a00c3c86a52c36a51c3c86a52c36c756659c56b6a00527ac46a51527ac411746573745374724c697374416e645374726a00c36a51c353c176c9681553797374656d2e52756e74696d652e4e6f746966796100c176c96a52527ac46a52c36a00c3c86a52c36a51c3c86a52c36c756659c56b6a00527ac46a51527ac411746573744e756d4c697374416e645374726a00c36a51c353c176c9681553797374656d2e52756e74696d652e4e6f746966796100c176c96a52527ac46a52c36a00c3c86a52c36a51c3c86a52c36c756655c56b6a00527ac40b746573744e756d4c6973746a00c352c176c9681553797374656d2e52756e74696d652e4e6f74696679616a00c36c75665fc56b6a00527ac46a51527ac46a52527ac46a53527ac46a54527ac4097465737448656c6c6f6a00c36a51c36a52c36a53c36a54c356c176c9681553797374656d2e52756e74696d652e4e6f746966796100c176c96a55527ac46a55c36a00c3c86a55c36a51c3c86a55c36a52c3c86a55c36a53c3c86a55c36a54c3c86a55c36c756654c56b6a00527ac46a00c36c7566";

    private ContractService(){
    }

    public static ContractService getInstance(){
        return contractService;
    }

    public static void testDemo(){
        try{
            ontSdk = getOntSdk();
            String privateKey = Account.getGcmDecodedPrivateKey("DFx14facOecataYeUtp1ZAHzyfse6zJAiwksdDFjqkB38XEaKACAjUAyA9MUwx24","7217486","AL42aUzAGJ18LdjjH6ppt29LLn8CvTcViq",Base64.getDecoder().decode("U5CfqUb/FUHOn1tiGACueg=="),4096,SignatureScheme.SHA256WITHECDSA);
            Account account = new Account(Helper.hexToBytes(privateKey),SignatureScheme.SHA256WITHECDSA);

            // 部署punica-init-default-box/contracts/hello_ontology.py 合约
            if(false){
                System.out.println("Test Function deployContract start -------");
                System.out.println("ContractAddress:" + Address.AddressFromVmCode(contractCode).toHexString());

                ontSdk.vm().setCodeAddress(Address.AddressFromVmCode(contractCode).toHexString());
                Transaction tx = ontSdk.vm().makeDeployCodeTransaction(contractCode, true, "name",
                        "v1.0", "author", "email", "desp", account.getAddressU160().toBase58(),30000000L,0);
                ontSdk.signTx(tx, new Account[][]{{account}});
                String txHex = Helper.toHexString(tx.toArray());

                System.out.println(txHex);
                Object result = ontSdk.getConnect().syncSendRawTransaction(txHex);
                System.out.println(result);
            }

            // 测试hello方法，合约中要求args.len等于1，否则返回false
            if(true){
                System.out.println("Test Function hello start -------");
                List paramList = new ArrayList<>();
                paramList.add("hello".getBytes());

                List contractArgs = new ArrayList();
                contractArgs.add("hello function param0");

                paramList.add(contractArgs);
                byte[] params = BuildParams.createCodeParamsScript(paramList);

                String result = callContract(params, account, 20000, 500);
                System.out.println("hello return is:  " + new String(Hex.decode(JSON.parseObject(result).getString("Result"))));
            }

            // 测试testHello方法，合约要求参数个数为5
            if(true){
                System.out.println("Test Function testHello start -------");
                List paramList = new ArrayList<>();
                paramList.add("testHello".getBytes());

                List contractArgs = new ArrayList();
                contractArgs.add(true);
                contractArgs.add(2);
                contractArgs.add("thirdParam".getBytes());
                contractArgs.add("fourthParam");
                contractArgs.add(account.getAddressU160().toBase58());

                paramList.add(contractArgs);
                byte[] params = BuildParams.createCodeParamsScript(paramList);

                String result = callContract(params, account, 20000, 500);
                List<String > resultList = JSON.parseObject(JSON.parseObject(result).getString("Result"), List.class);
                System.out.println("testHello return size is:  " + resultList.size());
                System.out.println("testHello forth return is:  " + new String(Hex.decode(resultList.get(4))));
            }

            // 测试testNumList方法，合约要求参数个数为1
            if(true){
                System.out.println("Test Function testNumList start -------");
                List paramList = new ArrayList<>();
                paramList.add("testNumList".getBytes());

                List contractArgs = new ArrayList();
                List contractArgs2 = new ArrayList();
                contractArgs2.add(2);
                contractArgs.add(contractArgs2);

                paramList.add(contractArgs);
                byte[] params = BuildParams.createCodeParamsScript(paramList);


                String result = callContract(params, account, 20000, 500);
                List<String > resultList = JSON.parseObject(JSON.parseObject(result).getString("Result"), List.class);
                System.out.println("testNumList return size is:  " + resultList.size());
                System.out.println("testNumList return is:  " + Integer.valueOf(resultList.get(0)));
            }

            // 测试testNumListAndStr方法，合约要求参数个数为2
            if(true){
                System.out.println("Test Function testNumListAndStr start -------");
                List paramList = new ArrayList<>();
                paramList.add("testNumListAndStr".getBytes());

                List contractArgs = new ArrayList();
                List contractArgs2 = new ArrayList();
                contractArgs2.add(2);
                contractArgs.add(contractArgs2);
                contractArgs.add("msgStrParam");

                paramList.add(contractArgs);
                byte[] params = BuildParams.createCodeParamsScript(paramList);


                String result = callContract(params, account, 20000, 500);
                List<String > resultList = JSON.parseObject(JSON.parseObject(result).getString("Result"), List.class);
                System.out.println("testNumListAndStr return size is:  " + resultList.size());
                System.out.println("testNumListAndStr Str return is:  " + new String(Hex.decode(resultList.get(1))));
            }

            // 测试testStrListAndStr方法，合约要求参数个数为2
            if(true){
                System.out.println("Test Function testStrListAndStr start -------");
                List paramList = new ArrayList<>();
                paramList.add("testStrListAndStr".getBytes());

                List contractArgs = new ArrayList();
                List contractArgs2 = new ArrayList();
                contractArgs2.add("msgStrListParam");
                contractArgs.add(contractArgs2);
                contractArgs.add("msgStrParam");

                paramList.add(contractArgs);
                byte[] params = BuildParams.createCodeParamsScript(paramList);

                String result = callContract(params, account, 20000, 500);
                List<String > resultList = JSON.parseObject(JSON.parseObject(result).getString("Result"), List.class);

                System.out.println("testStrListAndStr return size is:  " + resultList.size());
                System.out.println("testStrListAndStr first param return is:  " + new String(Hex.decode((String) JSON.parseObject(JSONObject.toJSON(resultList.get(0)).toString(), List.class).get(0))));
            }

            // 测试testByteArrayListAndStr方法，合约要求参数个数为2
            if(true){
                System.out.println("Test Function testByteArrayListAndStr start -------");
                List paramList = new ArrayList<>();
                paramList.add("testByteArrayListAndStr".getBytes());

                List contractArgs = new ArrayList();
                List contractArgs2 = new ArrayList();
                contractArgs2.add("byteParam".getBytes());
                contractArgs.add(contractArgs2);
                contractArgs.add("msgStrParam");

                paramList.add(contractArgs);
                byte[] params = BuildParams.createCodeParamsScript(paramList);

                String result = callContract(params, account, 20000, 500);
                List<String > resultList = JSON.parseObject(JSON.parseObject(result).getString("Result"), List.class);
                System.out.println("testByteArrayListAndStr return size is:  " + resultList.size());
                System.out.println("testByteArrayListAndStr first param return is:  " + new String(Hex.decode((String) JSON.parseObject(JSONObject.toJSON(resultList.get(0)).toString(), List.class).get(0))));
            }

            // 测试testStructList方法
            if(true){
                System.out.println("Test Function testStructList start -------");
                List paramList = new ArrayList<>();
                paramList.add("testStructList".getBytes());

                List contractArgs = new ArrayList();
                List structList = new ArrayList();
                structList.add("structParam0");
                contractArgs.add(structList);

                paramList.add(contractArgs);
                byte[] params = BuildParams.createCodeParamsScript(paramList);

                String result = callContract(params, account, 20000, 500);
                List<String > resultList = JSON.parseObject(JSON.parseObject(result).getString("Result"), List.class);

                System.out.println("testStructList return size is:  " + resultList.size());
                System.out.println("testStructList first param return is:  " + new String(Hex.decode(resultList.get(0))));
            }

            // 测试testStructListAndStr方法，合约要求参数个数为2
            if(true){
                System.out.println("Test Function testStructListAndStr start -------");
                List paramList = new ArrayList<>();
                paramList.add("testStructListAndStr".getBytes());

                List contractArgs = new ArrayList();
                List structList = new ArrayList();
                structList.add("structParam0");
                contractArgs.add(structList);
                contractArgs.add("structParam1");

                paramList.add(contractArgs);
                byte[] params = BuildParams.createCodeParamsScript(paramList);

                String result = callContract(params, account, 20000, 500);
                List<String > resultList = JSON.parseObject(JSON.parseObject(result).getString("Result"), List.class);
                System.out.println("testStructListAndStr return size is:  " + resultList.size());
                System.out.println("testStructListAndStr first param return is:  " + new String(Hex.decode((String) JSON.parseObject(JSONObject.toJSON(resultList.get(0)).toString(), List.class).get(0))));
            }

            // 测试testMap方法，合约要求参数个数为2，此方法因与下一个测试方法有关，因此不能预执行
            if(true){
                System.out.println("Test Function testMap start -------");
                List paramList = new ArrayList<>();
                paramList.add("testMap".getBytes());

                List contractArgs = new ArrayList();
                contractArgs.add("key");
                contractArgs.add("value");

                paramList.add(contractArgs);
                byte[] params = BuildParams.createCodeParamsScript(paramList);

                String result = invokeContract(params, account, 20000, 500);
                System.out.println("testMap return is:  " + result);
            }

            // 测试testGetMap方法，合约要求参数个数为1，此测试依赖上一个功能测试正常完成
            if(true){
                System.out.println("Test Function testGetMap start -------");
                List paramList = new ArrayList<>();
                paramList.add("testGetMap".getBytes());

                List contractArgs = new ArrayList();
                contractArgs.add("key");

                paramList.add(contractArgs);
                byte[] params = BuildParams.createCodeParamsScript(paramList);

                String result = callContract(params, account, 20000, 500);
                System.out.println("testGetMap return is:  " + new String(Hex.decode(JSON.parseObject(result).getString("Result"))));
            }
        }
        catch (Exception e){
            e.printStackTrace();
        }
    }

    public static String callContract(byte[] params, Account payerAcct, long gaslimit, long gasprice) throws Exception{
        if(payerAcct == null){
            throw new SDKException("params should not be null");
        }
        if(gaslimit < 0 || gasprice< 0){
            throw new SDKException("gaslimit or gasprice should not be less than 0");
        }

        Transaction tx = ontSdk.vm().makeInvokeCodeTransaction(Helper.reverse(ontSdk.neovm().oep4().getContractAddress()),null,params,payerAcct.getAddressU160().toBase58(),gaslimit,gasprice);

        ontSdk.addSign(tx, payerAcct);
        Object result = ontSdk.getConnect().sendRawTransactionPreExec(tx.toHexString());

        return result.toString();
    }

    public static String invokeContract(byte[] params, Account payerAcct, long gaslimit, long gasprice) throws Exception{
        if(payerAcct == null){
            throw new SDKException("params should not be null");
        }
        if(gaslimit < 0 || gasprice< 0){
            throw new SDKException("gaslimit or gasprice should not be less than 0");
        }

        Transaction tx = ontSdk.vm().makeInvokeCodeTransaction(Helper.reverse(ontSdk.neovm().oep4().getContractAddress()),null,params,payerAcct.getAddressU160().toBase58(),gaslimit,gasprice);

        ontSdk.addSign(tx, payerAcct);
        Object result = ontSdk.getConnect().sendRawTransaction(tx.toHexString());

        return result.toString();
    }

    public static OntSdk getOntSdk() throws Exception{
        String ip = "http://127.0.0.1";
        String restUrl = ip + ":" + "20334";
        String rpcUrl = ip + ":" + "20336";
        String wsUrl = ip + "：" +  "20335";

        OntSdk wm = OntSdk.getInstance();
        wm.setRpc(rpcUrl);
        wm.setRestful(restUrl);
        wm.setDefaultConnect(wm.getRestful());
        wm.neovm().oep4().setContractAddress("1954074ccf71603c47954f578378deafde1115c4");
        wm.openWalletFile("nep5.json");

        return wm;
    }
}
