import re


def read_file(filename: str) -> list[str]:
    data = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            data.append(line.strip())
    return data


def create_stacks():
    return [['R', 'G', 'H', 'Q', 'B', 'S', 'T', 'N'],
            ['H', 'S', 'F', 'D', 'P', 'Z', 'J'],
            ['Z', 'H', 'V'],
            ['M', 'Z', 'J', 'F', 'G', 'H'],
            ['T', 'Z', 'C', 'D', 'L', 'M', 'S', 'R'],
            ['M', 'T', 'W', 'V', 'H', 'Z', 'J'],
            ['T', 'F', 'P', 'L', 'Z'],
            ['Q', 'V', 'W', 'S'],
            ['W', 'H', 'L', 'M', 'T', 'D', 'N', 'C']]


def process_instructions(data, stacks: list[list[str]], stack_input_line_num):
    instrs = data[stack_input_line_num:]
    search_pattern = r'move\s(?P<num_to_move>\d{1,2})\sfrom\s(?P<move_from>\d{1})\sto\s(?P<move_to>\d{1})'
    for instr in instrs:
        nums = re.match(search_pattern, instr)
        for _ in range(int(nums.group('num_to_move'))):
            stacks[int(nums.group('move_to'))-1].append(stacks[int(nums.group('move_from'))-1].pop())
    return stacks


def process_instructions_v2(data, stacks: list[list[str]], stack_input_line_num):
    instrs = data[stack_input_line_num:]
    search_pattern = r'move\s(?P<num_to_move>\d{1,2})\sfrom\s(?P<move_from>\d{1})\sto\s(?P<move_to>\d{1})'
    for instr in instrs:
        nums = re.match(search_pattern, instr)
        temp_crates = stacks[int(nums.group('move_from'))-1][-int(nums.group('num_to_move')):]
        del stacks[int(nums.group('move_from'))-1][-int(nums.group('num_to_move')):]
        stacks[int(nums.group('move_to'))-1].extend(temp_crates)
    return stacks


def get_top_crates(stacks: list[list[str]]):
    return [sub_stack[-1] for sub_stack in stacks]


def test():
    test_stacks = [['Z', 'N'],
                   ['M', 'C', 'D'],
                   ['P']]
    test_instrs = ['move 1 from 2 to 1',
                   'move 3 from 1 to 3',
                   'move 2 from 2 to 1',
                   'move 1 from 1 to 2']
    new_test_stacks = process_instructions_v2(test_instrs, test_stacks, 0)
    test_top_crates = get_top_crates(new_test_stacks)
    assert "".join(test_top_crates) == 'MCD'


def main():
    test()
    data = read_file('input.txt')
    stacks = create_stacks()
    new_stacks = process_instructions_v2(data, stacks, 10)
    top_crates = get_top_crates(new_stacks)
    print(f'The top crates are {"".join(top_crates)}')


if __name__ == '__main__':
    main()
