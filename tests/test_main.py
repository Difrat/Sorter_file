import unittest
import os
from unittest.mock import patch
from main import Sorter


class MainTest(unittest.TestCase):

    @patch('builtins.input', return_value=r'C:\Users\Difrat\Downloads')
    def test_Sorter_set_directory(self, mock_input):
        sorter = Sorter()
        sorter.set_directory()
        self.assertEqual(r'C:\Users\Difrat\Downloads', sorter.directory)

    @patch('builtins.input', return_value=r'C:\Users\Difrat\Download')
    def test_exception_Sorter_set_directory(self, mock_input):
        sorter = Sorter()
        with self.assertRaises(SystemExit):
            sorter.set_directory()

    @patch('builtins.input', return_value=r'C:\Users\Difrat\Downloads')
    def test_set_file_list(self, mock_input):
        sorter = Sorter()
        sorter.set_directory()
        sorter.set_file_list()
        print(sorter.file_list)
        print(tuple(os.listdir(sorter.directory)))
        test_cases = os.listdir(sorter.directory)

        for file in test_cases:
            with self.subTest(input_string=file):
                self.assertIn(file, os.listdir(sorter.directory))
