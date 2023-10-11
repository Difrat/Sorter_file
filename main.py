import os

path = r'C:\Users\Difrat\Downloads'


class Sorter:
    def __init__(self, directory: str = None, exp_list: list = []):
        self.directory = directory
        self.exp_list = exp_list

    def set_directory(self) -> None:
        self.directory = input('Введите путь к интересующей директории: ')

    def get_directory(self) -> str:
        return self.directory

    def set_exp(self) -> None:
        file_list = os.listdir(self.directory)
        for item in file_list:
            exp = item.split('.')
            if len(exp) == 2:
                exp = exp[-1]
                if exp not in self.exp_list:
                    self.exp_list.append(exp)

    def create_directory(self):
        try:
            for dir_name in s.exp_list:
                os.mkdir(s.directory + f'/{dir_name}')
        except FileExistsError:
            print('!!!Attention!!! -> The directory already exists')

    def sorting_files_to_folders(self):
        file_list = os.listdir(self.directory)
        for item in file_list:
            try:
                os.rename(f'{self.get_directory()}' + f'/{item}', f'{self.get_directory()}' + f'/{item.split(".")[-1]}'
                                                                                              f'/{item}')
            except Exception:
                pass


# Need to fix sort
# Коммит

if __name__ == '__main__':
    s = Sorter()
    s.set_directory()
    print(s.directory)
    s.set_exp()
    print(s.exp_list)
    s.create_directory()
    s.sorting_files_to_folders()
