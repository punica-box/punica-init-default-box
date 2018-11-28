package com.java.example.demo.com.java.exzample.comtroller;

import com.java.example.demo.com.java.example.service.ContractService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.autoconfigure.AutoConfigurationPackage;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author king
 * @version 1.0
 * @date 2018.11.28
 */
@AutoConfigurationPackage
@RestController
@RequestMapping(value="Contract", produces="application/json")
public class ContractController {
    private static Logger logger = LoggerFactory.getLogger(ContractController.class);

    /**
     * 发起测试请求
     */
    @RequestMapping(value = "/deployContractTest", method = RequestMethod.POST)
    public void deployContractTest() throws Exception{
        logger.info("ContractController deployContractTest");
        ContractService.deployContractTest();
    }

    /**
     * 发起测试请求
     */
    @RequestMapping(value = "/helloTest", method = RequestMethod.POST)
    public void helloTest() throws Exception{
        logger.info("ContractController helloTest");
        ContractService.helloTest();
    }

    /**
     * 发起测试请求
     */
    @RequestMapping(value = "/testHelloTest", method = RequestMethod.POST)
    public void testHelloTest() throws Exception{
        logger.info("ContractController testHelloTest");
        ContractService.testHelloTest();
    }

    /**
     * 发起测试请求
     */
    @RequestMapping(value = "/testNumListTest", method = RequestMethod.POST)
    public void testNumListTest() throws Exception{
        logger.info("ContractController testNumListTest");
        ContractService.testNumListTest();
    }

    /**
     * 发起测试请求
     */
    @RequestMapping(value = "/testNumListAndStrTest", method = RequestMethod.POST)
    public void testNumListAndStrTest() throws Exception{
        logger.info("ContractController testNumListAndStrTest");
        ContractService.testNumListAndStrTest();
    }

    /**
     * 发起测试请求
     */
    @RequestMapping(value = "/testStrListAndStrTest", method = RequestMethod.POST)
    public void testStrListAndStrTest() throws Exception{
        logger.info("ContractController testStrListAndStrTest");
        ContractService.testStrListAndStrTest();
    }

    /**
     * 发起测试请求
     */
    @RequestMapping(value = "/testByteArrayListAndStrTest", method = RequestMethod.POST)
    public void testByteArrayListAndStrTest() throws Exception{
        logger.info("ContractController testByteArrayListAndStrTest");
        ContractService.testByteArrayListAndStrTest();
    }

    /**
     * 发起测试请求
     */
    @RequestMapping(value = "/testStructListTest", method = RequestMethod.POST)
    public void testStructListTest() throws Exception{
        logger.info("ContractController testStructListTest");
        ContractService.testStructListTest();
    }

    /**
     * 发起测试请求
     */
    @RequestMapping(value = "/testStructListAndStrTest", method = RequestMethod.POST)
    public void testStructListAndStrTest() throws Exception{
        logger.info("ContractController testStructListAndStrTest");
        ContractService.testStructListAndStrTest();
    }

    /**
     * 发起测试请求
     */
    @RequestMapping(value = "/testMapTest", method = RequestMethod.POST)
    public void testMapTest() throws Exception{
        logger.info("ContractController testMapTest");
        ContractService.testMapTest();
    }

    /**
     * 发起测试请求
     */
    @RequestMapping(value = "/testGetMapTest", method = RequestMethod.POST)
    public void testGetMapTest() throws Exception{
        logger.info("ContractController testGetMapTest");
        ContractService.testGetMapTest();
    }

    /**
     * 发起测试请求
     */
    @RequestMapping(value = "/testMapInMapTest", method = RequestMethod.POST)
    public void testMapInMapTest() throws Exception{
        logger.info("ContractController testMapInMapTest");
        ContractService.testMapInMapTest();
    }

    /**
     * 发起测试请求
     */
    @RequestMapping(value = "/testGetMapInMapTest", method = RequestMethod.POST)
    public void testGetMapInMapTest() throws Exception{
        logger.info("ContractController testGetMapInMapTest");
        ContractService.testGetMapInMapTest();
    }


    /**
     * 发起测试请求
     */
    @RequestMapping(value = "/testTransferMultiTest", method = RequestMethod.POST)
    public void testTransferMultiTest() throws Exception{
        logger.info("ContractController testTransferMultiTest");
        ContractService.testTransferMultiTest();
    }
}
