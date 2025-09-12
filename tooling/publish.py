import os
import sys
from .stage import Stage

class Publish:

    SOURCE_FOLDERS:list[str] = [
        "C00",
        "C01",
        "C02",
        "C03",
        "C04",
        "C05",
        "C06"
    ]


    @staticmethod
    def main(source_path:str, destination_path:str) -> None:
        for folder in Publish.SOURCE_FOLDERS:
            project_source:str = os.path.join(source_path, folder)
            project_destination:str = os.path.join(destination_path, folder)
            if os.path.exists(project_source) and os.path.isdir(project_source):
                print(f"INFO: '{project_source}' | '{project_destination}'")
                Stage.main(project_source, project_destination)
            else:
                print(f"Source folder does not exist or is not a directory: {project_source}")


# Entry Point
#--------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python publish.py <source_folder> <destination_folder>")
        sys.exit(1)
    source_path:str = sys.argv[1]
    destination_path:str = sys.argv[2]
    Publish.main(source_path, destination_path)
    print("\nPublish:")
    print("- Source:".ljust(15), source_path)
    print("- Destination:".ljust(15), destination_path)
