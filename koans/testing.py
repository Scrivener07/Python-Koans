"""
Custom test runner and results for koans.

See:
- https://docs.python.org/3/library/unittest.html
- https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner
- https://docs.python.org/3/library/unittest.html#unittest.TestResult
"""
import sys
from typing import override
import unittest


# TODO: Emoji characters need further testing.
#   They may not render correctly in all terminals or environments.
class KoanResult(unittest.TextTestResult):
    """
    Custom test result to simplify output.
    Suppresses tracebacks, durations, and other verbose output.
    """


    @override
    def addSuccess(self, test:unittest.TestCase):
        self.stream.writeln()
        self.stream.writeln(f"✅ SUCCESS in {test.id()}: Test passed successfully.")
        self.stream.writeln()


    @override
    def addError(self, test:unittest.TestCase, err):
        error = (test, "This test had an error.")
        self.errors.append(error)
        self.stream.writeln()
        self.stream.writeln(f"💥 ERROR in {test.id()}: Test had an error.")
        self.stream.writeln(f"Hint: Check for syntax errors.")
        self.stream.writeln()


    @override
    def addFailure(self, test:unittest.TestCase, err):
        failure = (test, "This test has failed")
        self.failures.append(failure)
        self.stream.writeln()
        self.stream.writeln(f"❌ FAIL in {test.id()}: Expected output not received.")
        self.stream.writeln(f"Hint: Your function's return value doesn't match what was expected.")
        self.stream.writeln()


#--------------------------------------------------


class KoanRunner(unittest.TextTestRunner):
    """
    A custom test runner with simplified result output.

    Use: `unittest.main(testRunner=KoanRunner())`
    """
    resultclass = KoanResult


#--------------------------------------------------


class KoanTester:
    START_DIRECTORY:str = "."
    TEST_PATTERN:str = "*_test.py"

    @staticmethod
    def main() -> None:
        pattern:str = KoanTester.TEST_PATTERN
        start:str = KoanTester.START_DIRECTORY

        if len(sys.argv) > 1:
            pattern = sys.argv[1]

        if len(sys.argv) > 2:
            start = sys.argv[2]

        success:bool = KoanTester.start(pattern, start)
        if success:
            sys.exit(0)
        else:
            sys.exit(1)


    @staticmethod
    def execute() -> None:
        """Execute tests using `KoanRunner`."""
        unittest.main(testRunner=KoanRunner())


    @staticmethod
    def start(pattern:str, start_directory:str) -> bool:
        """Custom test loader that uses `KoanRunner`."""
        # TODO: Learn more about this alternative way to get the default loader.
        # test_loader:unittest.TestLoader = unittest.defaultTestLoader

        #  TODO: Learn more about patching unittest to always use custom result class.
        # unittest.TextTestRunner.resultclass = KoanResult

        # Load tests
        loader:unittest.TestLoader = unittest.TestLoader()

        # Discover tests
        suite:unittest.TestSuite = KoanTester.discover(pattern, start_directory, loader)

        # Run tests with custom runner
        result:KoanResult = KoanTester.run(suite)

        # Check results.
        status:bool = result.wasSuccessful()
        if status:
            print("\nAll tests passed! 🎉")
        else:
            print("\nSome tests have failed. Please review the messages above for hints.")
        return status


    @staticmethod
    def discover(pattern:str, start_directory:str, loader:unittest.TestLoader) -> unittest.TestSuite:
        """
        Discover tests in the specified directory matching the given pattern.
        """
        suite:unittest.TestSuite = loader.discover(start_directory, pattern)
        return suite


    @staticmethod
    def run(suite:unittest.TestSuite) -> KoanResult:
        """
        Run the test suite using `KoanRunner`.
        """
        runner:KoanRunner = KoanRunner(verbosity=2)
        result:KoanResult = runner.run(suite)
        return result


# Entry Point (CLI)
#--------------------------------------------------
if __name__ == "__main__":
    KoanTester.main()
