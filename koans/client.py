"""
Custom test runner and results for koans.

See:
- https://docs.python.org/3/library/unittest.html
- https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner
- https://docs.python.org/3/library/unittest.html#unittest.TestResult
"""
import unittest
from typing import Any, override
from koans.framework import ResultStatus


class ClientResult(unittest.TextTestResult):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.successes:list[unittest.TestCase] = []


    @override
    def addSuccess(self, test:unittest.TestCase):
        self.successes.append(test)


    @override
    def addFailure(self, test:unittest.TestCase, err):
        failure:tuple[unittest.TestCase, str] = (
            test,
            "This test has failed"
        )
        self.failures.append(failure)


    @override
    def addError(self, test:unittest.TestCase, err):
        error:tuple[unittest.TestCase, str] = (
            test,
            "This test had an error."
        )
        self.errors.append(error)


    def encode(self) -> dict[str, Any]:
        duration:float = 0.0
        for _, case_duration in self.collectedDurations:
            duration += case_duration

        data:dict[str, Any] = {
            "wasSuccessful": self.wasSuccessful(),
            "summary": {
                "testsRun": self.testsRun,
                "passed": len(self.successes),
                "failed": len(self.failures),
                "errors": len(self.errors),
                "duration": duration
            }
        }

        cases:list[Any] = []

        for case_success in self.successes:
            resultCase:dict[str, Any] = {
                "id": case_success.id(),
                "status": ResultStatus.Passed.value,
                "message": "The test passed successfully.",
                "duration": self.duration_for(case_success)
            }
            cases.append(resultCase)

        for case_failure, reason in self.failures:
            resultCase:dict[str, Any] = {
                "id": case_failure.id(),
                "status": ResultStatus.Failed.value,
                "message": str(reason),
                "duration": self.duration_for(case_failure)
            }
            cases.append(resultCase)

        for case_error, reason in self.errors:
            resultCase:dict[str, Any] = {
                "id": case_error.id(),
                "status": ResultStatus.Error.value,
                "message": str(reason),
                "duration": self.duration_for(case_error)
            }
            cases.append(resultCase)

        data["cases"] = cases
        return data


    def duration(self) -> float:
        duration:float = 0.0
        for _, case_duration in self.collectedDurations:
            duration += case_duration
        return duration


    def duration_for(self, test_case:unittest.TestCase) -> float:
        for case_label, case_duration in self.collectedDurations:
            if case_label == f"{test_case._testMethodName} ({test_case.id()})":
                return case_duration



class ClientRunner(unittest.TextTestRunner):
    resultclass = ClientResult

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.descriptions = True
        self.verbosity = 2



class ClientService:

    @staticmethod
    def run_discover(start_directory:str, pattern:str) -> bool:
        loader:unittest.TestLoader = unittest.TestLoader()
        suite:unittest.TestSuite = loader.discover(start_directory, pattern)
        result:ClientResult = ClientService.run(suite)
        return result.wasSuccessful()


    @staticmethod
    def run_identity(identifier:str) -> bool:
        loader:unittest.TestLoader = unittest.TestLoader()
        suite:unittest.TestSuite = loader.loadTestsFromName(identifier)
        result:ClientResult = ClientService.run(suite)
        print(result.encode())
        return result.wasSuccessful()


    @staticmethod
    def run(suite:unittest.TestSuite) -> ClientResult:
        runner:ClientRunner = ClientRunner()
        result:ClientResult = runner.run(suite)
        return result
