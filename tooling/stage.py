"""
Provides automation for distributions of koan exercises.

Usage:
    python stage.py <source_folder> <destination_folder>

Example:
    python stage.py C01 _dist/C01
"""
import os
import sys
import shutil
from .stub import Stub

class Stage:

    VSC_FOLDER:str = ".vscode"
    README_FILE:str = "README.md"
    SOLUTION_FILE:str = "solution.py"
    EXERCISE_FILE:str = "exercise.py"
    TEST_FILE:str = "exercise_test.py"
    DISTRIBUTION_FILES:list[str] = [README_FILE, EXERCISE_FILE, TEST_FILE]

    KOAN_MODULE:str = "koans"
    KOAN_FILES:list[str] = ["__init__.py", "testing.py"]


    @staticmethod
    def main(source_path:str, destination_path:str) -> None:

        # Create destination directory if it doesn't exist.
        os.makedirs(destination_path, exist_ok=True)

        # Generate exercise from solution.
        Stage.generate_exercise(source_path, destination_path)

        # Copy required files from source to destination.
        Stage.copy_files(source_path, destination_path)

        # Copy the koans module from the project root to destination.
        Stage.copy_koans_module(destination_path)

        # Update exercise_test.py to use the local koans module.
        Stage.update_test_imports(destination_path)

        print("\nDistribution created:", destination_path)


    @staticmethod
    def generate_exercise(source_path:str, destination_path:str) -> None:
        """Generates an exercise from a solution using publish module."""
        solution_path:str = os.path.join(source_path, Stage.SOLUTION_FILE)
        exercise_path:str = os.path.join(destination_path, Stage.EXERCISE_FILE)
        Stub.main(solution_path, exercise_path)
        print(f"Generated exercise: {exercise_path}")


    @staticmethod
    def copy_files(source_path:str, destination_path:str) -> None:
        """Copies essential files from source to destination."""

        # Copy .vscode folder if it exists.
        vsc_source:str = os.path.join(source_path, Stage.VSC_FOLDER)
        if os.path.exists(vsc_source):
            vsc_destination:str = os.path.join(destination_path, Stage.VSC_FOLDER)
            shutil.copytree(vsc_source, vsc_destination)
            print(f"Copied: {Stage.VSC_FOLDER} folder")
        else:
            print(f"Warning: {Stage.VSC_FOLDER} folder not found in source.")

        # Copy individual files.
        for file in Stage.DISTRIBUTION_FILES:
            source_file = os.path.join(source_path, file)
            if os.path.exists(source_file):
                shutil.copy2(source_file, os.path.join(destination_path, file))
                print(f"Copied: {file}")
            else:
                print(f"Warning: {file} not found in source.")


    @staticmethod
    def copy_koans_module(destination_path:str) -> None:
        """Copies the koans module to the destination."""
        koans_destination:str = os.path.join(destination_path, Stage.KOAN_MODULE)

        # Create destination koans directory.
        os.makedirs(koans_destination)

        # Copy only the essential files from koans module.
        for file in Stage.KOAN_FILES:
            source_file:str = os.path.join(Stage.KOAN_MODULE, file)
            if os.path.exists(source_file):
                shutil.copy2(source_file, os.path.join(koans_destination, file))
            else:
                print(f"Warning: {file} not found in {Stage.KOAN_MODULE} module.")
        print(f"Copied: {Stage.KOAN_MODULE} module")


    @staticmethod
    def update_test_imports(destination_path:str) -> None:
        """Updates imports in `exercise_test.py` to use local koans module."""
        test_file:str = os.path.join(destination_path, Stage.TEST_FILE)

        if not os.path.exists(test_file):
            print(f"Warning: {Stage.TEST_FILE} not found in destination.")
            return

        content:str = ""
        with open(test_file, "r", encoding="utf-8") as file:
            content = file.read()

        # Replace relative koans import with local import if needed.
        KOAN_IMPORT_FROM:str = "from ..koans.testing import KoanRunner"
        KOAN_IMPORT_TO:str = "from koans.testing import KoanRunner"
        if KOAN_IMPORT_FROM in content:
            content = content.replace(KOAN_IMPORT_FROM, KOAN_IMPORT_TO)
        else:
            print(f"Note: No koans import update needed in {Stage.TEST_FILE}")

        # Always ensure module is pointing to exercise, not solution.
        TEST_IMPORT_FROM:str = "from . import solution as exercise"
        TEST_IMPORT_TO:str = "from . import exercise"
        if TEST_IMPORT_FROM in content:
            content = content.replace(TEST_IMPORT_FROM, TEST_IMPORT_TO)
        else:
            print(f"Note: No solution import update needed in {Stage.TEST_FILE}")

        # Write back the updated Python source file.
        with open(test_file, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"Updated: {Stage.TEST_FILE} imports")


# Entry Point
#--------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python stage.py <source_folder> <destination_folder>")
        print("Example: python stage.py C01 _dist/C01")
        sys.exit(1)
    source_path:str = sys.argv[1]
    destination_path:str = sys.argv[2]
    Stage.main(source_path, destination_path)
    print("\nTool:")
    print("- Source:".ljust(15), source_path)
    print("- Destination:".ljust(15), destination_path)
