

def read_file(filename: str) -> str:
    data = ''
    with open(filename, 'r') as file:
        data = file.read()
    return data


def find_packet_start(data: str, start_message_size: int) -> int:
    left = 0
    right = start_message_size
    for right in range(right, len(data)):
        if len(set(data[left:right])) == len(data[left:right]):
            return right
        else:
            left += 1


def test():
    test_data = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
    test_packet_start = find_packet_start(test_data, 4)
    assert test_packet_start == 7


def main():
    test()
    data = read_file('input.txt')
    marker = find_packet_start(data, 4)
    print(f'{marker} characters need to be processed')


if __name__ == '__main__':
    main()
