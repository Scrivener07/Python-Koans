"""
Usage:
    `py_to_ipynb("C01/solution.py", "C01/koans.ipynb", stub=True)`
"""
import ast
import sys
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

class Book:
    """Converts a Python solution file into a notebook with markdown and code cells."""

    @staticmethod
    def main(solution_path:str, notebook_path:str, stub:bool=True):
        source:str = ""
        with open(solution_path, "r", encoding="utf-8") as file:
            source = file.read()
        tree:ast.AST = ast.parse(source)

        notebook:nbformat.NotebookNode = new_notebook()
        cells:list[nbformat.NotebookNode] = []

        # Add module docstring as the first markdown cell if present.
        module_doc:str|None = ast.get_docstring(tree)
        if module_doc:
            module_doc_node:nbformat.NotebookNode = new_markdown_cell(module_doc)
            cells.append(module_doc_node)

        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                # Add function docstring as markdown cell if present.
                function_doc:str|None = ast.get_docstring(node)
                if function_doc:
                    function_doc_node:nbformat.NotebookNode = new_markdown_cell(function_doc)
                    cells.append(function_doc_node)

                # Build function signature.
                arguments:list[str] = [parameter.arg for parameter in node.args.args]
                signature:str = f"def {node.name}({', '.join(arguments)}):"
                code:str = ""
                # TODO: This is already done by another tool. Refactor to avoid duplication.
                if stub:
                    code = f"{signature}\n    raise NotImplementedError()"
                else:
                    # Get the actual code lines.
                    code_lines:list[str] = source.splitlines()[node.lineno-1:node.end_lineno]
                    code = "\n".join(code_lines)
                code_node:nbformat.NotebookNode = new_code_cell(code)
                cells.append(code_node)

        # Set the cells to the notebook.
        notebook.cells = cells

        # Write the notebook to file.
        with open(notebook_path, "w", encoding="utf-8") as file:
            nbformat.write(notebook, file)

        print(f"Notebook written to {notebook_path}")


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

    Book.main(solution_path, notebook_path, stub)
