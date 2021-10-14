from xUnit import TestCase, TestResult

class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)

    def testMethod(self):
        self.log += " testMethod"

    def setUp(self):
        self.log = "setUp"

    def tearDown(self):
        self.log += " tearDown"
    
    def testBrokenMethod(self):
         raise Exception 

class WasExceptionSetup(TestCase):
    def setUp(self):
        raise Exception("Failure on setup")

class TestCaseTest(TestCase):

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert test.log == "setUp testMethod tearDown"

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()

    def testFailedResultFormating(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert "1 run, 1 failed" == result.summary()

    def testFailedResultSetUp(self):
        test = WasExceptionSetup("testMethod")
        result = test.run()
        
        assert "1 run, 1 failed" == result.summary()


print(TestCaseTest("testTemplateMethod").run().summary())
print(TestCaseTest("testResult").run().summary())
print(TestCaseTest("testFailedResultFormating").run().summary())
print(TestCaseTest("testFailedResult").run().summary())
print(TestCaseTest("testFailedResultSetUp").run().summary())