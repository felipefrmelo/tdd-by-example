from xUnit import TestCase, TestResult, TestSuite


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

    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert test.log == "setUp testMethod tearDown"

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert "1 run, 0 failed" == self.result.summary()

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert "1 run, 1 failed" == self.result.summary()

    def testFailedResultFormating(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert "1 run, 1 failed" == result.summary()

    def testFailedResultSetUp(self):
        test = WasExceptionSetup("testMethod")
        test.run(self.result)
        assert "1 run, 1 failed" == self.result.summary()

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))

        suite.run(self.result)

        assert "2 run, 1 failed" == self.result.summary()


suite = TestSuite()

suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResultFormating"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedResultSetUp"))
suite.add(TestCaseTest("testSuite"))

result = TestResult()
suite.run(result)

print(result.summary())
