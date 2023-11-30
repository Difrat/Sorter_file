import os
import sys
from abc import ABC, abstractmethod
path = r'C:\Users\Difrat\Downloads'


class Absroot(ABC):
    @abstractmethod
    def set_directory(self) -> None:
        pass

    @abstractmethod
    def set_file_list(self) -> None:
        pass

    @abstractmethod
    def set_exp_list(self) -> None:
        pass

    @abstractmethod
    def get_directory(self) -> str:
        pass

    @abstractmethod
    def get_exp_list(self) -> list:
        pass

    @abstractmethod
    def get_file_list(self) -> list:
        pass

    @abstractmethod
    def create_directory(self) -> None:
        pass

    @abstractmethod
    def sorting_files_to_folders(self) -> None:
        pass


class Sorter(Absroot):
    def __init__(self, directory: str = None, exp_list: list = [], file_list: list = None):
        self.__directory = directory
        self.__exp_list = exp_list
        self.__file_list = file_list

    def set_directory(self) -> None:
        directory = input('\u001b[38;5;107mВведите путь к интересующей директории: ')
        if os.path.exists(directory):
            self.__directory = directory
        else:
            sys.exit(f'Attention!!! -> Директория не существует или указана неверно.')

    def set_file_list(self) -> None:
        self.__file_list = [item for item in os.listdir(self.__directory) if os.path.isfile(self.__directory +
                                                                                            f'/{item}')]

    def set_exp_list(self) -> None:
        if len(self.__file_list) > 0:
            for item in self.__file_list:
                exp = item.split('.')
                if exp[-1] not in self.__exp_list:
                    self.__exp_list.append(exp[-1])
        else:
            sys.exit(f'Attention!!! -> Отсутствуют файлы для сортировки.')

    def get_directory(self) -> str:
        return self.__directory

    def get_exp_list(self) -> list:
        return self.__exp_list

    def get_file_list(self) -> list:
        return self.__file_list

    def create_directory(self) -> None:
        for dir_name in self.__exp_list:
            if not os.path.exists(self.__directory + f'/{dir_name}'):
                os.mkdir(self.__directory + f'/{dir_name}')

    def sorting_files_to_folders(self) -> None:
        for item in self.__file_list:
            try:
                os.rename(f'{self.__directory}' + f'/{item}', f'{self.__directory}' + f'/{item.split(".")[-1]}'
                                                                                  f'/{item}')
            except Exception as Exc:
                print(Exc)


if __name__ == '__main__':
    s = Sorter()
    s.set_directory()
    s.set_file_list()
    s.set_exp_list()
    s.create_directory()
    s.sorting_files_to_folders()
    print(f'\u001b[38;5;107mSuccess -> Файлы успешно отсортированы.')
