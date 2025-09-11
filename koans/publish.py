"""
Provides automated publishing features for Python koans.

This module will process a koan solution into a stubbed challenge file.

Usage:
    python stub2.py <source.py> <destination.py>
"""
import ast
import sys
import koans

KOAN_MODULE:str = koans.__name__
KOAN_CHALLENGE:str = koans.koan.__name__

class Syntax:

    @staticmethod
    def imports_find(module:ast.Module, name:str) -> list[ast.Import]:
        found:list[ast.Import] = []
        for node in module.body:
            if isinstance(node, ast.ImportFrom) and node.module.startswith(name):
                found.append(node)
        return found


    @staticmethod
    def imports_strip(module:ast.Module, name:str) -> None:
        for node in module.body:
            if isinstance(node, ast.ImportFrom) and node.module.startswith(name):
                module.body.remove(node)
            elif isinstance(node, ast.Import) and node.names[0].name.startswith(name):
                module.body.remove(node)


    @staticmethod
    def functions_find(module:ast.Module, decoration:str) -> list[ast.FunctionDef]:
        functions:list[ast.FunctionDef] = []
        for node in module.body:
            if isinstance(node, ast.FunctionDef):
                for decorator in node.decorator_list:
                    if getattr(decorator, "id", None) == decoration:
                        functions.append(node)
        return functions


    @staticmethod
    def decorators_find(module:ast.Module, decoration:str) -> list[ast.expr]:
        decorators:list[ast.expr] = []
        for node in module.body:
            if isinstance(node, ast.FunctionDef):
                for decorator in node.decorator_list:
                    if getattr(decorator, "id", None) == decoration:
                        decorators.append(decorator)
        return decorators


class Publish:

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
        Publish.strip_imports(lines, koan_imports)

        # Remove koan decorators from functions.
        Publish.strip_decorators(lines, koan_decorators)

        # For each koan function, stub its body
        Publish.stub_functions(lines, koan_functions)

        # Write the new source to the destination file.
        with open(destination_path, "w", encoding="utf-8") as file:
            file.writelines(lines)


    @staticmethod
    def strip_imports(lines:list[str], koan_imports:list[ast.Import]) -> None:
        line_indexes:list[int] = []
        for koan_import in koan_imports:
            print(f"Koan import on line number {koan_import.lineno}")
            line_indexes.append(koan_import.lineno - 1)

        # Remove in reverse order to avoid messing up line numbers.
        for index in sorted(line_indexes, reverse=True):
            lines[index] = ""


    @staticmethod
    def strip_decorators(lines:list[str], koan_decorators:list[ast.expr]) -> None:
        line_indexes:list[int] = []
        for koan_decorator in koan_decorators:
            print(f"Koan decorator on line number {koan_decorator.lineno}")
            line_indexes.append(koan_decorator.lineno - 1)

        # Remove in reverse order to avoid messing up line numbers.
        for index in sorted(line_indexes, reverse=True):
            lines[index] = ""


    @staticmethod
    def stub_functions(lines:list[str], koan_functions:list[ast.FunctionDef]) -> None:
        for koan_function in sorted(koan_functions, key=lambda function: function.lineno, reverse=True):
            print(f"Koan function on line number {koan_function.lineno}")
            Publish.stub_function(lines, koan_function.lineno-1, koan_function.name)


    @staticmethod
    def stub_function(lines:list[str], line_index:int, function_name:str) -> None:
        lines_new:list[str] = []
        index:int = line_index
        indentation:int|None = None
        has_function:bool = False
        start_index = line_index
        while index < len(lines):
            line:str = lines[index]
            if not has_function:
                if line.lstrip().startswith(f"def {function_name}("):
                    has_function = True
                    indentation = len(line) - len(line.lstrip())
                    lines_new.append(line)
                    index += 1

                    # Copy docstring if present
                    if index < len(lines) and (lines[index].strip().startswith('"""') or lines[index].strip().startswith("'''")):
                        docstring_delimiter:str = lines[index].strip()[:3]
                        lines_new.append(lines[index])
                        index += 1
                        while index < len(lines):
                            lines_new.append(lines[index])
                            if lines[index].strip().endswith(docstring_delimiter):
                                index += 1
                                break
                            index += 1

                    # Insert stub after docstring
                    lines_new.append(" " * (indentation + 4) + "raise NotImplementedError()\n")
                    lines_new.append("\n")
                    lines_new.append("\n")

                    # Skip the rest of the function body
                    while index < len(lines):
                        next_line:str = lines[index]
                        if next_line.strip().startswith("def ") and (len(next_line) - len(next_line.lstrip())) <= indentation:
                            has_function = False
                            break
                        if next_line.strip() and (len(next_line) - len(next_line.lstrip())) <= indentation and not next_line.strip().startswith("@"):
                            has_function = False
                            break
                        index += 1
                    break # Done processing this function
                else:
                    break # Should not happen, but safety
            else:
                raise Exception(f"Unexpected state in stub_function at index {index}.")

        # Replace the original function lines with the stubbed lines.
        # The function's first and last line indexes are replaced.
        lines[start_index:index] = lines_new


# Entry Point
#--------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python stub2.py <source.py> <destination.py>")
        sys.exit(1)
    source_path:str = sys.argv[1]
    destination_path:str = sys.argv[2]
    Publish.main(source_path, destination_path)
