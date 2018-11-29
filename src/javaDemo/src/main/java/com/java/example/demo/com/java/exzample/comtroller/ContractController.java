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
     * allTest
     */
    @RequestMapping(value = "/allTest", method = RequestMethod.POST)
    public void allTest() throws Exception{
        logger.info("ContractController allTest");
        ContractService.helloTest();
        ContractService.testHelloTest();
        ContractService.testNumListTest();
        ContractService.testNumListAndStrTest();
        ContractService.testStrListAndStrTest();
        ContractService.testByteArrayListAndStrTest();
        ContractService.testStructListTest();
        ContractService.testStructListAndStrTest();
        ContractService.testMapTest();
        ContractService.testGetMapTest();
        ContractService.testMapInMapTest();
        ContractService.testGetMapInMapTest();
        ContractService.testTransferMultiTest();
    }

    /**
     * deployContractTest
     */
    @RequestMapping(value = "/deployContractTest", method = RequestMethod.POST)
    public void deployContractTest() throws Exception{
        logger.info("ContractController deployContractTest");
        ContractService.deployContractTest();
    }

    /**
     * helloTest
     */
    @RequestMapping(value = "/helloTest", method = RequestMethod.POST)
    public void helloTest() throws Exception{
        logger.info("ContractController helloTest");
        ContractService.helloTest();
    }

    /**
     * testHelloTest
     */
    @RequestMapping(value = "/testHelloTest", method = RequestMethod.POST)
    public void testHelloTest() throws Exception{
        logger.info("ContractController testHelloTest");
        ContractService.testHelloTest();
    }

    /**
     * testNumListTest
     */
    @RequestMapping(value = "/testNumListTest", method = RequestMethod.POST)
    public void testNumListTest() throws Exception{
        logger.info("ContractController testNumListTest");
        ContractService.testNumListTest();
    }

    /**
     * testNumListAndStrTest
     */
    @RequestMapping(value = "/testNumListAndStrTest", method = RequestMethod.POST)
    public void testNumListAndStrTest() throws Exception{
        logger.info("ContractController testNumListAndStrTest");
        ContractService.testNumListAndStrTest();
    }

    /**
     * testStrListAndStrTest
     */
    @RequestMapping(value = "/testStrListAndStrTest", method = RequestMethod.POST)
    public void testStrListAndStrTest() throws Exception{
        logger.info("ContractController testStrListAndStrTest");
        ContractService.testStrListAndStrTest();
    }

    /**
     * testByteArrayListAndStrTest
     */
    @RequestMapping(value = "/testByteArrayListAndStrTest", method = RequestMethod.POST)
    public void testByteArrayListAndStrTest() throws Exception{
        logger.info("ContractController testByteArrayListAndStrTest");
        ContractService.testByteArrayListAndStrTest();
    }

    /**
     * testStructListTest
     */
    @RequestMapping(value = "/testStructListTest", method = RequestMethod.POST)
    public void testStructListTest() throws Exception{
        logger.info("ContractController testStructListTest");
        ContractService.testStructListTest();
    }

    /**
     * testStructListAndStrTest
     */
    @RequestMapping(value = "/testStructListAndStrTest", method = RequestMethod.POST)
    public void testStructListAndStrTest() throws Exception{
        logger.info("ContractController testStructListAndStrTest");
        ContractService.testStructListAndStrTest();
    }

    /**
     * testMapTest
     */
    @RequestMapping(value = "/testMapTest", method = RequestMethod.POST)
    public void testMapTest() throws Exception{
        logger.info("ContractController testMapTest");
        ContractService.testMapTest();
    }

    /**
     * testGetMapTest
     */
    @RequestMapping(value = "/testGetMapTest", method = RequestMethod.POST)
    public void testGetMapTest() throws Exception{
        logger.info("ContractController testGetMapTest");
        ContractService.testGetMapTest();
    }

    /**
     * testMapInMapTest
     */
    @RequestMapping(value = "/testMapInMapTest", method = RequestMethod.POST)
    public void testMapInMapTest() throws Exception{
        logger.info("ContractController testMapInMapTest");
        ContractService.testMapInMapTest();
    }

    /**
     * testGetMapInMapTest
     */
    @RequestMapping(value = "/testGetMapInMapTest", method = RequestMethod.POST)
    public void testGetMapInMapTest() throws Exception{
        logger.info("ContractController testGetMapInMapTest");
        ContractService.testGetMapInMapTest();
    }


    /**
     * testTransferMultiTest
     */
    @RequestMapping(value = "/testTransferMultiTest", method = RequestMethod.POST)
    public void testTransferMultiTest() throws Exception{
        logger.info("ContractController testTransferMultiTest");
        ContractService.testTransferMultiTest();
    }
}
