"""
Tests are run using their fully qualified name.
This may run multiple tests depending on the scope of the given identity specifier.

ID: `<...Folder>.<Module>.<Class>.<Method>`

Example: `C00.exercise_test.Testing.test_challenge_01`
"""
from enum import Enum


class ResultStatus(str, Enum):
    Passed = "passed"
    Failed = "failed"
    Error = "error"


class ResultIcon(str, Enum):
    Passed = "✅"
    Failed = "❌"
    Error = "💥"
