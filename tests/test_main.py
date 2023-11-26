import unittest
import os
from unittest.mock import patch
from main import Sorter


@patch('builtins.input', return_value=r'C:\Users\Difrat\Downloads')
def create_object_Sorter(mock_input):
    Sorter_object = Sorter()
    Sorter_object.set_directory()
    Sorter_object.set_file_list()
    Sorter_object.set_exp_list()
    return Sorter_object


class MainTest(unittest.TestCase):

    def test_Sorter_set_directory(self):
        s = create_object_Sorter()
        self.assertEqual(r'C:\Users\Difrat\Downloads', s.directory)

    @patch('builtins.input', return_value=r'C:\Users\Difrat\Download')
    def test_exception_Sorter_set_directory(self, mock_input):
        s = Sorter()
        with self.assertRaises(SystemExit):
            s.set_directory()

    def test_set_file_list(self):
        s = create_object_Sorter()
        test_cases = os.listdir(s.directory)

        for file in test_cases:
            with self.subTest(input_string=file):
                self.assertIn(file, os.listdir(s.directory))

    def test_set_exp_list(self):
        s = create_object_Sorter()
        test_cases = s.exp_list
        for file in test_cases:
            with self.subTest(input_string=file):
                self.assertIn(file, os.listdir(s.directory))

    def test_exception_set_exp_list(self):
        s = create_object_Sorter()
        s.file_list.clear()
        with self.assertRaises(SystemExit):
            s.set_exp_list()
