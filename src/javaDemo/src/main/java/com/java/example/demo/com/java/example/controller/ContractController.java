package com.java.example.demo.com.java.example.controller;

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
    @RequestMapping(value = "/allTest", method = RequestMethod.GET)
    public void allTest() throws Exception{
        logger.info("ContractController allTest");
        ContractService.nameTest();
        ContractService.helloTest();
        ContractService.testHelloTest();
        ContractService.testListTest();
        ContractService.testListAndStrTest();
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
    @RequestMapping(value = "/deployContractTest", method = RequestMethod.GET)
    public void deployContractTest() throws Exception{
        logger.info("ContractController deployContractTest");
        ContractService.deployContractTest();
    }

    /**
     * helloTest
     */
    @RequestMapping(value = "/nameTest", method = RequestMethod.GET)
    public void nameTest() throws Exception{
        logger.info("ContractController nameTest");
        ContractService.nameTest();
    }

    /**
     * helloTest
     */
    @RequestMapping(value = "/helloTest", method = RequestMethod.GET)
    public void helloTest() throws Exception{
        logger.info("ContractController helloTest");
        ContractService.helloTest();
    }

    /**
     * testHelloTest
     */
    @RequestMapping(value = "/testHelloTest", method = RequestMethod.GET)
    public void testHelloTest() throws Exception{
        logger.info("ContractController testHelloTest");
        ContractService.testHelloTest();
    }

    /**
     * testNumListTest
     */
    @RequestMapping(value = "/testNumListTest", method = RequestMethod.GET)
    public void testNumListTest() throws Exception{
        logger.info("ContractController testNumListTest");
        ContractService.testListTest();
    }

    /**
     * testNumListAndStrTest
     */
    @RequestMapping(value = "/testNumListAndStrTest", method = RequestMethod.GET)
    public void testNumListAndStrTest() throws Exception{
        logger.info("ContractController testNumListAndStrTest");
        ContractService.testListAndStrTest();
    }

    /**
     * testStructListTest
     */
    @RequestMapping(value = "/testStructListTest", method = RequestMethod.GET)
    public void testStructListTest() throws Exception{
        logger.info("ContractController testStructListTest");
        ContractService.testStructListTest();
    }

    /**
     * testStructListAndStrTest
     */
    @RequestMapping(value = "/testStructListAndStrTest", method = RequestMethod.GET)
    public void testStructListAndStrTest() throws Exception{
        logger.info("ContractController testStructListAndStrTest");
        ContractService.testStructListAndStrTest();
    }

    /**
     * testMapTest
     */
    @RequestMapping(value = "/testMapTest", method = RequestMethod.GET)
    public void testMapTest() throws Exception{
        logger.info("ContractController testMapTest");
        ContractService.testMapTest();
    }

    /**
     * testGetMapTest
     */
    @RequestMapping(value = "/testGetMapTest", method = RequestMethod.GET)
    public void testGetMapTest() throws Exception{
        logger.info("ContractController testGetMapTest");
        ContractService.testGetMapTest();
    }

    /**
     * testMapInMapTest
     */
    @RequestMapping(value = "/testMapInMapTest", method = RequestMethod.GET)
    public void testMapInMapTest() throws Exception{
        logger.info("ContractController testMapInMapTest");
        ContractService.testMapInMapTest();
    }

    /**
     * testGetMapInMapTest
     */
    @RequestMapping(value = "/testGetMapInMapTest", method = RequestMethod.GET)
    public void testGetMapInMapTest() throws Exception{
        logger.info("ContractController testGetMapInMapTest");
        ContractService.testGetMapInMapTest();
    }


    /**
     * testTransferMultiTest
     */
    @RequestMapping(value = "/testTransferMultiTest", method = RequestMethod.GET)
    public void testTransferMultiTest() throws Exception{
        logger.info("ContractController testTransferMultiTest");
        ContractService.testTransferMultiTest();
    }
}
