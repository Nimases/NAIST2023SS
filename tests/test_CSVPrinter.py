import unittest
from NAIST23SS.CSVPrinter import CSVPrinter


def setUpModule():
    print('Running setUpModule')

def tearDownModule():
    print('Running tearDownModule')

class TestCSVPrinter(unittest.TestCase):

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
    
    "行数の確認"
    def test_read1(self):
        
        printer = CSVPrinter("sample.csv")
        line = printer.read()
        self.assertEqual(2, len(line))
        print("test1")

    def test_read2(self):

        printer = CSVPrinter("sample.csv")
        line = printer.read()
        test  = ["a", "a"]
        self.assertEqual(line[0], test)
        print("test2")

    def test_read3(self):
        try:
            printer = CSVPrinter("SSSample.csv")
            printer.read()
            unittest.TestCase.fail("This line should not be involved")
        except FileNotFoundError as e:
            self.assertTrue(1, 1)

if __name__ == "__main__":
    unittest.main()