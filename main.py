import os

path = r'C:\Users\Difrat\Downloads'


class Sorter:
    def __init__(self, directory: str = None, exp_list: list = [], file_list: list = None):
        self.directory = directory
        self.exp_list = exp_list
        self.file_list = file_list

    def set_directory(self) -> None:
        directory = input('Введите путь к интересующей директории: ')
        if os.path.exists(directory):
            self.directory = directory

    def set_file_list(self):
        self.file_list = [item for item in os.listdir(self.directory) if os.path.isfile(self.directory + f'/{item}')]

    def get_directory(self) -> str:
        return self.directory

    def set_exp_list(self) -> None:
        if len(self.file_list) > 0:
            for item in self.file_list:
                exp = item.split('.')
                if exp[-1] not in self.exp_list:
                    self.exp_list.append(exp[-1])

    def create_directory(self) -> None:
        for dir_name in self.exp_list:
            if not os.path.exists(self.directory + f'/{dir_name}'):
                os.mkdir(self.directory + f'/{dir_name}')

    def sorting_files_to_folders(self) -> None:
        file_list = os.listdir(self.directory)
        for item in file_list:
            try:
                os.rename(f'{self.directory}' + f'/{item}', f'{self.directory}' + f'/{item.split(".")[-1]}'
                                                                                  f'/{item}')
            except Exception as Exc:
                print(Exc)


if __name__ == '__main__':
    s = Sorter()
    s.set_directory()
    if s.directory:
        s.set_exp_list()
    else:
        print(f'Директория не существует или указана неверно')
    s.create_directory()
    s.sorting_files_to_folders()
