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


def sum_priorities(letters: list[str]) -> int:
    priorities_dict = dict(zip(string.ascii_letters, (i for i in range(1, 53))))
    return sum([priorities_dict[letter] for letter in letters])


def test():
    test_repeat_letters = find_repeat_items(['vJrwpWtwJgWrhcsFMMfFFhFp'])
    assert test_repeat_letters == ['p']
    repeat_letters = ['p', 'L', 'P', 'v', 't', 's']
    assert sum_priorities(repeat_letters) == 157


def main():
    test()
    data = read_file('input.txt')
    repeat_letters = find_repeat_items(data)
    priorities_sum = sum_priorities(repeat_letters)
    print(f'The sum of the priorities is {priorities_sum}')


if __name__ == '__main__':
    main()