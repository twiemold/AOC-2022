

def read_file(filename: str) -> list[str]:
    data = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            data.append(line)
    return data


def split_data(data: list[str]) -> list[list[int]]:
    main_list = []
    sub_list = []
    for line in data:
        if line == '\n':
            main_list.append(sub_list.copy())
            sub_list.clear()
        else:
            sub_list.append(int(line))
    return main_list


def find_max_sub_list(elves: list[list[int]]) -> int:
    max_sub = 0
    for elf in elves:
        sub_sum = sum(elf)
        if sub_sum > max_sub:
            max_sub = sub_sum
    return max_sub


def main():
    data = read_file('input.txt')
    split = split_data(data)
    max_sub = find_max_sub_list(split)
    print(f'The elf with the most Calories is carrying {max_sub} Calories')


if __name__ == '__main__':
    main()
