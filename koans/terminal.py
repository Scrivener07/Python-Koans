"""
Custom test runner and results for koans.

See:
- https://docs.python.org/3/library/unittest.html
- https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner
- https://docs.python.org/3/library/unittest.html#unittest.TestResult
"""
import unittest
from typing import Any, override
from koans.framework import ResultIcon


class TerminalResult(unittest.TextTestResult):
    """
    Custom test result to simplify output.
    Suppresses tracebacks, durations, and other verbose output.
    This is used for running koans on a terminal.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    @override
    def addSuccess(self, test:unittest.TestCase):
        self.stream.writeln()
        self.stream.writeln(f"{ResultIcon.Passed.value} SUCCESS in {test.id()}: Test passed successfully.")
        self.stream.writeln()


    @override
    def addFailure(self, test:unittest.TestCase, err):
        failure = (test, "This test has failed")
        self.failures.append(failure)
        self.stream.writeln()
        self.stream.writeln(f"{ResultIcon.Failed.value} FAIL in {test.id()}: Expected output not received.")
        self.stream.writeln(f"Hint: Your function's return value doesn't match what was expected.")
        self.stream.writeln()


    @override
    def addError(self, test:unittest.TestCase, err):
        error = (test, "This test had an error.")
        self.errors.append(error)
        self.stream.writeln()
        self.stream.writeln(f"{ResultIcon.Error.value} ERROR in {test.id()}: Test had an error.")
        self.stream.writeln(f"Hint: Check for syntax errors.")
        self.stream.writeln()



class TerminalRunner(unittest.TextTestRunner):
    """
    A custom test runner with simplified result output for terminals.
    """
    resultclass = TerminalResult


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.descriptions = True
        self.verbosity = 2


    @override
    def run(self, test: unittest.TestSuite | unittest.TestCase) -> unittest.TextTestResult | Any:
        result = super().run(test)

        if isinstance(test, unittest.TestSuite):
            status:bool = result.wasSuccessful()
            if status:
                print("\nAll tests passed! 🎉")
            else:
                print("\nSome tests have failed. Please review the messages above for hints.")

        if isinstance(test, unittest.TestCase):
            status:bool = result.wasSuccessful()
            if status:
                print(f"\n{test.id()} passed! 🎉")
            else:
                print(f"\n{test.id()} failed. Please review the messages above for hints.")

        return result



class TerminalService:

    @staticmethod
    def run_discover(start_directory:str, pattern:str) -> bool:
        loader:unittest.TestLoader = unittest.TestLoader()
        suite:unittest.TestSuite = loader.discover(start_directory, pattern)
        result:TerminalResult = TerminalService.run(suite)
        return result.wasSuccessful()


    @staticmethod
    def run_identity(identifier:str) -> bool:
        loader:unittest.TestLoader = unittest.TestLoader()
        suite:unittest.TestSuite = loader.loadTestsFromName(identifier)
        result:TerminalResult = TerminalService.run(suite)
        return result.wasSuccessful()


    @staticmethod
    def run(suite:unittest.TestSuite) -> TerminalResult:
        runner:TerminalRunner = TerminalRunner()
        result:TerminalResult = runner.run(suite)
        return result
