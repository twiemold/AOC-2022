

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


def sum_sub_lists(elves: list[list[int]]) -> list[int]:
    new_list = []
    for elf in elves:
        sub_sum = sum(elf)
        new_list.append(sub_sum)
    return new_list


def top_three_elves(elves: list[int]) -> list[int]:
    elves.sort(reverse=True)
    return elves[:3]


def main():
    data = read_file('input.txt')
    split = split_data(data)
    sum_subs = sum_sub_lists(split)
    top_elves = top_three_elves(sum_subs)
    print(f'The 3 elves carrying the most Calories are carring {sum(top_elves)} Calories')


if __name__ == '__main__':
    main()
