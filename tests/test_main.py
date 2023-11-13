import unittest
from unittest.mock import patch
from main import Sorter


class MainTest(unittest.TestCase):

    @patch('builtins.input', return_value='/home/runner/work/')
    def test_Sorter_set_directory(self, mock_input):
        sorter = Sorter()
        sorter.set_directory()
        self.assertEqual('/home/runner/work/', sorter.directory)

    @patch('builtins.input', return_value='/home/runner/wor')
    def test_exception_Sorter_set_directory(self, mock_input):
        sorter = Sorter()
        with self.assertRaises(SystemExit):
            sorter.set_directory()
