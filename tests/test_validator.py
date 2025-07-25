import unittest
from src.path_explorator.core import PathValidator
from pathlib import Path
from utils import get_folder_test_path

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.test_folder = get_folder_test_path()
        self.validator = PathValidator(self.test_folder)

    def test_is_goes_beyond_limits(self):
        limit_path = self.test_folder
        safe_path = Path(limit_path / Path('movies/brat.movie'))
        unsafe_path = Path(Path.cwd() / Path('__init__.py'))
        is_safe = not self.validator.is_goes_beyond_limits(safe_path.__str__())
        is_unsafe = self.validator.is_goes_beyond_limits(unsafe_path.__str__())
        self.assertTrue(is_safe)
        self.assertTrue(is_unsafe)

    def test_is_path_rel_to_another_path(self):
        limit_path = '/home/butcho/python projects'
        rel_path = '/home/butcho/python projects/media_storage'
        unrel = '/home/butcho'
        unrel2 = '/home/butcho/Загрузки'
        is_rel = self.validator.is_path_rel_to_another_path(rel_path, limit_path)
        is_unrel = not self.validator.is_path_rel_to_another_path(unrel, limit_path)
        is_unrel2 = not self.validator.is_path_rel_to_another_path(unrel2, limit_path)
        assert is_rel == is_unrel == is_unrel2 == True