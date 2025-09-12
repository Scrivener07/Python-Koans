import ast

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


class Text:

    @staticmethod
    def indent_at(lines:list[str], index:int) -> int:
        """
        Gets the indentation level of the line at the given index.
        """
        return len(lines[index]) - len(lines[index].lstrip())


    @staticmethod
    def has_documentation(line:str) -> bool:
        return line.strip().startswith('"""') \
            or line.strip().startswith("'''") \
            or line.strip().endswith('"""') \
            or line.strip().endswith("'''")
