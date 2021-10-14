from xUnit import TestCase, WasRun


class TestCaseTest(TestCase):

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert test.log == "setUp testMethod tearDown"


TestCaseTest("testTemplateMethod").run()
