import sys
import unittest
from enum import Enum
from types import ModuleType
from koans.client import ClientService
from koans.terminal import TerminalService, TerminalRunner


class ExitCode(int, Enum):
    Success = 0
    """Complete success (all tests passed)."""
    Failure = 1
    """Functional failure (tests ran but some failed)."""
    Error = 2
    """System failures (test runner itself had problems)."""


class KoanLauncher:
    # Mode
    ARGUMENT_MODE:int = 1
    MODE_TERMINAL:str = "terminal"
    MODE_CLIENT:str = "client"

    # Commands
    ARGUMENT_COMMAND:int = 2
    COMMAND_DISCOVERY:str = "discovery"
    COMMAND_IDENTITY:str = "identity"

    # Command: Discovery
    ARGUMENT_TEST_PATTERN:int = 3
    ARGUMENT_START_DIRECTORY:int = 4
    TEST_PATTERN:str = "*_test.py"
    START_DIRECTORY:str = "."

    # Command: Identity
    ARGUMENT_IDENTIFIER:int = 3


    @staticmethod
    def execute(module:str|ModuleType|None) -> None:
        """
        Execute tests using a command line or terminal.
        Calling this will not work as expected without passing the module containing unit test classes.
        """
        unittest.main(module=module, testRunner=TerminalRunner())


    @staticmethod
    def main() -> None:
        mode:str = KoanLauncher.MODE_TERMINAL
        if len(sys.argv) > KoanLauncher.ARGUMENT_MODE:
            mode = sys.argv[KoanLauncher.ARGUMENT_MODE].lower()
            if mode != KoanLauncher.MODE_TERMINAL and mode != KoanLauncher.MODE_CLIENT:
                print(f"Unknown mode: {mode}")
                sys.exit(ExitCode.Error)
        else:
            sys.exit(ExitCode.Error)


        command:str = KoanLauncher.COMMAND_DISCOVERY
        if len(sys.argv) > KoanLauncher.ARGUMENT_COMMAND:
            command = sys.argv[KoanLauncher.ARGUMENT_COMMAND].lower()
        else:
            sys.exit(ExitCode.Error)


        if command == KoanLauncher.COMMAND_DISCOVERY:
            pattern:str = KoanLauncher.TEST_PATTERN
            if len(sys.argv) > KoanLauncher.ARGUMENT_TEST_PATTERN:
                pattern = sys.argv[KoanLauncher.ARGUMENT_TEST_PATTERN]

            start_directory:str = KoanLauncher.START_DIRECTORY
            if len(sys.argv) > KoanLauncher.ARGUMENT_START_DIRECTORY:
                start_directory = sys.argv[KoanLauncher.ARGUMENT_START_DIRECTORY]

            if mode == KoanLauncher.MODE_TERMINAL:
                if TerminalService.run_discover(start_directory, pattern):
                    sys.exit(ExitCode.Success)
                else:
                    sys.exit(ExitCode.Failure)

            elif mode == KoanLauncher.MODE_CLIENT:
                if ClientService.run_discover(start_directory, pattern):
                    sys.exit(ExitCode.Success)
                else:
                    sys.exit(ExitCode.Failure)


        elif command == KoanLauncher.COMMAND_IDENTITY:
            identifier:str = ""
            if len(sys.argv) > KoanLauncher.ARGUMENT_IDENTIFIER:
                identifier = sys.argv[KoanLauncher.ARGUMENT_IDENTIFIER]

            if mode == KoanLauncher.MODE_TERMINAL:
                if TerminalService.run_identity(identifier):
                    sys.exit(ExitCode.Success)
                else:
                    sys.exit(ExitCode.Failure)

            elif mode == KoanLauncher.MODE_CLIENT:
                if ClientService.run_identity(identifier):
                    sys.exit(ExitCode.Success)
                else:
                    sys.exit(ExitCode.Failure)

        else:
            print(f"Unknown command: {command}")
            sys.exit(ExitCode.Error)



# Entry Point (CLI)
#--------------------------------------------------
# Usage: python -m koans.launcher <source_folder> <destination_folder>
# Example:
#   python -m koans.launcher terminal identity exercise_test.Testing.test_challenge_01
# Example:
#   python -m koans.launcher client identity exercise_test.Testing.test_challenge_01

if __name__ == "__main__":
    KoanLauncher.main()
