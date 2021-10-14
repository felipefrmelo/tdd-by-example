from typing import List


class TestResult:

    def __init__(self) -> None:
        self.runCount = 0
        self.failedCount = 0

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

    def run(self, result: TestResult):
        result.testStarted()

        try:
            self.setUp()
            method = getattr(self, self.name)
            method()
        except Exception as e:
            result.testFailed()

        self.tearDown()

    def tearDown(self):
        pass


class TestSuite:

    def __init__(self) -> None:
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result: TestResult):
        for test in self.tests:
            test.run(result)

        return result
