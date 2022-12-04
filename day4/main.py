import re
from collections import namedtuple

ElfPair = namedtuple('elf_pair', ['e1_start', 'e1_end', 'e2_start', 'e2_end'])


def read_file(filename: str) -> list[str]:
    data = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            data.append(line.strip())
    return data


def create_pairs(data: list[str]) -> list[list[int]]:
    all_pairs = []
    search_pattern = r'(?:(?P<s1_start>\d{1,2})-(?P<s1_end>\d{1,2}),(?P<s2_start>\d{1,2})-(?P<s2_end>\d{1,2}))'
    for line in data:
        sections = re.match(search_pattern, line)
        all_pairs.append(ElfPair(int(sections.group('s1_start')), int(sections.group('s1_end')),
                                 int(sections.group('s2_start')), int(sections.group('s2_end'))))
    return all_pairs


def find_overlaps(elves):
    overlaps = 0
    for elf_pair in elves:
        if (elf_pair.e1_start <= elf_pair.e2_start and elf_pair.e1_end >= elf_pair.e2_end) or \
                (elf_pair.e2_start <= elf_pair.e1_start and elf_pair.e2_end >= elf_pair.e1_end):
            overlaps += 1
    return overlaps


def test():
    test_elf_pairs = [ElfPair(2, 4, 6, 8),
                      ElfPair(2, 3, 4, 5),
                      ElfPair(5, 7, 7, 9),
                      ElfPair(2, 8, 3, 7),
                      ElfPair(6, 6, 4, 6),
                      ElfPair(2, 6, 4, 8)]
    test_overlaps = find_overlaps(test_elf_pairs)
    assert test_overlaps == 2


def main():
    test()
    data = read_file('input.txt')
    all_pairs = create_pairs(data)
    overlaps = find_overlaps(all_pairs)
    print(f'The number of overlaps is {overlaps}')


if __name__ == '__main__':
    main()
