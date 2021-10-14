class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()

    def tearDown(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)

    def testMethod(self):
        self.log += " testMethod"

    def setUp(self):
        self.log = "setUp"

    def tearDown(self):
        self.log += " tearDown"
