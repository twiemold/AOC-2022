import re
from dataclasses import dataclass


def read_file(filename: str) -> list[str]:
    data = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            data.append(line.strip())
    return data

@dataclass
class Folder:
    name: str
    size: int
    contains: list
    parent: int

def process_commands(commands: list[str]):
    commands = commands[1:]
    folder_pattern = r'dir\s(?P<dir_listing>\w+)'
    file_pattern = r'(?P<file_size>\d+)'
    cd_pattern = r'\$\scd\s(?P<dir_name>.+)'
    root_dir = Folder('/', 0, [], 0)
    working_dir = root_dir
    for command in commands:
        if re.match(folder_pattern, command):
            folder_match = re.match(folder_pattern, command)
            folder_name = folder_match.group('dir_listing')
            working_dir.contains.append(Folder(folder_name, 0, [], working_dir))
        elif re.match(file_pattern, command):
            file_match = re.match(file_pattern, command)
            file_size = int(file_match.group('file_size'))
            working_dir.size += file_size
        elif re.match(cd_pattern, command):
            cd_match = re.match(cd_pattern, command)
            new_dir = cd_match.group('dir_name')
            if new_dir == '..':
                working_dir.parent.size += working_dir.size
                working_dir = working_dir.parent
            else:
                for folder in working_dir.contains:
                    if folder.name == new_dir:
                        working_dir = folder
                        break
    root_dir.size += working_dir.size
    return root_dir


def sum_folders_of_size(root_dir, total, size):
    if not root_dir:
        return total
    total = sum_folders_of_size(root_dir[0].contains, total, size)
    new_list = root_dir[1:]
    total = sum_folders_of_size(new_list, total, size)
    if root_dir[0].size <= size:
        total += root_dir[0].size
    return total


def test():
    test_data = read_file('test_input.txt')
    test_root = process_commands(test_data)
    assert test_root.size == 48381165
    test_sum = sum_folders_of_size(test_root.contains, 0, 100000)
    assert test_sum == 95437


def main():
    test()
    data = read_file('input.txt')
    root = process_commands(data)
    sum_val = sum_folders_of_size(root.contains, 0, 100000)
    print(f'{sum_val} is the sum of folders less than 100000')


if __name__ == '__main__':
    main()
