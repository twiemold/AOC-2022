import string


def read_file(filename: str) -> list[str]:
    data = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            data.append(line.strip())
    return data


def find_repeat_items(data: list[str]) -> list[str]:
    repeat_letters = []
    for line in data:
        item_set = set()
        for i in range(len(line)//2):
            if line[i] not in item_set:
                item_set.add(line[i])
        for i in range(len(line)//2, len(line)):
            if line[i] in item_set:
                repeat_letters.append(line[i])
                break
    return repeat_letters


def find_repeat_items_v2(bags: list[str]) -> list[str]:
    group_size = 3
    badges = []
    for i in range(0, len(bags), group_size):
        bag_one_set = set()
        bag_two_set = set()
        for j in range(len(bags[i])):
            if bags[i][j] not in bag_one_set:
                bag_one_set.add(bags[i][j])
        for j in range(len(bags[i+1])):
            if bags[i+1][j] in bag_one_set:
                bag_two_set.add(bags[i+1][j])
        for j in range(len(bags[i+2])):
            if bags[i+2][j] in bag_two_set:
                badges.append(bags[i+2][j])
                break
    return badges


def sum_priorities(letters: list[str]) -> int:
    priorities_dict = dict(zip(string.ascii_letters, (i for i in range(1, 53))))
    return sum([priorities_dict[letter] for letter in letters])


def test():
    test_repeat_letters = find_repeat_items_v2(['vJrwpWtwJgWrhcsFMMfFFhFp',
                                                'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
                                                'PmmdzqPrVvPwwTWBwg'])
    assert test_repeat_letters == ['r']
    repeat_letters = ['p', 'L', 'P', 'v', 't', 's']
    assert sum_priorities(repeat_letters) == 157


def main():
    test()
    data = read_file('input.txt')
    repeat_letters = find_repeat_items_v2(data)
    priorities_sum = sum_priorities(repeat_letters)
    print(f'The sum of the priorities is {priorities_sum}')


if __name__ == '__main__':
    main()