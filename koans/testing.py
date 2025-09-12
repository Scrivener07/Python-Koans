"""
Custom test runner and results for koans.

See:
- https://docs.python.org/3/library/unittest.html
- https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner
- https://docs.python.org/3/library/unittest.html#unittest.TestResult
"""
import unittest


class KoanResult(unittest.TextTestResult):
    """
    Custom test result to simplify output.
    Suppresses tracebacks and shows only simple, friendly messages.
    """

    # TODO: Preserve critical information about the test.
    def addError(self, test, err):
        error = (test, "This test had an error.")
        self.errors.append(error)


    # TODO: Preserve critical information about the test.
    def addFailure(self, test, err):
        failure = (test, "This test has failed")
        self.failures.append(failure)


class KoanRunner(unittest.TextTestRunner):
    """
    A custom test runner with simplified result output.

    Use: `unittest.main(testRunner=KoanRunner())`
    """
    resultclass = KoanResult
