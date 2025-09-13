"""
Provides automated publishing features for Python koans.

This module will process a koan solution into a stubbed challenge file.

Usage:
    python stub.py <source.py> <destination.py>

Example:
    python stub.py solution.py exercise.py
"""
import ast
import sys
import koans
from .code import Syntax, Text

KOAN_MODULE:str = koans.__name__
KOAN_CHALLENGE:str = koans.koan.__name__

class Stub:

    @staticmethod
    def main(source_path:str, destination_path:str) -> None:
        # Read the Python source as text lines.
        with open(source_path, "r", encoding="utf-8") as file:
            lines:list[str] = file.readlines()

        # Parse the Python source text into an AST.
        module:ast.Module = ast.parse("".join(lines))

        # Find the `koans` import statements.
        koan_imports:list[ast.Import] = Syntax.imports_find(module, KOAN_MODULE)

        # Find all functions with the `koan_solution` decoration.
        koan_decorators:list[ast.expr] = Syntax.decorators_find(module, KOAN_CHALLENGE)

        # Find all functions with the `koan` decoration.
        koan_functions:list[ast.FunctionDef] = Syntax.functions_find(module, KOAN_CHALLENGE)

        # Remove the `koans` import statements.
        Stub.strip_imports(lines, koan_imports)

        # Remove koan decorators from functions.
        Stub.strip_decorators(lines, koan_decorators)

        # For each koan function, stub its body
        Stub.stub_functions(lines, koan_functions)

        # Write the new source to the destination file.
        with open(destination_path, "w", encoding="utf-8") as file:
            file.writelines(lines)


    @staticmethod
    def strip_imports(lines:list[str], koan_imports:list[ast.Import]) -> None:
        line_indexes:list[int] = []
        for koan_import in koan_imports:
            line_indexes.append(koan_import.lineno - 1)
        for index in sorted(line_indexes, reverse=True):
            lines[index] = ""


    @staticmethod
    def strip_decorators(lines:list[str], koan_decorators:list[ast.expr]) -> None:
        line_indexes:list[int] = []
        for koan_decorator in koan_decorators:
            line_indexes.append(koan_decorator.lineno - 1)
        for index in sorted(line_indexes, reverse=True):
            lines[index] = ""


    @staticmethod
    def stub_functions(lines:list[str], koan_functions:list[ast.FunctionDef]) -> None:
        for koan_function in sorted(koan_functions, key=lambda function: function.lineno, reverse=True):
            Stub.stub_function(lines, koan_function)


    @staticmethod
    def stub_function(lines:list[str], function:ast.FunctionDef) -> None:
        # Store the first and last line index of the function definition.
        first:int = function.lineno - 1
        last:int = function.end_lineno

        # Build new lines for the stubbed function.
        stubbed:list[str] = []

        # The first line is the function definition.
        stubbed.append(lines[first])

        # Copy docstring if present.
        # TODO: Consider copying the docstring content directly from the AST, then wrapping it.
        documentation:list[str] = Stub.get_documentation(lines, function)
        stubbed.extend(documentation)

        # Insert stub after docstring.
        indent:int = Text.indent_at(lines, first)
        indentation:str = " " * (indent + 4)
        stubbed.append(f"{indentation}raise NotImplementedError()\n")

        # Replace the function lines with stubbed lines.
        lines[first:last] = stubbed


    @staticmethod
    def get_documentation(lines:list[str], function:ast.FunctionDef) -> list[str]:
        first:int = function.lineno - 1
        last:int = function.end_lineno - 1
        documentation:list[str] = []
        inside_block:bool = False
        for line in lines[first:last]:
            if inside_block:
                documentation.append(line)
            elif Text.has_documentation(line):
                inside_block = not inside_block
                documentation.append(line)
        return documentation


# Entry Point
#--------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python stub.py <source.py> <destination.py>")
        print("Example: python stub.py solution.py exercise.py")
        sys.exit(1)

    source_path:str = sys.argv[1]
    destination_path:str = sys.argv[2]

    Stub.main(source_path, destination_path)
    print("\nPublished:")
    print("- Source:".ljust(15), source_path)
    print("- Destination:".ljust(15), destination_path)
