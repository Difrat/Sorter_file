import unittest
from unittest.mock import patch
from main import Sorter


class MainTest(unittest.TestCase):

    @patch('builtins.input', return_value=r'C:\Users\Difrat\Downloads')
    def test_Sorter_set_directory(self, mock_input):
        sorter = Sorter()
        sorter.set_directory()
        self.assertEqual('C:\\Users\\Difrat\\Downloads', sorter.directory)

    @patch('builtins.input', return_value=r'C:\Users\Difrat\Downl')
    def test_exception_Sorter_set_directory(self, mock_input):
        sorter = Sorter()
        with self.assertRaises(SystemExit):
            sorter.set_directory()
