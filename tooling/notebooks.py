"""
Converts a Python solution file into a notebook with markdown and code cells.

- TODO: Refactor to avoid duplication with other tools that generate stubs.
- TODO: Add validation to ensure provided Python script is valid for notebook generation.
"""
import ast
import sys
import os
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

class Book:
    """Converts a Python solution file into a notebook with markdown and code cells."""

    @staticmethod
    def main(solution_path:str, notebook_path:str, stub:bool=True):
        if not os.path.isfile(solution_path):
            raise FileNotFoundError(f"Error: Solution file does not exist: {solution_path}")
        elif not solution_path.endswith(".py"):
            raise ValueError(f"Error: Solution file must be a `.py` file: {solution_path}")

        # Read the solution source code as text.
        source:str = ""
        with open(solution_path, "r", encoding="utf-8") as file:
            source = file.read()

        # Parse the source text into an AST.
        tree:ast.AST = ast.parse(source)

        # Create a new notebook instance.
        notebook:nbformat.NotebookNode = new_notebook()
        cells:list[nbformat.NotebookNode] = []

        # Add module docstring as the first markdown cell if present.
        module_doc:str|None = ast.get_docstring(tree)
        if module_doc:
            md = [
                f"# **{os.path.basename(solution_path)}**",
                "",
                module_doc,
                ""
            ]

            module_doc_node:nbformat.NotebookNode = new_markdown_cell("\n".join(md))
            cells.append(module_doc_node)

        # Process each top-level node in the AST.
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                Book.build_function(cells, source, node, stub)

        # Set the cells to the notebook.
        notebook.cells = cells

        # Write the notebook to file.
        with open(notebook_path, "w", encoding="utf-8") as file:
            nbformat.write(notebook, file)

        print(f"Notebook written to {notebook_path}")


    @staticmethod
    def build_function(cells:list[nbformat.NotebookNode], source:str, function:ast.FunctionDef, stub:bool) -> None:
        # Build function docstring as markdown cell if present.
        function_doc:str|None = ast.get_docstring(function)
        if function_doc:
            md = [
                f"## `{function.name}`",
                "",
                function_doc,
                ""
            ]
            function_doc_node:nbformat.NotebookNode = new_markdown_cell("\n".join(md))
            cells.append(function_doc_node)

        # Prepare function arguments.
        arguments:list[str] = []
        for parameter in function.args.args:
            arguments.append(parameter.arg)

        # Build function signature.
        signature:str = f"def {function.name}({', '.join(arguments)}):"

        # Build function body for code cell.
        code:str = ""
        if stub:
            # TODO: This is already done by another tool. Refactor to avoid duplication.
            code = f"{signature}\n    raise NotImplementedError()"
        else:
            # Get the actual code lines.
            code_lines:list[str] = source.splitlines()[function.lineno-1:function.end_lineno]
            code = "\n".join(code_lines)
        code_node:nbformat.NotebookNode = new_code_cell(code)
        cells.append(code_node)


# Entry Point
#--------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python book.py <solution_path> <notebook_path> <stub(True|False)>")
        print("Example: python book.py C01/solution.py C01/koans.ipynb True")
        sys.exit(1)

    solution_path:str = sys.argv[1]
    notebook_path:str = sys.argv[2]
    stub:bool = sys.argv[3].lower() == "true"

    print()
    print(f"{__loader__.name}:")
    print("- Source:".ljust(15), solution_path)
    print("- Notebook:".ljust(15), notebook_path)
    print("- Stub:".ljust(15), stub)
    print()
    Book.main(solution_path, notebook_path, stub)
    print()
