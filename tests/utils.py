from pathlib import Path

def get_folder_test_path():
    return Path(Path.cwd().parent / Path('folder_tests'))