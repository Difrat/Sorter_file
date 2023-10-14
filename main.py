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

    def set_exp_list(self) -> None:
        file_list = sorted(os.listdir(self.directory),
                           key=lambda x: os.path.isdir(self.directory + f'/{x}'))
        # file_list = sorted(os.listdir(self.directory), key=lambda x: os.path.isfile(self.directory + f'/{x}'))
        for item in file_list:
            exp = item.split('.')
            if exp[-1] not in self.exp_list and len(exp) == 2:
                self.exp_list.append(exp[-1])

    def create_directory(self):
        try:
            for dir_name in self.exp_list:
                os.mkdir(self.directory + f'/{dir_name}')
        except FileExistsError:
            print('!!!Attention!!! -> The directory already exists')

    def sorting_files_to_folders(self):
        file_list = os.listdir(self.directory)
        for item in file_list:
            try:
                os.rename(f'{self.get_directory()}' + f'/{item}', f'{self.directory}' + f'/{item.split(".")[-1]}'
                                                                                        f'/{item}')
            except Exception:
                pass


# Need to fix sort
# Next iteration but
if __name__ == '__main__':
    s = Sorter()
    s.set_directory()
    print(s.directory)
    s.set_exp_list()
    print(s.exp_list)
    s.create_directory()
    s.sorting_files_to_folders()
