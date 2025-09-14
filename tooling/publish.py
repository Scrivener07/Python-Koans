"""
Provides orchestration for publishing Python koan exercises.

Usage:
    python publish.py <configuration_file.json> <destination_folder>

Example:
    python publish.py projects.json _dist
"""
import os
import sys
import json
from .stage import Stage
from .notebooks import Book
from .pack import Pack

class Publish:
    """Orchestrates the publishing of multiple koan projects based on a configuration file."""


    @staticmethod
    def main(configuration_path:str, destination_path:str) -> None:
        """
        Publishes multiple koan projects based on a JSON configuration file.
        """
        # Read the configuration file.
        paths:list[str] = Publish.configuration_read(configuration_path)

        # Get the config file's directory to resolve relative paths.
        directory:str = os.path.dirname(os.path.abspath(configuration_path))

        # Process each project path in the configuration.
        for path in paths:
            # Take absolute path or resolve to the configuration file's directory.
            project_source:str = ""
            if os.path.isabs(path):
                project_source = path
            else:
                project_source = os.path.normpath(os.path.join(directory, path))

            # Extract the project name from the path (last folder name).
            project_name:str = os.path.basename(project_source)
            project_destination:str = os.path.join(destination_path, project_name)

            # Publish the project.
            Publish.project(project_source, project_name, project_destination)


    @staticmethod
    def project(project_source:str, project_name:str, project_destination:str) -> None:
        """
        Publishes a single koan project.
        """
        # Verify the source to be valid.
        if not os.path.exists(project_source):
            print(f"Ignoring: Source does not exist: {project_source}")
            return
        elif not os.path.isdir(project_source):
            print(f"Ignoring: Source is not a directory: {project_source}")
            return

        # Verify the destination to be valid.
        if os.path.exists(project_destination):
            print(f"Ignoring: Destination cannot already exist: {project_destination}")
            return

        print()
        print(f"Publishing project: {project_name}")
        print(f"- Source: {project_source}")
        print(f"- Destination: {project_destination}")
        Stage.main(project_source, project_destination)
        Book.main(os.path.join(project_source, "solution.py"), os.path.join(project_destination, "koans.ipynb"), stub=False)
        Pack.archive(project_destination)


    @staticmethod
    def configuration_read(file_path:str) -> list[str]:
        """
        Reads the JSON configuration file.
        """
        try:
            with open(file_path, "r") as file:
                configuration:list[str] = json.load(file)
            if not isinstance(configuration, list):
                raise ValueError("Configuration must be a list of project paths.")
            return configuration
        except json.JSONDecodeError as jsonDecodeError:
            print(f"Error parsing JSON configuration: {jsonDecodeError}")
            sys.exit(1)
        except Exception as exception:
            print(f"Error reading configuration file: {exception}")
            sys.exit(1)


# Entry Point
#--------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python publish.py <configuration_file.json> <destination_folder>")
        print("Example: python publish.py projects.json _dist")
        sys.exit(1)

    configuration_path:str = sys.argv[1]
    destination_path:str = sys.argv[2]

    print()
    print(f"{__loader__.name}:")
    print("- Configuration:".ljust(16), configuration_path)
    print("- Destination:".ljust(16), destination_path)
    print()
    Publish.main(configuration_path, destination_path)
    print()
