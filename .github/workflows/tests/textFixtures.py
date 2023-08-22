import unittest

def setUpModule():
    print('Running setUpModule')

def tearDownModule():
    print('Running tearDownModule')
    print(unittest.TestResult)

class HogeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Running setUpClass')
        pass

    @classmethod
    def tearDownClass(cls):
        print('Running tearDownClass')

    def setUp(self):
        print('Running setUp')

    def tearDown(self):
        print('Running tearDown')

    def test1(self):
        expected = 1
        actual = 1
        self.assertEqual(expected, actual)

HogeTest.setUp(self)