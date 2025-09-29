"""
Custom test runner and results for koans.

See:
- https://docs.python.org/3/library/unittest.html
- https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner
- https://docs.python.org/3/library/unittest.html#unittest.TestResult
"""
import sys
from enum import Enum
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


class ExitCode(Enum):
    Success = 0
    """Complete success (all tests passed)."""
    Failure = 1
    """Functional failure (tests ran but some failed)."""
    Error = 2
    """System failures (test runner itself had problems)."""



class KoanLauncher:
    ARGUMENT_MODE:int = 1
    MODE_DISCOVERY:str = "discovery"
    MODE_IDENTITY:str = "identity"

    # Discovery
    ARGUMENT_TEST_PATTERN:int = 2
    ARGUMENT_START_DIRECTORY:int = 3
    TEST_PATTERN:str = "*_test.py"
    START_DIRECTORY:str = "."

    # Identity
    ARGUMENT_IDENTIFIER:int = 2


    @staticmethod
    def execute() -> None:
        """Execute tests using `KoanRunner`."""
        # TODO: Calling this will not work as expected without passing the module containing unit test classes.
        unittest.main(testRunner=KoanRunner())


    @staticmethod
    def main() -> None:
        mode:str = KoanLauncher.MODE_DISCOVERY

        if len(sys.argv) > KoanLauncher.ARGUMENT_MODE:
            mode = sys.argv[KoanLauncher.ARGUMENT_MODE].lower()

        if mode == KoanLauncher.MODE_DISCOVERY:
            pattern:str = KoanLauncher.TEST_PATTERN
            if len(sys.argv) > KoanLauncher.ARGUMENT_TEST_PATTERN:
                pattern = sys.argv[KoanLauncher.ARGUMENT_TEST_PATTERN]

            start_directory:str = KoanLauncher.START_DIRECTORY
            if len(sys.argv) > KoanLauncher.ARGUMENT_START_DIRECTORY:
                start_directory = sys.argv[KoanLauncher.ARGUMENT_START_DIRECTORY]

            success:bool = KoanLauncher.run_discover(start_directory, pattern)
            if success:
                sys.exit(ExitCode.Success)
            else:
                sys.exit(ExitCode.Failure)

        elif mode == KoanLauncher.MODE_IDENTITY:
            identifier:str = ""
            if len(sys.argv) > KoanLauncher.ARGUMENT_IDENTIFIER:
                identifier = sys.argv[KoanLauncher.ARGUMENT_IDENTIFIER]

            success:bool = KoanLauncher.run_identity(identifier)
            if success:
                sys.exit(ExitCode.Success)
            else:
                sys.exit(ExitCode.Failure)
        else:
            print(f"Unknown mode: {mode}")
            sys.exit(ExitCode.Error)



    @staticmethod
    def run_discover(start_directory:str, pattern:str) -> bool:
        """Starts the Koan runner using test discovery with a directory pattern."""
        loader:unittest.TestLoader = unittest.TestLoader()

        # Discover tests that match the given pattern.
        suite:unittest.TestSuite = loader.discover(start_directory, pattern)
        print(f"Found {len(suite._tests)} test modules with {suite.countTestCases()} cases matching pattern '{pattern}' in '{start_directory}'.")
        print()

        # Run tests with custom runner.
        result:KoanResult = KoanLauncher.run(suite)

        # Check the results.
        status:bool = result.wasSuccessful()
        if status:
            print("\nAll tests passed! 🎉")
        else:
            print("\nSome tests have failed. Please review the messages above for hints.")
        return status


    @staticmethod
    def run_identity(identifier:str) -> bool:
        """
        Run a single test by its fully qualified name.
        This may run multiple tests depending on the given identity specifier.

        ID: `<Folder>.<Module>.<Class>.<Method>`

        Example: `C00.exercise_test.Testing.test_challenge_01`
        """
        loader:unittest.TestLoader = unittest.TestLoader()

        # Load tests that match the given identity.
        suite:unittest.TestSuite = loader.loadTestsFromName(identifier)
        if suite.countTestCases() == 0:
            print(f"No test found for: {identifier}")
            return False

        # Run tests with custom runner.
        result:KoanResult = KoanLauncher.run(suite)

        # Check the results.
        status:bool = result.wasSuccessful()
        if status:
            print(f"\n{identifier} passed! 🎉")
        else:
            print(f"\n{identifier} failed. Please review the messages above for hints.")
        return status


    @staticmethod
    def run(suite:unittest.TestSuite, verbosity:int=2) -> KoanResult:
        """
        Run the test suite using `KoanRunner`.
        """
        runner:KoanRunner = KoanRunner(descriptions=True, verbosity=verbosity)
        result:KoanResult = runner.run(suite)
        return result



# Entry Point (CLI)
#--------------------------------------------------
if __name__ == "__main__":
    KoanLauncher.main()
