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

class Publish:
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
            if os.path.isabs(path):
                project_source:str = path
            else:
                project_source:str = os.path.normpath(os.path.join(directory, path))

            # Extract the project name from the path (last folder name).
            project_name:str = os.path.basename(project_source)
            project_destination:str = os.path.join(destination_path, project_name)

            # Verify the source exists and is a directory.
            if os.path.exists(project_source) and os.path.isdir(project_source):
                print(f"\nProcessing project: {project_name}")
                print(f"- Source: {project_source}")
                print(f"- Destination: {project_destination}")
                Stage.main(project_source, project_destination)
            else:
                print(f"Error: Source does not exist or is not a directory: {project_source}")


    @staticmethod
    def configuration_read(file_path:str) -> list[str]:
        """
        Reads the JSON configuration file.
        """
        try:
            with open(file_path, "r") as file:
                config = json.load(file)

            # Validate the configuration.
            if not isinstance(config, list):
                raise ValueError("Configuration must be a list of project paths.")

            return config
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

    config_path:str = sys.argv[1]
    destination_path:str = sys.argv[2]

    Publish.main(config_path, destination_path)
    print("\nPublishing complete!")
    print("- Config:".ljust(15), config_path)
    print("- Destination:".ljust(15), destination_path)
