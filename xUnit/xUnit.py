class TestResult:
    runCount = 0
    failedCount = 0
    def summary(self):
        return f"{self.runCount} run, {self.failedCount} failed"

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.failedCount += 1    

class TestCase:
    def __init__(self, name):
        self.name = name
        self.result = TestResult()

    def setUp(self):
        pass

    def run(self):
        self.result.testStarted()
        
        try:
            self.setUp()
            method = getattr(self, self.name)
            method()
        except Exception as e:
            self.result.testFailed()

        self.tearDown()
        return self.result

    def tearDown(self):
        pass


