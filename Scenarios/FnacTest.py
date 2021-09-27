import unittest
import os
import HtmlTestRunner
import TestCase1
import TestCase2
import TestCase3
import TestCase4
import TestCase5
import TestCase6


current_directory = os.getcwd()

class TestSuite(unittest.TestCase):

    def test(self):

        consolidated_test = unittest.TestSuite()
        consolidated_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCase1.Test1),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCase2.Test2),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCase3.Test3),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCase4.Test4),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCase5.Test5),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCase6.Test6),
        ])

        html_runner = HtmlTestRunner.HTMLTestRunner(
            report_name='HTML Reporting using PyUnit',
            description='HTML Reporting using PyUnit & HTMLTestRunner')

        html_runner.run(consolidated_test)

if __name__ == '__main__':
    unittest.main()