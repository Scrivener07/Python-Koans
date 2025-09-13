"""
Provides packaging functionality for Python koan distributions.

This module creates zip archives of koan projects for easy distribution.

Usage:
    from tooling.pack import Pack
    Pack.create_archives(["_dist/C01", "_dist/C02"])
"""
import os
import zipfile
from pathlib import Path

class Pack:
    """Provides methods for packaging koan distributions into zip archives."""


    @staticmethod
    def archives(directories:list[str], output_directory:str|None = None) -> list[str]:
        """
        Creates zip archives for the specified directories.
        """
        archives:list[str] = []
        for directory in directories:
            archive_path:str = Pack.archive(directory, output_directory)
            archives.append(archive_path)
        return archives


    @staticmethod
    def archive(directory:str, output_directory:str|None = None) -> str:
        """
        Archives the specified directory into a zip file.
        """
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Project path does not exist: {directory}")

        # Get project name (last part of the path)
        project_name:str = os.path.basename(os.path.normpath(directory))

        # Determine output directory
        archive_directory:str = output_directory if output_directory else os.path.dirname(directory)
        os.makedirs(archive_directory, exist_ok=True)

        # Create archive path
        archive_path:str = os.path.join(archive_directory, f"{project_name}.zip")

        # Create zip archive
        try:
            Pack.create(directory, archive_path)
            print(f"Created archive: {archive_path}")
        except Exception as exception:
            print(f"Error creating archive for {directory}: {exception}")
        return archive_path


    @staticmethod
    def create(source_directory:str, output_filename:str) -> None:
        """
        Creates a zip archive of the source directory.
        """
        source_path:Path = Path(source_directory)
        with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as file:
            for file_path in Pack.find_files(source_path):
                # Calculate the relative path for the zip file
                relative_path:Path = file_path.relative_to(source_path)
                file.write(file_path, relative_path)


    # TODO: Consider an explicit file manifest instead of filtering here.
    @staticmethod
    def find_files(directory:Path) -> list[Path]:
        """
        Finds all files in a directory recursively.
        """
        files:list[Path] = []
        for item in directory.rglob("*"):
            if "__pycache__" in str(item):
                continue
            elif str(item).endswith(".pyc"):
                continue
            elif item.is_file():
                files.append(item)
        return files
