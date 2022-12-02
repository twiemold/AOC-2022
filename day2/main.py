import enum

DRAW_POINTS = 3
WIN_POINTS = 6


class ScoreEnums(enum.IntEnum):
    ROCK_SCORE = 1
    PAPER_SCORE = 2
    SCISSORS_SCORE = 3


class ElfEnums(enum.Enum):
    ROCK_PLAY = 'A'
    PAPER_PLAY = 'B'
    SCISSORS_PLAY = 'C'


class SantaEnums(enum.Enum):
    ROCK_PLAY = 'X'
    PAPER_PLAY = 'Y'
    SCISSORS_PLAY = 'Z'


def will_win(elf_play, santa_play):
    win = False
    if elf_play == ElfEnums.ROCK_PLAY.value:
        if santa_play == SantaEnums.PAPER_PLAY.value:
            return True
    elif elf_play == ElfEnums.SCISSORS_PLAY.value:
        if santa_play == SantaEnums.ROCK_PLAY.value:
            return True
    elif elf_play == ElfEnums.PAPER_PLAY.value:
        if santa_play == SantaEnums.SCISSORS_PLAY.value:
            return True
    return win


def will_draw(elf_play, santa_play):
    draw = False
    if elf_play == ElfEnums.ROCK_PLAY.value and santa_play == SantaEnums.ROCK_PLAY.value:
        return True
    elif elf_play == ElfEnums.PAPER_PLAY.value and santa_play == SantaEnums.PAPER_PLAY.value:
        return True
    elif elf_play == ElfEnums.SCISSORS_PLAY.value and santa_play == SantaEnums.SCISSORS_PLAY.value:
        return True
    return draw


def read_file(filename: str) -> list[str]:
    data = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            data.append(line)
    return data


def create_dict(data):
    play_list = []
    for line in data:
        sub_list = []
        plays = line.split(' ')
        sub_list.append(plays[0])
        sub_list.append(plays[1].strip())
        play_list.append(sub_list)
    return play_list


def match_enum(enum_val):
    for val in SantaEnums:
        if enum_val == val.value:
            return val
    for val in ElfEnums:
        if enum_val == val.value:
            return val


def calculate_score(play_list):
    score_dict = {
        SantaEnums.ROCK_PLAY.value: ScoreEnums.ROCK_SCORE.value,
        SantaEnums.PAPER_PLAY.value: ScoreEnums.PAPER_SCORE.value,
        SantaEnums.SCISSORS_PLAY.value: ScoreEnums.SCISSORS_SCORE.value
    }
    score = 0
    for plays in play_list:
        score += score_dict[plays[1]]
        if will_draw(plays[0], plays[1]):
            score += DRAW_POINTS
        elif will_win(plays[0], plays[1]):
            score += WIN_POINTS
    return score


def test():
    test_plays = [
        ['A', 'Y'],
        ['B', 'X'],
        ['C', 'Z']
    ]
    score = calculate_score(test_plays)
    assert score == 15


def main():
    test()
    data = read_file('input.txt')
    play_dict = create_dict(data)
    score = calculate_score(play_dict)
    print(f'Your score will be {score}')


if __name__ == '__main__':
    main()
